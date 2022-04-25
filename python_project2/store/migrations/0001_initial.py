# Generated by Django 4.0.4 on 2022-04-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='no owner', max_length=100)),
                ('name', models.CharField(default='no item name', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('type', models.CharField(default='no item type', max_length=100)),
                ('description', models.TextField(default='no description')),
                ('comments', models.TextField(default='no comments')),
                ('likes', models.IntegerField(default=0)),
                ('size', models.CharField(default='no size', max_length=100)),
                ('details', models.TextField(default='no details')),
            ],
        ),
    ]