# Generated by Django 4.1.2 on 2023-01-25 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complete_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('decription', models.TextField()),
                ('category', models.CharField(choices=[(None, 'select gender'), ('outdoor', 'outdoor'), ('indoor', 'indor')], default=None, max_length=12)),
                ('Create_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register')),
            ],
        ),
    ]
