from sqlalchemy import MetaData, Column, Table, Integer, String, ForeignKey
from database import base

metadata = MetaData()

class Sociology(base):
    __tablename__ = "sociology"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # добавить все вопросы анкеты через Column()
    # opinion = Column(String) <- пример (первый вопрос)
