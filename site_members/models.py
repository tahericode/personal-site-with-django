from django.db import models
from django.db.models.fields import TextField
import os

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instanse, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instanse.id}-{instanse.name}{ext}"
    return f"members/{final_name}"



class Member(models.Model):
    desc = TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, height_field=None, width_field=None, max_length=None, verbose_name='عکس',blank = True,null = True)
    name = models.CharField( max_length=50, verbose_name='نام و نام خانوادگی')
    active = models.BooleanField(verbose_name='فعال', default=True)



    class Meta:
        verbose_name = 'اعضا تیم'
        verbose_name_plural = 'اعضا تیم'

    def __str__(self):
        return self.name





    
