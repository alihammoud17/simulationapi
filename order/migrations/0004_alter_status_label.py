# Generated by Django 4.1.6 on 2023-02-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_status_label_alter_status_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="status",
            name="label",
            field=models.CharField(
                blank=True, max_length=2, null=True, verbose_name="Status Label"
            ),
        ),
    ]