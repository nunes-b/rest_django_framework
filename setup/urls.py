from django.contrib import admin
from django.urls import path
from escola.views import get_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', get_student, name='alunos',)
]
