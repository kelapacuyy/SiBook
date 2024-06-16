# Generated by Django 5.0.6 on 2024-06-16 02:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcommerce', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
