from django.db import models

# Create your models here.

class Students (models.Model):
    name = models.CharField(max_length=100)
    std_id = models.IntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    dob = models.DateField()
    dept = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    image = models.ImageField(upload_to='student_img/', null= True, blank=True)

    def __str__(self):
        return self.name
