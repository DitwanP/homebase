# Generated by Django 3.1.1 on 2020-09-09 20:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0005_auto_20200909_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]