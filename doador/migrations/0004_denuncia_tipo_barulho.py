# Generated by Django 5.0 on 2024-10-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doador', '0003_denuncia_alter_doador_email_alter_doador_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='tipo_barulho',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]