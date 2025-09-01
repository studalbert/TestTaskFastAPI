"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Question
from schemas.question import QuestionCreate


async def get_questions(session: AsyncSession) -> list[Question]:
    stmt = select(Question).order_by(Question.id)
    result: Result = await session.execute(stmt)
    questions = result.scalars().all()
    return list(questions)

async def get_question(session: AsyncSession, question_id: int) -> Question | None:
    stmt = select(Question).where(Question.id == question_id).options(selectinload(Question.answers))
    result: Result = await session.execute(stmt)
    question = result.scalar_one_or_none()
    return question

async def create_question(session: AsyncSession, question_in: QuestionCreate) -> Question:
    question = Question(**question_in.model_dump())
    session.add(question)
    try:
        await session.commit()
        await session.refresh(question)
        return question
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=404, detail='Such a question already exists')

async def delete_question(session: AsyncSession, question_id: int):
    question = await get_question(session=session, question_id=question_id)
    if question:
        await session.delete(question)
        await session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Question {question_id} not found')