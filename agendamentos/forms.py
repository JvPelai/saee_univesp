from django import forms
from agendamentos.models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = "__all__"
