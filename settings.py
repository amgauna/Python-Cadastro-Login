# Entendendo o Django
# O Django é um framework de Python e como tal traz as seguintes vantagens:
# - Eficiência
# - Apoio Técnico
# - Segurança
# - Integração
# - Usabilidade

# O Django utiliza a arquitetura de software MVT (Model - View - Template):
# Para configurar o banco de dados primeiramente vamos adicionar o app e depois inserir os dados do banco:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=InnoDB'
        }
    }
}

# Para que o diretório static funcione corretamente precisamos configurá-lo 
# no arquivo de configurações adicionando a seguinte linha:

STATICFILES_DIR = ('/static/')


