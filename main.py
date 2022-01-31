from fastapi import FastAPI
import motor
from beanie import init_beanie

from utils import settings, db
from models.predictModel import predictModel
from routes.predictRouter import router as PredictRouter

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    version=settings.VERSION,
    docs_url="/"
)

# Añadiendo rutas
app.include_router(PredictRouter)

@app.on_event('startup')
async def app_init():
    #Creando el cliente de mongo\
    client = motor.motor_asyncio.AsyncIOMotorClient(
        db.Settings().mongo_dns
    )

    # Iniciar el odm beanie para MongoDB (odm creado por el creado de Fastapi)
    await init_beanie(client.predict_db, document_models=[predictModel])

    
