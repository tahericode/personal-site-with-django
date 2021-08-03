from django.db import models
import os
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instanse, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instanse.id}-{instanse.full_name}{ext}"
    return f"personal/{final_name}"



class AdminInformation(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    brief_desc = models.CharField(max_length=200, verbose_name='توضیحات کوتاه')
    desc = models.TextField(verbose_name='توضیحات کامل')
    place_of_birth = models.CharField(max_length=200, verbose_name='محل تولد')
    address = models.CharField(max_length=200, verbose_name='محل سکونت')
    age = models.IntegerField(verbose_name='سن')
    gender = models.CharField(max_length=200, verbose_name='جنسیت')
    email = models.EmailField( max_length=254, verbose_name='ایمیل', blank=True, null = True)
    image = models.ImageField(upload_to=upload_image_path, height_field=None, width_field=None, verbose_name="عکس پروفایل", null = True, blank = True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'اطلاعات ادمین'
        verbose_name_plural = 'اطلاعات'

    def __str__(self):
        return self.full_name

