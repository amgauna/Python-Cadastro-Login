# Vamos criar uma url de Hello World para testar se o django realmente já está ativo:

from django.contrib import admin
from django.urls import path
from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

# cadastro utilizando Python e Django. 
# Vamos aprender desde o formulário html até a inserção no banco.
# Cadastro de Dados no banco com Python
# Para trabalhar com cadastro vamos criar duas rotas:

path('create/', create),
path('store/', store),

