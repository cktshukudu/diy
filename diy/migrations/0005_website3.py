# Generated by Django 4.0.2 on 2022-05-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diy', '0004_website2_delete_image_remove_website_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='webSite3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htmlString', models.TextField()),
                ('companyName', models.CharField(default='No name', max_length=60)),
            ],
        ),
    ]