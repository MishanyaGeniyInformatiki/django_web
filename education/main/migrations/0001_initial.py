# Generated by Django 4.2.13 on 2024-05-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('question_text', models.TextField(blank=True)),
                ('correct_answer', models.FloatField()),
                ('user_answer', models.FloatField(blank=True, default=None)),
            ],
        ),
    ]