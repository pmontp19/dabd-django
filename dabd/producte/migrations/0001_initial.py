# Generated by Django 2.0.4 on 2018-04-18 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('list_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('salable', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='productproduct',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producte.ProductTemplate'),
        ),
    ]
