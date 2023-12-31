# Generated by Django 4.0.2 on 2023-12-26 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_essayquestion_multichoicequestion_shortquestion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essayquestion',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='essayquestion',
            name='required',
        ),
        migrations.RemoveField(
            model_name='shortquestion',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='shortquestion',
            name='required',
        ),
        migrations.CreateModel(
            name='ShortResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.shortquestion')),
            ],
        ),
        migrations.CreateModel(
            name='EssayResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.essayquestion')),
            ],
        ),
    ]
