"""Controlador dos acessos requisições

    Raises:
        HTTPException: 500 error predict

    Returns:
        _type_: O Resultado da execução do modelo treinado
    """
from fastapi import APIRouter, HTTPException
from models.input_data import InputData
from app.services.model_service import ModelService

router = APIRouter()
model_service = ModelService()


@router.post("/predict")
async def predict(data: InputData):
    """Função Assync para retornar a predição

    Args:
        data (InputData): Mandante, Visistante, pos_mandante e pos_visitante

    Raises:
        HTTPException: 500 error

    Returns:
        _type_: Resultado previtao
    """
    try:
        # Pré-processando e fazendo a predição
        input_data_scaled = model_service.preprocess_input(data)
        resultado = model_service.predict(input_data_scaled)
        return {"resultado_previsto": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {e}")
