# Generated by Django 4.0.3 on 2022-04-11 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_alter_course_outcome_alter_course_requirements'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-id']},
        ),
    ]
