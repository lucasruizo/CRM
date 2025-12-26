from fastapi import FastAPI
from app.auth.routes import router as auth_router




app = FastAPI(title="CRM Backend")

@app.get("/")
def root():
    return {"status": "CRM backend running"}

app.include_router(auth_router)
