package main

import (
	"go-mvc/routes"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()
	routes.RegisterUserRoutes(r)

	log.Println("🚀 Servidor Go rodando em http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", r))
}
