from django.db import models

# Create your models here.


class Agendamento(models.Model):
    sala = models.PositiveSmallIntegerField(
        verbose_name="Número da sala",
    )
    horario_inicio = models.DateTimeField(
        verbose_name="Horário inicial do agendamento",
        auto_now_add=False,
        blank=False,
    )

    horario_fim = models.DateTimeField(
        verbose_name="Horário do fim do tempo de uso",
        auto_now_add=False,
        blank=False,
    )

    responsavel = models.ForeignKey(
        "usuarios.Usuario",
        verbose_name="Responsavel pelo agendamento",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        db_table = "agendamento"

        def __str__(self):
            return str(self.sala)
