# Generated by Django 3.2.14 on 2022-07-19 16:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0003_auto_20220719_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(null=True, related_name='likepost', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='unlike',
            field=models.ManyToManyField(null=True, related_name='unlikepost', to=settings.AUTH_USER_MODEL),
        ),
    ]