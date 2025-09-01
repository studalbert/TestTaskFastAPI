from fastapi import APIRouter
from .views_questions import router as router_1
from .views_answers import router as router_2
router = APIRouter()
router.include_router(router_1, prefix='/questions', tags=['Questions'])
router.include_router(router_2, tags=['Answers'])