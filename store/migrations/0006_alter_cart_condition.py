# Generated by Django 4.2.6 on 2023-10-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_cart_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='condition',
            field=models.CharField(choices=[('ND', 'NOTDELIVERED'), ('D', 'DELIVERED'), ('OP', 'ONPROGRESS'), ('C', 'CANCLLED')], default='ND', max_length=2),
        ),
    ]
