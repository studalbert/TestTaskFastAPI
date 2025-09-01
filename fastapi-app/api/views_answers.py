from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .crud_answers import create_answer, get_answer, delete_answer
from models import db_helper
from schemas.answer import AnswerCreate, AnswerRead, AnswerBase
from .crud_questions import get_question

router = APIRouter()


@router.post("/questions/{id}/answers/", response_model=AnswerRead)
async def create_answer_(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
], id:int, answer_in: AnswerBase):
    question = await get_question(session=session, question_id=id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Question {id} not found')
    answer = AnswerCreate(text=answer_in.text, user_id=answer_in.user_id, question_id=id)
    return await create_answer(session=session, answer_in=answer)

@router.get("/answers/{id}/", response_model=AnswerRead)
async def get_answer_by_id(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ], id: int):
    answer = await get_answer(session=session, answer_id=id)
    if answer:
        return answer


@router.delete("/answers/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer_by_id(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ], id: int) -> None:
    await delete_answer(session=session, answer_id=id)
