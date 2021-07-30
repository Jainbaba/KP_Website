# Generated by Django 3.2.5 on 2021-07-26 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KP_Form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personFamily',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KP_Form.familydetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='marudharMe',
            field=models.CharField(choices=[('Sojat Road', 'Sojat Road')], max_length=256),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='residenceArea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='KP_Form.area'),
        ),
    ]
