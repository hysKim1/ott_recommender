# Generated by Django 4.0 on 2022-01-08 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entertainment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyOTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ott', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entertainment.ott')),
            ],
        ),
    ]
