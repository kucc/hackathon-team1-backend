from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class K_Test(Base):
    __tablename__ = 'K_TestTable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)

class K_MainEvent(Base):
    __tablename__ = 'K_MainEvent'

    main_event_id = Column(Integer, primary_key=True, autoincrement=True)
    event_date = Column(Date, nullable=False)
    event_name = Column(String(255), nullable=False)
    priority = Column(Integer, nullable=False, default=15)

class K_Event(Base):
    __tablename__ = 'K_Event'

    event_id = Column(Integer, primary_key=True, autoincrement=True)
    event_date = Column(Date, nullable=True)
    event_name = Column(String(255), nullable=True)
    priority = Column(Integer, nullable=False, default=0)
    event_type = Column(String(255), nullable=False)
    # event_type: Designated, Fixed, Routine
    category = Column(String(255), nullable=False)
    # category: Study, Exercise, Meal, Sleep, etc
    finished = Column(Boolean, nullable=False, default=False)
    activated = Column(Boolean, nullable=False, default=False)