# Generated by Django 3.2.9 on 2022-06-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_doctor_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='doctors'),
        ),
    ]