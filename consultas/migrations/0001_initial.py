# Generated by Django 3.1.3 on 2023-06-15 22:33

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
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), 
                ('fecha', models.TextField(default='')),             
                ('modelo', models.TextField(default='')),
                ('prompt', models.TextField(default='')),
                ('result', models.TextField(default='')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
