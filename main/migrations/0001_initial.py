# Generated by Django 4.2.16 on 2024-11-27 13:34

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.PositiveIntegerField(default=0)),
                ('agrees', models.ManyToManyField(blank=True, related_name='post_agrees', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
                ('disagrees', models.ManyToManyField(blank=True, related_name='post_disagrees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
