package services

import (
	"go-mvc/models"
	"go-mvc/repository"
)

func GetAllUsers() []models.User {
	return repository.GetAllUsers()
}

func GetUserByID(id int) *models.User {
	return repository.GetUserByID(id)
}

func CreateUser(user models.User) models.User {
	return repository.CreateUser(user)
}

func UpdateUser(id int, user models.User) *models.User {
	return repository.UpdateUser(id, user)
}

func DeleteUser(id int) bool {
	return repository.DeleteUser(id)
}
