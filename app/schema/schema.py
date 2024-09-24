# app/schema/schema.py
import strawberry
from app.graphql.queries import resolve_predict_match

@strawberry.type
class Query:
    @strawberry.field
    def predict_match(self, info: strawberry.types.Info, mandante: str, visitante: str, posMandante: int, posVisitante: int) -> str:
        return resolve_predict_match(info, mandante, visitante, posMandante, posVisitante)

schema = strawberry.Schema(query=Query)
