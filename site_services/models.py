from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Service(models.Model):
    logo_css = models.CharField( max_length=50, verbose_name='لوگو')
    title = models.CharField( max_length=50, verbose_name='عنوان')
    desc = TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'سرویس ها'
        verbose_name_plural = 'سرویس ها'

    def __str__(self):
        return self.title

