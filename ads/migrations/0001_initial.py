# Generated by Django 4.0.3 on 2022-03-21 10:49

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
                ('desc', models.TextField()),
                ('price', models.TextField()),
                ('phone', models.TextField()),
                ('category_id', models.TextField()),
                ('region_id', models.TextField()),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
