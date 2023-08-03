# Generated by Django 4.2.3 on 2023-08-03 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('room_number', models.IntegerField()),
                ('age', models.PositiveIntegerField(null=True)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=6, null=True)),
                ('reason_adm', models.CharField(max_length=500)),
                ('notes', models.CharField(max_length=1000)),
                ('body_temp', models.IntegerField(null=True)),
                ('pulse_rate', models.IntegerField(null=True)),
                ('respiration_rate', models.IntegerField(null=True)),
                ('systolic', models.IntegerField(null=True)),
                ('diastolic', models.IntegerField(null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
