# 📚 Aprendendo MVC - Node.js vs Django

Este repositório contém dois exemplos práticos de implementação do padrão **MVC (Model-View-Controller)** usando duas tecnologias diferentes:

- **Node.js + Express** (MVC tradicional)
- **Django** (MTV - Model-Template-View)
- **Go** (MVC REST)

## 🎯 Objetivo

Demonstrar como o mesmo conceito arquitetural pode ser implementado de formas diferentes, ajudando a entender:

- As diferenças entre as abordagens
- Vantagens e desvantagens de cada tecnologia
- Conceitos fundamentais do MVC
- Boas práticas de desenvolvimento web

## 📁 Estrutura dos Projetos


```
estudos/nodejs/
├── nodejs-mvc/          # Projeto Node.js + Express
│   ├── models/          # Camada Model
│   ├── views/           # Templates EJS
│   ├── controllers/     # Lógica da aplicação
│   ├── routes/          # Definição de rotas
│   └── app.js           # Arquivo principal
│
├── django-mvc/          # Projeto Django
│   ├── users/           # App Django
│   │   ├── models.py    # Models Django
│   │   ├── views.py     # Views (Controllers)
│   │   ├── templates/   # Templates Django
│   │   └── urls.py      # URLs do app
│   └── userproject/     # Configurações Django
│
└── go-mvc/              # Projeto Go (MVC REST)
    ├── main.go          # Entrypoint
    ├── models/          # Structs de domínio
    ├── controllers/     # Handlers HTTP
    ├── services/        # Lógica de negócio
    ├── repository/      # Simula acesso a dados
    ├── routes/          # Roteamento
    └── README.md        # Instruções Go
```

## 🚀 Como Executar

### Node.js MVC
```bash
cd nodejs-mvc
npm install
npm run dev
# Acesse: http://localhost:3000
```

### Django MTV
```bash
cd django-mvc
source venv/bin/activate
python manage.py runserver
# Acesse: http://127.0.0.1:8000
```

### Go MVC
```bash
cd go-mvc
go mod tidy
go run main.go
# Acesse: http://localhost:8080
```

Principais rotas Go:
- `GET    /users`         → Lista usuários
- `GET    /users/{id}`    → Detalhe usuário
- `POST   /users`         → Cria usuário (JSON)
- `PUT    /users/{id}`    → Atualiza usuário (JSON)
- `DELETE /users/{id}`    → Remove usuário

## 🔍 Comparação Detalhada

| Aspecto | Node.js + Express | Django | Go |
|---------|-------------------|--------|----|
| **Padrão** | MVC (Model-View-Controller) | MTV (Model-Template-View) | MVC REST |
| **Linguagem** | JavaScript | Python | Go |
| **Flexibilidade** | Muito alta - escolha suas libs | Estrutura mais rígida | Estrutura livre |
| **Curva de Aprendizado** | Moderada | Íngreme no início | Baixa/moderada |
| **Admin Interface** | Precisa criar | Automática | Manual |
| **ORM** | Escolha (Sequelize, etc.) | Django ORM built-in | Manual ou GORM |
| **Templates** | Escolha (EJS, Handlebars) | Django Template Language | html/template (opcional) |
| **Scaffolding** | Manual | Comandos automáticos | Manual |
| **Ecosystem** | NPM (muito vasto) | PyPI (focado) | Go Modules |

## 📊 Fluxo de Funcionamento

### Node.js MVC
```
Request → Route → Controller → Model → Controller → View → Response
```

### Django MTV
```
Request → URL → View → Model → View → Template → Response
```

### Go MVC
```
Request → Route → Controller → Service → Repository → Model → Controller → Response
```

## 💡 Conceitos Aprendidos

### Ambos os Projetos:
- ✅ Separação de responsabilidades
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Roteamento
- ✅ Templates dinâmicos
- ✅ Validação de formulários
- ✅ Tratamento de erros

### Específicos do Node.js:
- ✅ Express.js middleware
- ✅ EJS templates
- ✅ Estruturação manual de projeto
- ✅ NPM package management

### Específicos do Django:
- ✅ Django ORM
- ✅ Migrações automáticas
- ✅ Admin interface
- ✅ Django Template Language
- ✅ Apps modulares
- ✅ Proteção CSRF automática

## 🎓 Qual Escolher?

### Choose Node.js quando:
- Você prefere JavaScript
- Quer máxima flexibilidade
- Projeto necessita alta performance
- Equipe já conhece JavaScript
- Quer construir APIs REST/GraphQL

### Choose Django quando:
- Você prefere Python
- Quer desenvolvimento rápido
- Precisa de admin interface
- Projeto tem muitas regras de negócio
- Segurança é prioridade

## 📚 Próximos Passos

Depois de entender estes exemplos, você pode:

1. **Adicionar banco de dados real** (PostgreSQL, MySQL, SQLite)
2. **Implementar autenticação** de usuários
3. **Criar APIs REST** para mobile
4. **Adicionar testes** automatizados
5. **Deploy em produção** (Heroku, AWS, etc.)
6. **Implementar cache** (Redis)
7. **Adicionar WebSockets** para tempo real
8. **Adicionar templates HTML no Go**

## 🔗 Recursos Úteis

### Node.js + Express:
- [Express.js Official Docs](https://expressjs.com/)
- [EJS Template Engine](https://ejs.co/)
- [Sequelize ORM](https://sequelize.org/)

### Django:
- [Django Official Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)

---

💡 **Dica Final**: Não existe tecnologia "melhor" - existe a tecnologia mais adequada para cada projeto e equipe. Este repositório te ajuda a entender as diferenças para fazer uma escolha informada!