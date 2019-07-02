# Generated by Django 2.2.2 on 2019-07-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'verbose_name': 'Art'},
        ),
        migrations.AddField(
            model_name='art',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='art',
            name='year',
            field=models.IntegerField(null=True, verbose_name='year'),
        ),
    ]