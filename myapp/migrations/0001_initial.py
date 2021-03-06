# Generated by Django 2.0.7 on 2018-07-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('web', 'web'), ('pwn', 'pwn'), ('Forensics', 'Forensics'), ('Cryptography', 'Cryptography'), ('misc', 'misc')], max_length=20)),
                ('point', models.IntegerField()),
                ('description', models.TextField()),
                ('attachment', models.FileField(blank='true', upload_to='admin')),
            ],
        ),
    ]
