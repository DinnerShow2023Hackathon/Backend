# Generated by Django 4.0.4 on 2023-04-29 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('phonenum', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Bookpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='dinner')),
                ('whos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dinner.user')),
            ],
        ),
    ]
