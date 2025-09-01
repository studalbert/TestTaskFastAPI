from datetime import datetime

from pydantic import BaseModel

class AnswerBase(BaseModel):
    """Базовая модель ответа"""
    text: str

class AnswerCreate(AnswerBase):
    """Модель для создания нового ответа"""
    question_id: int
    user_id: str

class AnswerRead(AnswerBase):
    """Модель для вывода информации о добавленном ответе"""
    id: int
    question_id: int
    user_id: str
    created_at: datetime