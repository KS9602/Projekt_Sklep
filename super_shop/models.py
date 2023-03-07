from django.db import models
from django.contrib.auth.models import User

class ShopUser(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.SmallIntegerField()
    profile_img = models.ImageField(default='default_pic.jpg',upload_to='user_imgs/',
                                    help_text='Allowed file types: jpg, jpeg, png')
    address = models.TextField()
    date_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.username}'


    
class Product(models.Model):
    
    class Category(models.TextChoices):

        SPORT = 0,'Sport'
        DOM = 1,'Dom'
        ELEKTRONIKA = 2,'Elektronika'
        URODA = 3,'Uroda'
        ROZRYWKA = 4,'Rozrywka'
        ODZIEZ = 5,'Odzież'
        MOTORYZACJA = 6,'Motoryzacja'

    class Status(models.TextChoices):

        NOWY = 0,'Nowy'
        UZYWANY = 1,'Używany'


    name = models.CharField('Nazwa produktu:',max_length=150)   
    price = models.FloatField('Cena:')
    quantity = models.PositiveIntegerField('Ilosc',default=1)
    status = models.CharField(max_length=40,choices=Status.choices)
    description_product = models.TextField('Opis:')
    date_created = models.DateField(auto_now_add=True)
    tag = models.CharField(max_length=40,choices=Category.choices)
    image = models.ImageField(default='default_item.jpg',null=True,blank=True,             
                              help_text='Allowed file types: jpg, jpeg, png')
    
    shopuser = models.ForeignKey(ShopUser,blank=True,on_delete=models.CASCADE,related_name='products')

    
    def __str__(self):
        return f'{self.name}'
    


class Advertisement(models.Model):
    
    title = models.CharField('Tytul: ',max_length=20)   
    description_adv = models.TextField('Tresc ogloszenia: ')
    available = models.BooleanField('Czy ogloszenie ma byc aktywne',default=True)
    date_created = models.DateField(auto_now_add=True) 
    
    products = models.ManyToManyField(Product)
    shopuser = models.ForeignKey(ShopUser,on_delete=models.CASCADE,null=False,blank=False,related_name='advertisement')
    
    def __str__(self):
        return f'{self.title}'
    


class Order(models.Model):

    class Payment(models.TextChoices):

        CASH = 0,'Gotowka'
        BLIK = 1,'Blik'
        TRANSFER = 2,'Przelew'
    
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.SmallIntegerField()
    address = models.TextField()
    payment = models.CharField(max_length=40,choices=Payment.choices)

    date_created = models.DateField(auto_now_add=True) 
    
    buyer = models.ForeignKey(ShopUser,on_delete=models.CASCADE,null=False,blank=False,related_name='buyer')
    seller = models.ForeignKey(ShopUser,on_delete=models.CASCADE,null=False,blank=False,related_name='seller')
    advertisement = models.ForeignKey(Advertisement,null=False,blank=False,on_delete=models.CASCADE,related_name='order')
    


