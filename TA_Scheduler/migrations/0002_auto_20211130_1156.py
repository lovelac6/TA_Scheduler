# Generated by Django 3.2.8 on 2021-11-30 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='accountType',
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountType', models.CharField(choices=[('S', 'Supervisor'), ('I', 'Instructor'), ('T', 'Ta')], default='T', max_length=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_Scheduler.user')),
            ],
        ),
    ]