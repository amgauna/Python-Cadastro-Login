Agora vamos exibir o Hello Word

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello World')
  
# Vamos inserir as funções relativas as rotas acima no arquivo views:
# Formulário de cadastro de usuários

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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

# Na views vamos criar as funções relativas as rotas recém criadas. 
# Essas rotas serão responsáveis pela autenticação e redirecionamento do usuário:
#Formulário do painel de login

def painel(request):
    return render(request,'painel.html')

#Processa o login

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html',data)

#Página inicial do dashboard

def dashboard(request):
    return render(request,'dashboard/home.html')

# Na views, vamos criar as funções relativas as rotas criadas anteriormente:

# Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

# Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password('123456')
    user.save()
    logout(request)
    return redirect('/painel/')

# Permissões e Níveis de Acesso no DJANGO
# O ideal é inserir a permissão do usuário assim que ele for cadastrado no sistema. 
# O Django disponibiliza o método para fazer isso:

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
        user.user_permissions.add(27)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)


