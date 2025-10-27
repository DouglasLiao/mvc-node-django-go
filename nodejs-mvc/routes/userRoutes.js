const express = require('express');
const UserController = require('../controllers/userController');

const router = express.Router();

// Rotas para usuários
router.get('/users', UserController.getAllUsers);
router.get('/users/create', UserController.showCreateForm);
router.post('/users', UserController.createUser);
router.get('/users/:id', UserController.getUserById);
router.get('/users/:id/edit', UserController.showEditForm);
router.post('/users/:id/update', UserController.updateUser);
router.post('/users/:id/delete', UserController.deleteUser);

module.exports = router;