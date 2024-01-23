# Generated by Django 4.2.9 on 2024-01-23 13:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('df_notifications', '0008_alter_custompushmessage_action_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPushNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='push_images')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('sent', models.DateTimeField(blank=True, db_index=True, editable=False, null=True)),
                ('audience', models.ManyToManyField(blank=True, help_text='Leave blank to send to all users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
