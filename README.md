# CRUD_LEAP - Sistema de Gerenciamento de Posts
## Descrição
Este é um projeto simples de CRUD (Create, Read, Update, Delete).

## Funcionalidades
- Criar novos posts
- Visualizar lista de posts
- Atualizar posts existentes
- Deletar posts
- Ordenação automática por data de criação (mais recentes primeiro)

## 📋 Estrutura do Post
Cada post contém:

- Username (autor)
- Título
- Conteúdo
- Data de criação (gerada automaticamente)

### Passos para Execução
1. Clone o repositório ou baixe os arquivos
2. Crie e ative um ambiente virtual
3. Instale as dependências
4. Execute as migrações
5. Inicie o servidor

6. Comandos de Endpoints
- GET /careers/ - Lista todos os posts
- POST /careers/ - Cria um novo post
- GET /careers/{id}/ - Obtém detalhes de um post específico
- PUT /careers/{id}/ - Atualiza um post existente
- DELETE /careers/{id}/ - Remove um post
