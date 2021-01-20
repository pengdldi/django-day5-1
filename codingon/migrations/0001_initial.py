# Generated by Django 3.1.5 on 2021-01-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='이름')),
                ('gender', models.CharField(choices=[('M', '남성(M)'), ('W', '여성(W)')], max_length=1, verbose_name='성별')),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
