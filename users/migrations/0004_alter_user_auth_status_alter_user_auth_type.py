# Generated by Django 5.0.3 on 2024-05-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_auth_status_user_auth_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_status',
            field=models.CharField(choices=[('new', 'new'), ('code_verified', 'code_verified'), ('done', 'done'), ('photo_done', 'photo_done')], default='new', max_length=31),
        ),
        migrations.AlterField(
            model_name='user',
            name='auth_type',
            field=models.CharField(choices=[('via_phone', 'via_phone'), ('via_email', 'via_email')], max_length=31),
        ),
    ]
