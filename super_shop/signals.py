from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save



from .models import ShopUser

@receiver(post_save,sender=User)
def shopUserCreated(sender,instance,created, **kwargs):
    if created:
        
            group = Group.objects.get(name='ShopUser')
            instance.groups.add(group)
            ShopUser.objects.create( user = instance, username = instance.username)




            