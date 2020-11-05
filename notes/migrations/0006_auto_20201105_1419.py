# Generated by Django 3.1.1 on 2020-11-05 11:19

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20201025_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='note',
            name='state',
            field=django_fsm.FSMField(default='draft', max_length=50, protected=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='note',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Low'), (2, 'Middle'), (3, 'Above the average'), (4, 'High'), (5, 'Highest')]),
        ),
    ]
