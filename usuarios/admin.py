from django.contrib import admin
from professores.models import Professor
from usuarios.models import Usuario

admin.site.register([Usuario, Professor])
