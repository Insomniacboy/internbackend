# Generated by Django 4.0.3 on 2022-03-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_about', '0003_info_title_en_info_title_kg_info_title_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='title_text_en',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='title_text_kg',
            new_name='desc_en',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='title_text_ru',
            new_name='desc_kg',
        ),
        migrations.AddField(
            model_name='info',
            name='desc_ru',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='facebook',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='gallery_id',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='instagram',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='latitude',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='longitude',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='phone',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='zoom',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
