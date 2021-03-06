# Generated by Django 2.2.13 on 2020-06-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0006_auto_20200611_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
