# Generated by Django 5.0.4 on 2024-09-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personal", "0007_alter_shoppinglistitem_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.BooleanField(default="false", verbose_name="Status"),
        ),
    ]