# main.py
from fastapi import FastAPI
from app.controllers import api_controller
from strawberry.fastapi import GraphQLRouter
from app.schema.schema import schema

# Instância do FastAPI
app = FastAPI()

# Registrando as rotas da API REST
app.include_router(api_controller.router, prefix="/api")

# Registrando o GraphQL Router
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Rota de verificação do serviço
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Previsão de Resultados de Partidas!"}
