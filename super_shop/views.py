from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import authenticated_user,current_user_only
from math import floor
from django.core.mail import send_mail


from .models import Product, Advertisement, ShopUser
from .filters import AdvFilter
from .forms import *


""" Inicjalizacja aplikacji. Stworzenie grup admin i superuser oraz dodanie do nich superuser'a o nazwie 'admin'"""

def init_app(request):

    try:
        Group.objects.get(name='Admin')
        return redirect('home')
    except:   
        admin_group = Group(name='Admin')
        shopuser_group = Group(name='ShopUser')
        admin_group.save()
        shopuser_group.save()
        admin = User.objects.get(username='admin')
        ShopUser.objects.create(user=admin,username='admin')
        admin.groups.add(admin_group,shopuser_group)
            
        return redirect('home')
    

def home(request):
    
    return render(request,'home.html')


@authenticated_user
def registrationPage(request):
    
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()
  
            username = form.cleaned_data.get('username')
            messages.success(request,f'Dodano użytkownika {username}')
            return redirect('home')
        
        messages.error(request,'Cos poszło nie tak')
        print(form.errors)
        return redirect('registrationPage')
    
    context = {'form':form}
    return render(request,'registration.html',context)


@authenticated_user
def login_page(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,'Zalogowano')
            return redirect('home')
        
        else:
            messages.error(request,'Błędne dane')
            return redirect('login_page')
    
    
    context = {'form':form}
    return render(request,'login.html',context)


@login_required(login_url=('login_page'))
def logoutPage(request):
    
    logout(request)
    
    return redirect('login_page')




""" Profil użytkownika. Zastosoano dekorator dzięki któremu 
osoba inna niż właściciel profilu jest przekierowywana na stronę dla gości """


@login_required(login_url=('login_page'))
@current_user_only
def user_profile(request,pk):

    user = get_object_or_404(ShopUser,id=pk)
    products = user.products.all()
    advertisements = user.advertisement.all()

    context = {'user':user, 'products':products, 'advertisements':advertisements}
    return render(request,'user_profile.html',context)


def profile_for_other(request,pk):

    user = get_object_or_404(ShopUser,id=pk)
    advertisements = user.advertisement.all()

    context = {'user':user, 'advertisements':advertisements}
    return render(request,'profile_for_other.html',context)



@login_required(login_url=('login_page'))
def create_product(request):
    
    form = CreateProductForm()
    
    if request.method == 'POST':
        form = CreateProductForm(request.POST,request.FILES)
        if form.is_valid():

            product = form.save(commit=False)
            product.shopuser_id = request.user.shopuser.id
            product.save()

            return redirect('home')
    
    context = {'form':form}
    return render(request,'create_product.html',context)




""" Ogłszenie może dotyczyć kilku przedmiotów. Dlatego po przesłaniu formularza z zaznaczonymi przedmiotami,
    tworzę zmienną form która jest słownikiem list. 
    Listę produktów umieszczam w pętli która wydobywa obiekty produktów z bazy"""


@login_required(login_url=('login_page'))
def create_advertisement(request):
    
    form = CreateAdvertisementForm(user=request.user)
    products = Product.objects.filter(shopuser=request.user.id).all()

    
    if len(products) == 0:
        messages.error(request,'Nie posiadasz produktów które mógłbyś wystawić')
        return redirect('create_product')

    if request.method == 'POST':
        form = dict(request.POST.lists())      

        product = lambda i: Product.objects.get(id=i)       
        products = [product(i) for i in form['products']] 


        title = form['title'][0]
        description_adv = form['description_adv'][0]
        user = request.user.shopuser           
        available = True if form.get('available')[0] == 'on' else False

        adv = Advertisement(title=title,
                            description_adv=description_adv,
                            available=available,
                            shopuser=user)
        adv.save()
        adv.products.set(products)
         
        return redirect('home')

    context = {'form':form, 'products':products}
    return render(request,'create_advertisement.html',context)


@login_required(login_url=('login_page'))
def delete_adv(request,pk):

    adv = get_object_or_404(Advertisement,pk=pk)

    if request.method == 'POST':

        if request.POST['delete_form'] == '1':
            adv.delete()
            return redirect('user_profile',request.user.shopuser.id)
        else:
            return redirect('user_profile',request.user.shopuser.id)

    return render(request,'delete_adv.html')


@login_required(login_url=('login_page'))
def change_status(request,pk):

    adv = get_object_or_404(Advertisement,pk=pk)
    adv.available = (adv.available + 1) % 2
    adv.save()

    return redirect('user_profile',request.user.shopuser.id)



@login_required(login_url=('login_page'))
def edit_user(request,pk):
    
    user = ShopUser.objects.get(id=pk)
    form = EditUserProfile(instance=user)
    
    if request.method == 'POST':
        form = EditUserProfile(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()

            return redirect('user_profile',pk)
        
        else:
            messages.error(request,'Cos poszlo nie tak :(')
            return redirect('edit_user',pk)
    
    context = {'form':form}
    return render(request,'edit_user.html',context)



""" View advertisements ma za zadanie wyświetlić wszystkie ogłoszenia, po 6 na jednej stronie + okno filtrów.
    Jeśli ogłoszeń będzie więcej niż 6 zostanie wyświetlony licznik stron. Do tego służą zmienne counter i site.
    Counter zlicza potrzebne strony, a site to lista list ogłoszeń które mają być wyświetlone na jednej stronie.
    Jeśli liczba stron w counter jest wieksza niz 6 licznik wyswietli tylko pierwsza i pięć ostatnich """


def advertisements(request,possition):
    
    all_advertisements = Advertisement.objects.filter(available=True).all().order_by('-date_created')   
    if len(all_advertisements) == 0:
        messages.error(request,'Brak ogłoszeń')
        return redirect('home')

    filter = AdvFilter(request.GET,queryset=all_advertisements) 
    all_advertisements = filter.qs


    div = all_advertisements.count()/7
    counter = [1]
    for i in range(0,floor(div)):
        counter.append(counter[-1]+1)
    if len(counter) >= 6:
        first = counter[0:1]
        last = counter[-5:]
        counter = first + last
    

    sites = []
    one_page = []
    for i,item in enumerate(all_advertisements):
        if item.available == True:
            one_page.append(item) 
        else:
            pass
        if len(one_page) == 6 or i == len(all_advertisements)-1:
            sites.append(one_page.copy()) 
            one_page.clear()

    try:
        site = sites[int(possition)-1]
    except (ValueError,IndexError):
        return redirect('advertisements',1)

    context = {'all_advertisements': all_advertisements, 'counter':counter,'site':site,'filter':filter}
    return render(request,'advertisements.html',context) 


def advertisements_window(request,pk):

    adv = Advertisement.objects.get(pk=pk)
   
    context = {'adv':adv}
    return render(request,'advertisements_window.html',context)


@login_required(login_url=('login_page'))
def buy(request,pk):

    adv = Advertisement.objects.get(pk=pk)
    form = OrderForm()

    if request.method == 'POST':

        total_price = 0
        for price in adv.products.all():
            total_price += price.price

        Order.objects.create(total_price=total_price,
                             name = request.POST['name'],
                             surname = request.POST['surname'],
                             phone = request.POST['phone'],
                             address = request.POST['address'],
                             payment = request.POST['payment'],
                             buyer = request.user.shopuser,
                             seller = adv.shopuser,
                             advertisement = adv)
        
        adv.available = 0
        adv.save()

        return redirect('home')


    context = {'adv':adv,'form':form}
    return render(request,'buy.html',context)




