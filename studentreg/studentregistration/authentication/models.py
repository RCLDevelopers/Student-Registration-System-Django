from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=200)
    s_fathername = models.CharField(max_length=200)
    s_mothername = models.CharField(max_length=200)
    s_addr = models.CharField(max_length=200)
    s_school = models.CharField(max_length=200)
    s_email = models.EmailField(max_length=200)
    s_gender = models.CharField(max_length=200)
    s_class = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "%s %s %s " %(self.s_name, self.s_fathername, self.s_email)