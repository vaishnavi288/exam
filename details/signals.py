from django.dispatch import receiver
from django.db.models.signals import pre_save
from details.models import student
@receiver(pre_save,sender=student)

def display(sender,instance,**kwargs):
    
  instance.name=instance.name.upper()
