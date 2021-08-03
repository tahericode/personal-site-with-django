# Generated by Django 3.2.5 on 2021-07-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')),
                ('brief_desc', models.CharField(max_length=200, verbose_name='توضیحات کوتاه')),
                ('desc', models.TextField(verbose_name='توضیحات کامل')),
                ('place_of_birth', models.CharField(max_length=200, verbose_name='محل تولد')),
                ('address', models.CharField(max_length=200, verbose_name='محل سکونت')),
                ('age', models.IntegerField(verbose_name='سن')),
                ('gender', models.CharField(max_length=200, verbose_name='جنسیت')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'اطلاعات ادمین',
                'verbose_name_plural': 'اطلاعات',
            },
        ),
    ]