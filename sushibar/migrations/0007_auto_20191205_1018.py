# Generated by Django 2.2.7 on 2019-12-05 15:18

from django.db import migrations, models
import sushibar.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sushibar', '0006_auto_20191205_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('correo', models.EmailField(max_length=256)),
                ('asunto', models.CharField(max_length=128)),
                ('mensaje', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='postulante',
            name='cv',
            field=models.FileField(upload_to='cv/', validators=[sushibar.validators.validate_file_size]),
        ),
    ]
