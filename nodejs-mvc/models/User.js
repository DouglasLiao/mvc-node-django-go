class User {
    constructor(id, name, email, age) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.age = age;
    }

    // Simulando um banco de dados em memória
    static users = [
        new User(1, 'João Silva', 'joao@email.com', 25),
        new User(2, 'Maria Santos', 'maria@email.com', 30),
        new User(3, 'Pedro Oliveira', 'pedro@email.com', 28)
    ];

    // Buscar todos os usuários
    static findAll() {
        return this.users;
    }

    // Buscar usuário por ID
    static findById(id) {
        return this.users.find(user => user.id === parseInt(id));
    }

    // Criar novo usuário
    static create(userData) {
        const newId = Math.max(...this.users.map(u => u.id)) + 1;
        const newUser = new User(newId, userData.name, userData.email, parseInt(userData.age));
        this.users.push(newUser);
        return newUser;
    }

    // Atualizar usuário
    static update(id, userData) {
        const userIndex = this.users.findIndex(user => user.id === parseInt(id));
        if (userIndex !== -1) {
            this.users[userIndex] = { ...this.users[userIndex], ...userData };
            return this.users[userIndex];
        }
        return null;
    }

    // Deletar usuário
    static delete(id) {
        const userIndex = this.users.findIndex(user => user.id === parseInt(id));
        if (userIndex !== -1) {
            return this.users.splice(userIndex, 1)[0];
        }
        return null;
    }
}

module.exports = User;