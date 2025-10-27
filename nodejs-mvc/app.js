const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

// Importar rotas
const userRoutes = require('./routes/userRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// Configurar view engine (EJS)
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// Rotas
app.use('/', userRoutes);

// Rota inicial
app.get('/', (req, res) => {
    res.render('index', { 
        title: 'MVC com Node.js',
        message: 'Bem-vindo ao exemplo MVC!'
    });
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`🚀 Servidor rodando na porta ${PORT}`);
    console.log(`📱 Acesse: http://localhost:${PORT}`);
});

module.exports = app;