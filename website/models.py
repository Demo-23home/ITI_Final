from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.db import models
from django.contrib.auth.models import User





class CustomeUser(User):
    is_admin = models.BooleanField(default=False)







class Student(models.Model):
    username=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=100) 
    last_name= models.CharField(max_length=100) 
    phone_number= models.CharField(max_length=100) 
    email= models.CharField(max_length=100) 
    address= models.CharField(max_length=100) 
    city= models.CharField(max_length=100) 
    state= models.CharField(max_length=100) 
    zip_code= models.CharField(max_length=100) 
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username





class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_of_publish = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)  # Add the is_borrowed field

    # Create a foreign key relationship with User for borrowing
    borrower = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title









