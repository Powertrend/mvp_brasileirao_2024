# app/graphql/queries.py
from strawberry.types import Info
from app.services.graphql_services import GraphQLService

graphql_service = GraphQLService()


def resolve_predict_match(info: Info, mandante: str, visitante: str, posMandante: int, posVisitante: int):
    return graphql_service.predict_match(mandante, visitante, posMandante, posVisitante)
