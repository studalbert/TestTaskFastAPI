from datetime import datetime
from typing import List

from pydantic import BaseModel, constr

from schemas.answer import AnswerRead


class QuestionBase(BaseModel):
    """Базовая модель вопроса"""
    text: constr(min_length=1)

class QuestionCreate(QuestionBase):
    """Модель для создания нового вопроса"""
    pass

class QuestionRead(QuestionBase):
    """Модель для вывода информации о добавленном вопросе"""
    id: int
    created_at: datetime


class QuestionWithAnswersRead(QuestionBase):
    """Модель для вывода информации о добавленном вопросе вместе с ответами"""
    id: int
    created_at: datetime
    answers: List[AnswerRead] = []