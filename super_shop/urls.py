from django.urls import path
from . import views

urlpatterns = [
    path('init_app/',views.init_app,name='init_app'),

    path('', views.home,name='home'),
    path('registration/',views.registrationPage,name='registrationPage'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logoutPage, name='logoutPage'),
    
    path('profile/<int:pk>', views.user_profile, name='user_profile'),
    path('edit_user/<int:pk>', views.edit_user, name='edit_user'),
    path('user/<int:pk>',views.profile_for_other,name='profile_for_other'),

    path('create_product/',views.create_product, name='create_product'),
    path('delete_product/<int:pk>', views.delete_adv, name='delete_adv'),
    path('change_status/<int:pk>', views.change_status, name='change_status'),

    path('advertisements/<int:possition>', views.advertisements, name='advertisements'),
    path('advertisements/show/<int:pk>', views.advertisements_window, name='advertisements_window'),
    path('create_advertisement/',views.create_advertisement, name='create_advertisement'),

    path('buy/<int:pk>',views.buy,name='buy'),
      
]