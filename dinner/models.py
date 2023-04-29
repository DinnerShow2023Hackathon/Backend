from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=10, blank=False, null=False)
    phonenum = models.CharField(max_length=13, blank=False, null=False)

class Bookpost(models.Model):
    whos = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=20, blank=False, null=False)
    contents = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='dinner', null=True)

    def __str__(self):
        return self.title