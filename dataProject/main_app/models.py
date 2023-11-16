import os.path
import uuid

from django.db import models


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)

    ext = filename.split(".")
    full_name = f"{name}.{ext}"

    return os.path.join('employees', full_name)


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to=unique_img_name, null=True, default='employees/employee.png')
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now_add=True, null=True)  # Every time on update happens

    def __str__(self):
        return self.name

# python manage.py makemigrations
# python manage.py migrate
# python manage.py populate
