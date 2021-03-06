# Generated by Django 4.0.6 on 2022-07-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('thecurrency', models.CharField(choices=[('NGN', 'NGN'), ('USD', 'USD'), ('EUR', 'EUR')], max_length=255)),
                ('theduration', models.CharField(choices=[('DAILY', 'DAILY'), ('WEEKLY', 'WEEKLY'), ('MONTHLY', 'MONTHLY'), ('YEARLY', 'YEARLY')], max_length=255)),
                ('category', models.CharField(choices=[('FOOD', 'FOOD'), ('SHOPPING', 'SHOPPING'), ('HEALTH', 'HEALTH'), ('BOOKS', 'BOOKS'), ('OTHERS', 'OTHERS')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
