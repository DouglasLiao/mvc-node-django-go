# Go MVC Example

Este projeto demonstra uma estrutura MVC simples em Go, similar ao exemplo Node.js/Django.

## Estrutura

- `main.go`: Entrypoint da aplicação
- `models/`: Structs de domínio (User)
- `repository/`: Simula acesso a dados (CRUD em memória)
- `services/`: Lógica de negócio
- `controllers/`: Handlers HTTP
- `routes/`: Roteamento

## Como rodar

1. Instale as dependências:
   ```sh
   cd go-mvc
   go mod tidy
   ```
2. Execute o servidor:
   ```sh
   go run main.go
   ```
3. Teste as rotas:
   - `GET    /users`         → Lista usuários
   - `GET    /users/{id}`    → Detalhe usuário
   - `POST   /users`         → Cria usuário (JSON)
   - `PUT    /users/{id}`    → Atualiza usuário (JSON)
   - `DELETE /users/{id}`    → Remove usuário

## Observações
- O projeto usa [gorilla/mux](https://github.com/gorilla/mux) para roteamento.
- Os dados são mantidos em memória (não persistem após reiniciar).
- Estrutura pronta para adicionar views/templates se desejar.
