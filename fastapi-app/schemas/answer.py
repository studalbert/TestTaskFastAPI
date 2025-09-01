from datetime import datetime

from pydantic import BaseModel, constr


class AnswerBase(BaseModel):
    """Базовая модель ответа"""
    text: constr(min_length=1)
    user_id: str

class AnswerCreate(AnswerBase):
    """Модель для создания нового ответа"""
    question_id: int
    user_id: str

class AnswerRead(AnswerBase):
    """Модель для вывода информации о добавленном ответе"""
    id: int
    question_id: int
    created_at: datetime