# Generated by Django 3.2.7 on 2021-09-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='account.Profile'),
        ),
    ]
