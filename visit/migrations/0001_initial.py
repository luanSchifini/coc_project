# Generated by Django 4.2.4 on 2024-12-18 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.IntegerField(null=True)),
                ('student_name', models.CharField(max_length=50)),
                ('anosemestre', models.IntegerField(null=True)),
                ('student_class', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('evaluation', models.IntegerField(null=True)),
                ('student_visited', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_visits', to='visit.student')),
            ],
        ),
    ]
