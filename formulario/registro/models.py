from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    photo = models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.username
