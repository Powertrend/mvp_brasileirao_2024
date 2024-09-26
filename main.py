"""Backend GraphQl com Algoritimo de Machine LEarning Embarcado

Params: Mandante, Visitante, PosMandante, PosVisitante
Returns:
    _type_: Vitoria_Mandante, Vitoria_Visitante, Empate
"""

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.controllers import api_controller
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
    """Rota Proncipal da API

    Returns:
        _type_: Saudação para acessar o Strawberry colocar um /grapql_
    """
    return {"message": "Bem-vindo à API de Previsão de Resultados de Partidas!"}
