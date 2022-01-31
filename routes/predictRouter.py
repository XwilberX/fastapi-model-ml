from fastapi import APIRouter
from controllers import predictController

router = APIRouter (
    prefix="/api/v1"
)

router.include_router(predictController.router, tags=["predicts"])