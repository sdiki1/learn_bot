import enum, sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import String, Integer, Float, Column, Enum, create_engine, ForeignKey, DATETIME

engine = create_engine("sqlite:////Users/vladimirbuharin/learning/programming/learn_bot/Untitled.db")
Session = sessionmaker()
session = Session(bind=engine)

class male(enum.Enum):
    dont_know = 0
    male = 1
    female = 2


Base = declarative_base()
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_user_id = Column(Integer)
    tg_user_chat_id = Column(Integer)
    name = Column(String(255))
    age = Column(Integer)
    male = Column(Enum(male))



class List(Base):
    __tablename__ = "lists"
    id_list = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    path_to_json = Column(String(255))

