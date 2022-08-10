# Generated by Django 4.1 on 2022-08-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_grooming'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='grooming',
            name='date',
            field=models.DateField(verbose_name='grooming date'),
        ),
        migrations.AddField(
            model_name='canine',
            name='tricks',
            field=models.ManyToManyField(to='main_app.trick'),
        ),
    ]
