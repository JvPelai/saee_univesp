from django.shortcuts import render
from agendamentos.forms import AgendamentoForm

# Create your views here.


def registrar_agendamento(request):

    form = AgendamentoForm()

    context = {
        "nome_pagina": "Registrar agendamento",
        "form": form,
    }
    return render(request, "registrar_agendamento.html", context)
