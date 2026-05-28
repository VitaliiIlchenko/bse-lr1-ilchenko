from fastapi import FastAPI
from pydantic import BaseModel
from main import SmartDocAI

app = FastAPI(title="SmartDoc API")
ai = SmartDocAI()

# Схема даних, які ми будемо отримувати від користувача
class FileRequest(BaseModel):
    filename: str
    size_mb: float
    is_priority: bool = False

# 1. Ендпоінт для перевірки працездатності,
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running perfectly"}

# 2. Основний ендпоінт для обробки документів
@app.post("/api/process")
def process_file(request: FileRequest):
    is_valid, msg = ai.validate_file(request.filename, request.size_mb)
    
    if not is_valid:
        return {"status": "error", "message": msg}

    fee = ai.calculate_processing_fee(request.size_mb, request.is_priority)
    doc_type = ai.get_document_type(request.filename)

    return {
        "status": "success",
        "filename": request.filename,
        "document_type": doc_type,
        "fee": fee,
        "message": "Файл успішно оброблено"
    }