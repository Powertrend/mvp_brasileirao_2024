# app/controllers/api_controller.py
from fastapi import APIRouter, HTTPException
from models.input_data import InputData
from app.services.model_service import ModelService

router = APIRouter()
model_service = ModelService()

@router.post("/predict")
async def predict(data: InputData):
    try:
        # Pré-processando e fazendo a predição
        input_data_scaled = model_service.preprocess_input(data)
        resultado = model_service.predict(input_data_scaled)
        return {"resultado_previsto": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {e}")
