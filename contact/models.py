from django.db import models
from django.utils import timezone

objects = models.Manager()
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Person(models.Model) :
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250, default='Singapore')
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    #profilepic = models.ImageField()
    #profilepic = models.ImageField(upload_to='media' , blank=True)




    def publish(self) :
        self.published_date = timezone.now()
        self.save()

    def full_name(self) :
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self) :
        return self.full_name()

