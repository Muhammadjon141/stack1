# Generated by Django 5.0.6 on 2024-07-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_center', '0005_user_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
