# 🐍 MVC com Django - Exemplo Didático

Este é um exemplo prático de como implementar a arquitetura **Model-Template-View (MTV)** usando Django, que é a versão do MVC específica do Django.

## 📁 Estrutura do Projeto

```
django-mvc/
├── venv/                        # Ambiente virtual Python
├── userproject/                 # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py              # Configurações do Django
│   ├── urls.py                  # URLs principais
│   ├── wsgi.py                  # Interface WSGI
│   └── asgi.py                  # Interface ASGI
├── users/                       # App Django para usuários
│   ├── migrations/              # Migrações do banco de dados
│   ├── templates/users/         # Templates (Views do MVC)
│   │   ├── base.html            # Template base
│   │   ├── home.html            # Página inicial
│   │   ├── user_list.html       # Lista de usuários
│   │   ├── user_detail.html     # Detalhes do usuário
│   │   ├── user_form.html       # Formulário de usuário
│   │   └── user_confirm_delete.html # Confirmação de exclusão
│   ├── __init__.py
│   ├── admin.py                 # Interface de administração
│   ├── apps.py                  # Configurações do app
│   ├── models.py                # Models (M do MTV)
│   ├── tests.py                 # Testes
│   ├── urls.py                  # URLs do app
│   └── views.py                 # Views (V do MTV = Controller do MVC)
├── manage.py                    # Utilitário de linha de comando
└── requirements.txt             # Dependências Python
```

## 🏗️ Arquitetura MTV (Django's MVC)

### 📊 Model (Modelo)
- **Arquivo**: `users/models.py`
- **Responsabilidade**: Definir estrutura de dados e regras de negócio
- **O que faz**: Classes Python que representam tabelas do banco de dados

### 📄 Template (Template)
- **Arquivos**: `users/templates/users/*.html`
- **Responsabilidade**: Apresentação/Interface do usuário
- **O que faz**: HTML dinâmico usando Django Template Language

### 🎮 View (Visão)
- **Arquivo**: `users/views.py`
- **Responsabilidade**: Lógica da aplicação (Controller no MVC tradicional)
- **O que faz**: Funções Python que processam requisições e retornam respostas

## 🚀 Como Executar

### 1. Ativar ambiente virtual
```bash
cd django-mvc
source venv/bin/activate
```

### 2. Instalar dependências (se necessário)
```bash
pip install django
```

### 3. Fazer migrações do banco
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 5. Executar o servidor
```bash
python manage.py runserver
```

### 6. Acessar no navegador
```
http://127.0.0.1:8000/
```

### 7. Acessar admin (opcional)
```
http://127.0.0.1:8000/admin/
```

## 🔄 Fluxo MTV vs MVC

### Django MTV:
1. **URL** → Requisição chega no Django
2. **View** → Função Python processa (= Controller)
3. **Model** → Interage com banco de dados
4. **Template** → Renderiza HTML (= View)
5. **Response** → Retorna para o usuário

### Node.js MVC Tradicional:
1. **Route** → Requisição chega no Express
2. **Controller** → Processa a requisição
3. **Model** → Interage com dados
4. **View** → Renderiza HTML
5. **Response** → Retorna para o usuário

## 📋 Funcionalidades

- ✅ Listar usuários
- ✅ Criar novo usuário
- ✅ Ver detalhes de usuário
- ✅ Editar usuário
- ✅ Deletar usuário (com confirmação)
- ✅ Interface de administração automática
- ✅ Validação de formulários
- ✅ Proteção CSRF
- ✅ Timestamps automáticos
- ✅ Interface responsiva com Bootstrap

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **Django**: Framework web
- **SQLite**: Banco de dados (padrão do Django)
- **Django Template Language**: Sistema de templates
- **Bootstrap**: Framework CSS
- **Django Admin**: Interface de administração

## 📚 Conceitos Django Aprendidos

- Models e ORM do Django
- Views baseadas em funções
- Sistema de templates do Django
- URLs e roteamento
- Django Admin
- Migrações de banco
- Proteção CSRF
- Mensagens do sistema
- Estruturação de apps Django

## 🔍 Principais Diferenças Django vs Node.js

| Aspecto | Django (Python) | Node.js (Express) |
|---------|----------------|-------------------|
| **Padrão** | MTV (Model-Template-View) | MVC (Model-View-Controller) |
| **Linguagem** | Python | JavaScript |
| **Templates** | Django Template Language | EJS, Handlebars, etc. |
| **ORM** | Django ORM (built-in) | Sequelize, Mongoose, etc. |
| **Admin** | Interface automática | Precisa criar manualmente |
| **Banco** | SQLite/PostgreSQL/MySQL | Qualquer (mais flexível) |
| **Estrutura** | Apps organizados | Estrutura livre |

## 🎯 Vantagens do Django

1. **Batteries Included**: Vem com muita coisa pronta
2. **Admin Interface**: Interface de administração automática
3. **ORM Poderoso**: Sistema de banco de dados integrado
4. **Segurança**: Proteções built-in (CSRF, SQL Injection, etc.)
5. **Scaffold Rápido**: Desenvolvimento rápido de protótipos

## 🚀 Próximos Passos

Para expandir este projeto:

1. Adicionar autenticação de usuários
2. Implementar API REST com Django REST Framework
3. Adicionar paginação na lista de usuários
4. Implementar upload de imagens
5. Criar relacionamentos entre models
6. Adicionar testes automatizados
7. Deploy em produção

---

💡 **Nota**: Este projeto demonstra as diferenças práticas entre Django MTV e Node.js MVC, mostrando como o mesmo conceito pode ser implementado de formas diferentes!