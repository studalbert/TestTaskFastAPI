from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, func
from .base import Base

if TYPE_CHECKING:
    from .answer import Answer

class Question(Base):
    text: Mapped[str] = mapped_column(Text, unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.utcnow)
    answers: Mapped[list["Answer"]] = relationship(back_populates='question', cascade="all, delete-orphan")

