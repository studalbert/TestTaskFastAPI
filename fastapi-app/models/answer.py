from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey, String, func
from .base import Base

if TYPE_CHECKING:
    from .question import Question

class Answer(Base):
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete='CASCADE'))
    user_id: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.utcnow)
    question: Mapped["Question"] = relationship(back_populates='answers')