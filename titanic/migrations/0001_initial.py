# Generated by Django 5.0.6 on 2024-06-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pclass', models.IntegerField()),
                ('Age', models.FloatField()),
                ('SibSp', models.IntegerField()),
                ('Parch', models.IntegerField()),
                ('Fare', models.FloatField()),
                ('Sex_male', models.IntegerField()),
                ('Embarked_Q', models.IntegerField()),
                ('Embarked_S', models.IntegerField()),
                ('prediction', models.CharField(max_length=20)),
                ('probability', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
