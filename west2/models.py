from django.db import models

# Create your models here.

class Character(models.Model):
    #objects = models.Manager()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Character2(models.Model):
    name = models.CharField(max_length=200)
    # def __unicode__(self):
    #     return self.name
class Character3(models.Model):
    name = models.CharField(max_length=200)
    # def __unicode__(self):
    #     return self.name
class Character4(models.Model):
    name = models.CharField(max_length=200)
    # def __unicode__(self):
    #     return self.name

