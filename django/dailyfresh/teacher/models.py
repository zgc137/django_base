from django.db import models

# Create your models here.
class Student(models.Model):
    c_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(null=True)
    sex = models.SmallIntegerField(default=1)
    qq = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name