Agora vamos exibir o Hello Word

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello World')
  
# Vamos inserir as funções relativas as rotas acima no arquivo views:
# Formulário de cadastro de usuários

def create(request):
    return render(request,'create.html')


#Inserção dos dados dos usuários no banco

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)

