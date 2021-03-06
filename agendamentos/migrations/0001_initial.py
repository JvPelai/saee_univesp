# Generated by Django 3.2.7 on 2021-10-07 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.PositiveSmallIntegerField(verbose_name='Número da sala')),
                ('horario_inicio', models.DateTimeField(verbose_name='Horário inicial do agendamento')),
                ('horario_fim', models.DateTimeField(verbose_name='Horário do fim do tempo de uso')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Responsavel pelo agendamento')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
                'db_table': 'agendamento',
            },
        ),
    ]
