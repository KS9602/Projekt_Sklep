from django.shortcuts import redirect


"""'authenticated_user' - Funkcja sprawdza i przekirowuje użytkownika próbującego 
    dostać się do view zarezerwowanych tylko dla niezalogowanych (rejestracja/logowanie)"""

def authenticated_user(funv_view):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return funv_view(request,*args,**kwargs)
        
    return wrapper_func


""" 'current_user_only' i 'other_user_only' - Funkcje mają regulować treść wyświetlaną dla zalogowanych użytkowników.
    Przykładowo, będąc nie zalogowanym na koncie A zobaczysz inną treść na view profilu """


def current_user_only(func_view):
    def wrapper_func(request,pk,*args,**kwargs):
        if request.user.shopuser.id == pk:
            return func_view(request,pk,*args,**kwargs)
        else:
            return redirect('profile_for_other',pk)
    return wrapper_func


def other_user_only(func_view):
    def wrapper_func(request,pk,*args,**kwargs):
        if request.user.shopuser.id != pk:
            return func_view(request,pk,*args,**kwargs)
        else:
            return redirect('profile_for_other',pk)
    return wrapper_func