# Generated by Django 3.2.8 on 2021-10-20 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('product', '0002_auto_20211020_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_state', models.CharField(max_length=255)),
                ('current_state', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
