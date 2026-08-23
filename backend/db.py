from datetime import datetime
from sqlalchemy import create_engine, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class SetRow(Base):
    __tablename__ = "sets"

    id: Mapped[int] = mapped_column(primary_key=True)
    exercise_title: Mapped[str]
    start_time: Mapped[datetime]
    weight_lbs: Mapped[float]
    reps: Mapped[int]
    set_volume: Mapped[float]

engine = create_engine("sqlite:///workouts.db", echo=True)
Base.metadata.create_all(engine)