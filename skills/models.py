from django.db import models

# Create your models here.

class ModelManager(models.Manager):
    def get_code_skills(self):
        return self.get_queryset().filter(title = 'code')

class AdminSkill(models.Model):
    title = models.CharField(max_length=100, verbose_name='code | design')
    skill_name = models.CharField(max_length=150, verbose_name='نام مهارت')
    percent = models.IntegerField(verbose_name='درصد داشتن مهارت')
    
    objects = ModelManager()


    class Meta:
        verbose_name = 'مهارت ادمین'
        verbose_name_plural = 'مهارت های ادمین'

    def __str__(self):
        return self.skill_name

