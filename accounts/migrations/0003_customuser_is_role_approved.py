# Generated by Django 5.1.7 on 2025-03-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_role_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_role_approved',
            field=models.BooleanField(default=True),
        ),
    ]
