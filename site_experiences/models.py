from django.db import models

# Create your models here.
class Experience(models.Model):
    year = models.IntegerField(verbose_name='سال آموزش')
    title = models.CharField(max_length=200, verbose_name='عنوان دوره یا اموزش')
    address = models.CharField( max_length=50, verbose_name='محل گذراندن دوره یا آموزش')
    desc =models.TextField(verbose_name= 'توضیحات')

    class Meta:
        verbose_name = 'تجربه های کاری'
        verbose_name_plural = 'تجربه های کاری'

    def __str__(self):
        return self.title

