from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .crud_questions import get_questions, create_question, get_question, delete_question
from models import db_helper
from schemas.question import QuestionCreate, QuestionRead, QuestionWithAnswersRead

router = APIRouter()

@router.get("/", response_model=list[QuestionRead])
async def get_all_questions(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],):
    return await get_questions(session=session)

@router.post("/", response_model=QuestionRead)
async def create_question_(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
], question_in: QuestionCreate):
    return await create_question(session=session, question_in=question_in)

@router.get("/{id}/", response_model=QuestionWithAnswersRead)
async def get_question_by_id(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ], id: int):
    question = await get_question(session=session, question_id=id)
    if question:
        return question
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Question {id} not found')

@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question_by_id(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ], id: int) -> None:
    await delete_question(session=session, question_id=id)
