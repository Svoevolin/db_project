from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship, Mapped
from database.models import Base


class CarMark(Base):
    __tablename__ = "car_mark"

    id_mark = mapped_column(Integer, primary_key=True, autoincrement=True)
    name_mark = mapped_column(String(20), nullable=False)

    models: Mapped[List["CarModel"]] = relationship(back_populates="mark")
