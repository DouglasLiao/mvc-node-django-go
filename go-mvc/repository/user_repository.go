package repository

import (
	"go-mvc/models"
)

var users = []models.User{
	{ID: 1, Name: "João Silva", Email: "joao@email.com", Age: 25},
	{ID: 2, Name: "Maria Santos", Email: "maria@email.com", Age: 30},
	{ID: 3, Name: "Pedro Oliveira", Email: "pedro@email.com", Age: 28},
}

func GetAllUsers() []models.User {
	return users
}

func GetUserByID(id int) *models.User {
	for _, u := range users {
		if u.ID == id {
			return &u
		}
	}
	return nil
}

func CreateUser(user models.User) models.User {
	user.ID = users[len(users)-1].ID + 1
	users = append(users, user)
	return user
}

func UpdateUser(id int, user models.User) *models.User {
	for i, u := range users {
		if u.ID == id {
			users[i].Name = user.Name
			users[i].Email = user.Email
			users[i].Age = user.Age
			return &users[i]
		}
	}
	return nil
}

func DeleteUser(id int) bool {
	for i, u := range users {
		if u.ID == id {
			users = append(users[:i], users[i+1:]...)
			return true
		}
	}
	return false
}
