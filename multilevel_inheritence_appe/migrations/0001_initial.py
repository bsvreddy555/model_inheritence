# Generated by Django 3.2 on 2021-04-23 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multilevel_inheritence_appe.employee')),
                ('cust_name', models.CharField(max_length=50)),
                ('sales', models.FloatField()),
            ],
            bases=('multilevel_inheritence_appe.employee',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multilevel_inheritence_appe.customer')),
                ('stu_name', models.CharField(max_length=50)),
                ('marks', models.FloatField()),
            ],
            bases=('multilevel_inheritence_appe.customer',),
        ),
    ]
