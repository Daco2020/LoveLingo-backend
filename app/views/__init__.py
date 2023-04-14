from fastapi.routing import APIRouter
from app.views import lovelingo


router = APIRouter()


router.include_router(lovelingo.router, prefix="/lovelingos", tags=["LoveLingo"])
