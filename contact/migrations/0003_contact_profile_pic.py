# Generated by Django 4.1.7 on 2023-03-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profile_pic',
            field=models.ImageField(default='default', upload_to='profile_pics'),
            preserve_default=False,
        ),
    ]
