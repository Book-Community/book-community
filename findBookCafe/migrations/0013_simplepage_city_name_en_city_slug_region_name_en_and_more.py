# Generated by Django 4.0.6 on 2022-12-11 11:05

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0012_remove_shop_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500, unique=True)),
                ('content', django_quill.fields.QuillField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='name_en',
            field=models.CharField(default=models.CharField(max_length=200, primary_key=True, serialize=False), max_length=200),
        ),
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.CharField(default=models.CharField(default=models.CharField(max_length=200, primary_key=True, serialize=False), max_length=200), max_length=200),
        ),
        migrations.AddField(
            model_name='region',
            name='name_en',
            field=models.CharField(default=models.CharField(max_length=200, primary_key=True, serialize=False), max_length=200),
        ),
        migrations.AddField(
            model_name='region',
            name='slug',
            field=models.CharField(default=models.CharField(default=models.CharField(max_length=200, primary_key=True, serialize=False), max_length=200), max_length=200),
        ),
        migrations.AddField(
            model_name='shop',
            name='isAccessibleForPeopleWithDisabilities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shop',
            name='name_en',
            field=models.CharField(default=models.CharField(max_length=300), max_length=300),
        ),
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.CharField(default=models.CharField(default=models.CharField(max_length=300), max_length=300), max_length=300),
        ),
    ]
