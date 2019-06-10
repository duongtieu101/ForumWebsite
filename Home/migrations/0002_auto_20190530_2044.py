# Generated by Django 2.2.1 on 2019-05-30 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='thread',
            name='Content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AddField(
            model_name='board',
            name='Topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Home.Topic'),
            preserve_default=False,
        ),
    ]
