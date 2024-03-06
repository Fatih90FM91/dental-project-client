from django.db import models
from django.urls import reverse




class Register(models.Model):

    class FindingType(models.TextChoices):
        INTERNET = 'Via Internet'
        ADS = 'Outdour Ads'
        VIA_FAMILY = 'Family'
        VIA_FRIEND = 'Friend and Neigbors'
        SOCIAL_MEDIA = 'Social Media'
        GOOGLE = 'Internet Search Engine via Google'
        ALREADY_PATIENT = 'Already Patient'
        OTHER = 'Other'
    
    class GenderType(models.TextChoices):
        MAN = 'Man'
        WOMAN = 'Woman'
        LIKE_NEITHER  = 'Like Neither'

    class MemberType(models.TextChoices):
        YES = 'Yes'
        NO = 'No'
        
       

    
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=50, choices=GenderType.choices, default=GenderType.MAN)
    email = models.CharField(max_length=150, unique=True, blank=False, error_messages ={"unique":"The Email Field you entered already exists."})
    phone = models.CharField(max_length=150, blank=True)
    date_of_birth = models.CharField(max_length=150)
    house_number = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zipcode = models.CharField(max_length=15, blank=False)
    street = models.CharField(max_length=200, blank=False)
    how_hear_about_us = models.CharField(max_length=50, blank=False, choices=FindingType.choices, default=FindingType.VIA_FRIEND)
    question = models.TextField(blank=True)
    are_you_member = models.CharField(max_length=50, blank=False, choices=MemberType.choices, default=MemberType.YES)



    def __str__(self):
        return self.first_name  + '  ' +  str(self.last_name)  + ' | ' + str(self.email)
    

    def get_absolute_url(self):
        return reverse("home")


    

