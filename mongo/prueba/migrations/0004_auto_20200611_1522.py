# Generated by Django 2.2.13 on 2020-06-11 15:22

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0003_remove_entry_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default='666f6f2d6261722d71757578', primary_key=True, serialize=False),
        ),
    ]
