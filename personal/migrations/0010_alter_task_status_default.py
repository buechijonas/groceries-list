from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("personal", "0009_alter_shoppinglistitem_unit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.BooleanField(default=False, verbose_name="Status"),
        ),
    ]

