"""Query AI Predição

    Returns:
        _type_: GraphQl
    """
from strawberry.types import Info
from app.services.graphql_services import GraphQLService

graphql_service = GraphQLService()


def resolve_predict_match(info: Info, mandante: str, visitante: str,
                          pos_mandante: int, pos_visitante: int):
    """_summary_

    Args:
        info (Info): _description_
        mandante (str): _description_
        visitante (str): _description_
        pos_mandante (int): _description_
        pos_visitante (int): _description_

    Returns:
        _type_: _description_
    """
    return graphql_service.predict_match(mandante, visitante, pos_mandante, pos_visitante)
