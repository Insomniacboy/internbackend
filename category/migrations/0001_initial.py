# Generated by Django 4.0.3 on 2022-03-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('position_id', models.IntegerField()),
                ('buy_or_sell', models.BooleanField()),
                ('subcategory', models.TextField()),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]