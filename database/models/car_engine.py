from typing import List
from sqlalchemy import String, Integer, Double
from sqlalchemy.orm import mapped_column, relationship, Mapped
from database.models import Base


class CarEngine(Base):
    __tablename__ = "car_engine"

    id_engine = mapped_column(Integer, primary_key=True, autoincrement=True)
    fuel_type = mapped_column(String(20), nullable=False)
    hoursepower = mapped_column(Integer, nullable=False)
    caparcity = mapped_column(String(4), nullable=False)

    cars: Mapped[List["Car"]] = relationship(back_populates="engine")
