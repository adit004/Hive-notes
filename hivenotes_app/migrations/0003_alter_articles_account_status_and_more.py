# Generated by Django 5.2.3 on 2025-06-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivenotes_app', '0002_alter_articles_account_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='account_status',
            field=models.CharField(choices=[('denied', 'denied'), ('approved', 'approved'), ('pending', 'pending')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='loginview',
            name='account_status',
            field=models.CharField(choices=[('denied', 'denied'), ('accepted', 'accepted'), ('pending', 'pending')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='members',
            name='account_status',
            field=models.CharField(choices=[('denied', 'denied'), ('accepted', 'accepted'), ('pending', 'pending')], default='pending', max_length=10),
        ),
    ]
