# Generated by Django 3.0.7 on 2020-06-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(related_name='PersonSkills', to='profiles.Skill'),
        ),
    ]
