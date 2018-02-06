from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


COMPANY_STATUS_CHOICES = (
    (0, 'Desabilitado'),
    (1, 'Habilitado'),
    (2, 'Demonstração'),
)
CHANNEL_STATUS_CHOICES = (
    (0, 'Desabilitado'),
    (1, 'Habilitado'),
)
LOG_EVENT_CHOICES = (
    (0, 'Informação'),
    (1, 'Erro'),
    (2, 'Aviso'),
)
NOTIFICATION_STYLE_CHOICES = (
    (0, 'Critical'),
    (1, 'Query'),
    (2, 'Warning'),
    (3, 'Information'),
)
PROFILE_ROLES_CHOICES = (
    (0, 'Espectador'),
    (1, 'Editor'),
    (2, 'Gerente'),
    (3, 'Administrador'),
)
BLOCK_RESOLUTION_CHOICES = (
    (0, '4K'),
    (1, 'HD 1080'),
    (2, 'HD 720'),
    (3, '480'),
    (4, '360'),
    (5, '270'),
  

)
BLOCK_STATUS_CHOICES = (
    (0, 'Indisponivel'),
    (1, 'Disponivel'),
)

# Create your models here.
  
class Channel(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.CharField(max_length=10, unique=True)
  hiresLifetime = models.PositiveSmallIntegerField(default=0)
  lowresLifetime = models.PositiveSmallIntegerField(default=0)
  logo = models.ImageField(upload_to='logo/', blank=True)
  status = models.PositiveSmallIntegerField(choices=CHANNEL_STATUS_CHOICES, default=0)
  
  def __str__(self):
    return self.name
  
class Company(models.Model):
  name = models.CharField(max_length=50, unique=True)
  numberLicenses = models.PositiveSmallIntegerField(default=0)
  status = models.PositiveSmallIntegerField(choices=COMPANY_STATUS_CHOICES, default=0)
  channel = models.ManyToManyField(Channel)
  
  def __str__(self):
    return self.name
  
class Clip(models.Model):
  channel = models.ForeignKey(Channel,on_delete=models.CASCADE, related_name='clips')
  recordDate = models.DateTimeField(null=True)
  length = models.PositiveSmallIntegerField(default=0)
  posterURL = models.ImageField(upload_to='poster/')
  thumbsURL = models.ImageField(upload_to='thumbs/')
  
class Log(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
  event = models.PositiveSmallIntegerField(choices=LOG_EVENT_CHOICES, default=0)
  eventDescription = models.CharField(max_length=250)
  createdAt = models.DateTimeField(auto_now_add=True)
  
class Notification(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
  description = models.CharField(max_length=250)
  style = models.PositiveSmallIntegerField(choices=NOTIFICATION_STYLE_CHOICES, default=0)
  createdAt = models.DateTimeField(auto_now_add=True)
  
class Block(models.Model):
  channel = models.ForeignKey(Channel,on_delete=models.CASCADE, related_name='blocks')
  clip = models.ForeignKey(Clip,on_delete=models.CASCADE, related_name='clip')
  resolution = models.PositiveSmallIntegerField(choices=BLOCK_RESOLUTION_CHOICES, default=3)
  url = models.URLField(blank=False)
  fileName = models.CharField(max_length=50, unique=True)
  fileHash = models.CharField(max_length=50, unique=True)
  sizeKB = models.PositiveIntegerField(default=0)
  status = models.PositiveSmallIntegerField(choices=BLOCK_STATUS_CHOICES, default=1)
  
class Favorite(models.Model):
  block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='favorites')
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
  frame = models.PositiveSmallIntegerField(default=0)
  description = models.CharField(max_length=250)
  
#class Profile(models.Model):
#  user = models.OneToOneField(User, on_delete=models.CASCADE)
#  company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
#  notifyByEmail = models.BooleanField()
#  roles = models.PositiveSmallIntegerField(choices=PROFILE_ROLES_CHOICES, default=1)  
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html 
#https://gist.github.com/jacobian/827937

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
    
  