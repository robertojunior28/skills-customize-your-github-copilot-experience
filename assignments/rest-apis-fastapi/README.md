# 📘 Assignment: Construindo APIs REST com framework FastAPI

## 🎯 Objective

Aprender a criar APIs RESTful utilizando o framework FastAPI. Os estudantes irão construir uma API simples que permite operações CRUD (Create, Read, Update, Delete) em um recurso de exemplo, como "Tarefas" ou "Usuários".

## 📝 Tasks

### 🛠️ Configuração do Ambiente

#### Description
Configurar o ambiente de desenvolvimento para utilizar o FastAPI e o servidor ASGI Uvicorn.

#### Requirements
Completed program should:

- Instalar o FastAPI e o Uvicorn utilizando o gerenciador de pacotes pip.
- Criar um arquivo principal `main.py` para iniciar o servidor.
- Verificar se o servidor está funcionando acessando a documentação interativa do Swagger em `http://127.0.0.1:8000/docs`.


### 🛠️ Implementação de Endpoints CRUD

#### Description
Criar endpoints para realizar operações CRUD em um recurso de exemplo (e.g., "Tarefas").

#### Requirements
Completed program should:

- Implementar os endpoints `GET`, `POST`, `PUT`, e `DELETE` para o recurso.
- Utilizar um dicionário ou lista como banco de dados em memória.
- Garantir que os endpoints retornem respostas apropriadas (status codes e mensagens).


### 🛠️ Testando a API

#### Description
Testar os endpoints criados utilizando ferramentas como o Swagger UI ou o Postman.

#### Requirements
Completed program should:

- Verificar se todos os endpoints estão funcionando corretamente.
- Corrigir quaisquer erros encontrados durante os testes.
- Documentar os testes realizados no arquivo `README.md`.