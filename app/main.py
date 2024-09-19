from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema

# Inicialize o FastAPI
app = FastAPI()

# Crie a rota GraphQL
graphql_app = GraphQLRouter(schema)

# Adicione a rota ao FastAPI
app.include_router(graphql_app, prefix="/graphql")

# Rota simples para testar se a API está no ar
@app.get("/")
def read_root():
    return {"message": "API de Predição com GraphQL e FastAPI está funcionando!"}
