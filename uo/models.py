from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
@receiver(post_migrate)
def create_enseignants(sender, **kwargs):
    User.objects.get_or_create(username='e1', email='e1@e.com', password='p')
    User.objects.get_or_create(username='e2', email='e2@e.com', password='p')
    User.objects.get_or_create(username='e3', email='e3@e.com', password='p')
    User.objects.get_or_create(username='e4', email='e4@e.com', password='p')

class Formation(models.Model):
    intitule = models.CharField(max_length =100)
    description = models.TextField()
    responsable = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.intitule
