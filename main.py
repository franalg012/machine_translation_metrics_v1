from fastapi import FastAPI
import uvicorn
from api.routes import router

app = FastAPI(title="Translation Metrics API")
app.include_router(router)

if __name__ == "__main__":
    port = 8000
    print(f"Escuchando en el puerto {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)