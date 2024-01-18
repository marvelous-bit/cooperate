# Generated by Django 4.2.4 on 2023-08-21 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10055)),
                ('subject', models.CharField(max_length=3066)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('messagess', models.TextField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('photo', models.ImageField(upload_to='image/')),
                ('image', models.ImageField(upload_to='imagerr/')),
                ('author', models.CharField(max_length=9887)),
                ('mblockquote', models.TextField()),
                ('intro', models.CharField(max_length=9887)),
                ('Body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='teamdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('point', models.CharField(max_length=100)),
                ('twitter', models.URLField()),
                ('fbook', models.URLField()),
                ('insta', models.URLField()),
                ('linkden', models.URLField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='testimonyp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]