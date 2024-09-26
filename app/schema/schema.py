"""Schema representação modelo

    Returns:
        _type_: Estrutura de dados
    """
import strawberry
from app.graphql.queries import resolve_predict_match


@strawberry.type
class Query:
    """Query de predição

    Returns:
        _type_: Predição de jogos
    """
    @strawberry.field
    def predict_match(self, info: strawberry.types.Info, mandante: str, visitante: str,
                      pos_mandante: int, pos_visitante: int) -> str:
        """Função que aciona a AI para Predição

        Args:
            info (strawberry.types.Info): _description_
            mandante (str): Nome do Time
            visitante (str): Nome do Time
            pos_mandante (int): Colcocação na tabela
            pos_visitante (int): Colcocação na tabela

        Returns:
            str: Vitoria_MAndante, Vitoria_Visitante, Empate
        """
        return resolve_predict_match(info, mandante, visitante, pos_mandante, pos_visitante)


schema = strawberry.Schema(query=Query)
