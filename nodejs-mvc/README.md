# 🚀 MVC com Node.js - Exemplo Didático

Este é um exemplo prático de como implementar a arquitetura **Model-View-Controller (MVC)** usando Node.js, Express e EJS.

## 📁 Estrutura do Projeto

```
nodejs-mvc/
├── models/
│   └── User.js              # Model - Gerencia dados dos usuários
├── views/
│   ├── users/
│   │   ├── index.ejs        # Lista todos os usuários
│   │   ├── create.ejs       # Formulário para criar usuário
│   │   ├── show.ejs         # Exibe detalhes de um usuário
│   │   └── edit.ejs         # Formulário para editar usuário
│   ├── index.ejs            # Página inicial
│   ├── layout.ejs           # Layout base
│   └── error.ejs            # Página de erro
├── controllers/
│   └── userController.js    # Controller - Lógica da aplicação
├── routes/
│   └── userRoutes.js        # Rotas da aplicação
├── public/                  # Arquivos estáticos (CSS, JS, imagens)
├── app.js                   # Arquivo principal da aplicação
└── package.json             # Dependências e scripts
```

## 🏗️ Arquitetura MVC

### 📊 Model (Modelo)
- **Arquivo**: `models/User.js`
- **Responsabilidade**: Gerenciar dados e lógica de negócio
- **O que faz**: Define a estrutura dos dados de usuário e métodos para CRUD

### 👁️ View (Visão)
- **Arquivos**: `views/*.ejs`
- **Responsabilidade**: Interface do usuário
- **O que faz**: Renderiza HTML dinâmico usando EJS templates

### 🎮 Controller (Controlador)
- **Arquivo**: `controllers/userController.js`
- **Responsabilidade**: Lógica da aplicação
- **O que faz**: Processa requisições, usa Models e renderiza Views

## 🚀 Como Executar

### 1. Instalar dependências
```bash
cd nodejs-mvc
npm install
```

### 2. Executar a aplicação
```bash
# Modo desenvolvimento (com nodemon)
npm run dev

# Ou modo produção
npm start
```

### 3. Acessar no navegador
```
http://localhost:3000
```

## 🔄 Fluxo de Funcionamento

1. **Usuário faz uma requisição** → Express recebe via rotas
2. **Rota chama o Controller** → UserController processa a requisição
3. **Controller usa o Model** → Busca/modifica dados no User
4. **Controller renderiza a View** → EJS gera HTML com os dados
5. **Response é enviada** → Usuário vê o resultado

## 📋 Funcionalidades

- ✅ Listar usuários
- ✅ Criar novo usuário
- ✅ Ver detalhes de usuário
- ✅ Editar usuário
- ✅ Deletar usuário
- ✅ Interface responsiva com Bootstrap
- ✅ Validação de formulários
- ✅ Tratamento de erros

## 🛠️ Tecnologias Utilizadas

- **Node.js**: Runtime JavaScript
- **Express**: Framework web
- **EJS**: Template engine
- **Bootstrap**: Framework CSS
- **Body-parser**: Middleware para parsing de dados

## 📚 Conceitos Aprendidos

- Arquitetura MVC
- Roteamento com Express
- Templates com EJS
- Middlewares
- CRUD operations
- Estruturação de projetos Node.js

## 🎯 Próximos Passos

Para expandir este projeto, você pode:

1. Adicionar banco de dados (MongoDB, PostgreSQL)
2. Implementar autenticação
3. Adicionar validações mais robustas
4. Criar API REST
5. Adicionar testes unitários
6. Implementar upload de arquivos

---

💡 **Dica**: Este é um exemplo didático. Em projetos reais, considere usar ORMs como Sequelize ou Mongoose para gerenciar dados.