# Generated by Django 3.1.2 on 2021-04-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_handsetorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilenumber',
            name='call_mins',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mobilenumber',
            name='data_usage_3m',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mobilenumber',
            name='mms_sent',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mobilenumber',
            name='texts_sent_3m',
            field=models.IntegerField(null=True),
        ),
    ]
