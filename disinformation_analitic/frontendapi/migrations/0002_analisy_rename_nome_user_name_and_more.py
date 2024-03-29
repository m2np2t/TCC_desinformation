# Generated by Django 4.0.3 on 2022-08-20 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analisy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='disinformation',
            name='auto_increment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
