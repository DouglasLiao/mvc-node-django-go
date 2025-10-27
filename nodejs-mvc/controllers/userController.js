const User = require('../models/User');

class UserController {
    // Listar todos os usuários
    static getAllUsers(req, res) {
        try {
            const users = User.findAll();
            res.render('users/index', { 
                title: 'Lista de Usuários',
                users: users 
            });
        } catch (error) {
            res.status(500).json({ error: 'Erro ao buscar usuários' });
        }
    }

    // Mostrar formulário de criação
    static showCreateForm(req, res) {
        res.render('users/create', { 
            title: 'Criar Novo Usuário' 
        });
    }

    // Criar novo usuário
    static createUser(req, res) {
        try {
            const { name, email, age } = req.body;
            
            if (!name || !email || !age) {
                return res.status(400).render('users/create', { 
                    title: 'Criar Novo Usuário',
                    error: 'Todos os campos são obrigatórios' 
                });
            }

            const newUser = User.create({ name, email, age });
            res.redirect('/users');
        } catch (error) {
            res.status(500).render('users/create', { 
                title: 'Criar Novo Usuário',
                error: 'Erro ao criar usuário' 
            });
        }
    }

    // Mostrar usuário específico
    static getUserById(req, res) {
        try {
            const user = User.findById(req.params.id);
            if (!user) {
                return res.status(404).render('error', { 
                    title: 'Usuário não encontrado',
                    message: 'Usuário não encontrado' 
                });
            }
            res.render('users/show', { 
                title: `Usuário: ${user.name}`,
                user: user 
            });
        } catch (error) {
            res.status(500).json({ error: 'Erro ao buscar usuário' });
        }
    }

    // Mostrar formulário de edição
    static showEditForm(req, res) {
        try {
            const user = User.findById(req.params.id);
            if (!user) {
                return res.status(404).render('error', { 
                    title: 'Usuário não encontrado',
                    message: 'Usuário não encontrado' 
                });
            }
            res.render('users/edit', { 
                title: `Editar: ${user.name}`,
                user: user 
            });
        } catch (error) {
            res.status(500).json({ error: 'Erro ao buscar usuário' });
        }
    }

    // Atualizar usuário
    static updateUser(req, res) {
        try {
            const { name, email, age } = req.body;
            const updatedUser = User.update(req.params.id, { name, email, age });
            
            if (!updatedUser) {
                return res.status(404).render('error', { 
                    title: 'Usuário não encontrado',
                    message: 'Usuário não encontrado' 
                });
            }
            
            res.redirect('/users');
        } catch (error) {
            res.status(500).json({ error: 'Erro ao atualizar usuário' });
        }
    }

    // Deletar usuário
    static deleteUser(req, res) {
        try {
            const deletedUser = User.delete(req.params.id);
            if (!deletedUser) {
                return res.status(404).json({ error: 'Usuário não encontrado' });
            }
            res.redirect('/users');
        } catch (error) {
            res.status(500).json({ error: 'Erro ao deletar usuário' });
        }
    }
}

module.exports = UserController;