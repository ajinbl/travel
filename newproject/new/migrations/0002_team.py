# Generated by Django 3.2.15 on 2022-08-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=250)),
                ('imge', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
