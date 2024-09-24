from pydantic import BaseModel

class InputData(BaseModel):
    Mandante: str
    Visitante: str
    Posicao_Mandante: int
    Posicao_Visitante: int