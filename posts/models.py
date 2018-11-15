from django.db import models

# Create your models here.


class Person(models.Model):
   # id = models.IntegerField(primary_key=True)
    client = models.CharField("browser", max_length=200)  #, primary_key=True
    date = models.DateTimeField("Date created", auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"