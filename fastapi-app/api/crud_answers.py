"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession


from models import Answer
from schemas.answer import AnswerCreate


async def get_answer(session: AsyncSession, answer_id: int) -> Answer:
    stmt = select(Answer).where(Answer.id == answer_id)
    result: Result = await session.execute(stmt)
    answer = result.scalar_one_or_none()
    if answer:
        return answer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Answer {answer_id} not found')

async def create_answer(session: AsyncSession, answer_in: AnswerCreate) -> Answer:
    answer = Answer(**answer_in.model_dump())
    session.add(answer)
    await session.commit()
    await session.refresh(answer)
    return answer


async def delete_answer(session: AsyncSession, answer_id: int):
    answer = await get_answer(session=session, answer_id=answer_id)
    if answer:
        await session.delete(answer)
        await session.commit()
