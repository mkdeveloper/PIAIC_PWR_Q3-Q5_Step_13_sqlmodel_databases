# from db_tutorial import settings
from sqlmodel import SQLModel, create_engine, Field, Session, select
from typing import Optional, Any
from sqlalchemy.sql import text

from starlette.config import Config
from starlette.datastructures import Secret

try:
    Config = Config(".env")
except:
    Config = Config()

Database_URL = Config("DATABASE_URL", cast=Secret)

connection_string = str(Database_URL).replace(
    "postgresql", "postgresql+psycopg")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine(connection_string)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# creating multiple heroes


hero_3 = Hero(name="Deadpool", secret_name="Dade Wilson")
hero_4 = Hero(name="Spider-Man", secret_name="Pedro Parqueador")
hero_5 = Hero(name="Hulk", secret_name="Bruce Banner")
hero_6 = Hero(name="Thor", secret_name="Thor Odinson")
hero_7 = Hero(name="Captain America", secret_name="Steve Rogers")
hero_8 = Hero(name="Rogue", secret_name="Rogue")
hero_9 = Hero(name="Iron Man", secret_name="Tony Stark")

# adding all heroes to database


def adding_heroes():
    with Session(engine) as session:
        session.add_all(
            [hero_3, hero_4, hero_5, hero_6, hero_7, hero_8, hero_9])
        session.commit()
        session.refresh(hero_3)
        session.refresh(hero_4)
        session.refresh(hero_5)
        session.refresh(hero_6)
        session.refresh(hero_7)
        session.refresh(hero_8)
        session.refresh(hero_9)

        print("Record Added")
# getting all heroes


def getting_heroes():
    with Session(engine) as session:
        # writing raw sql query instead using sqlModel
        statement = text("SELECT * FROM hero;")
        results = session.exec(statement).all()
        for result in results:
            print(result)

# getting specific Hero


def getting_specific_hero(id: int):
    with Session(engine) as session:
        statement = text(
            f"select from hero WHERE id = {id};")
        results = session.exec(statement).first()
        print(results)

# SQL INJECTION
# select * from hero; drop table hero;
# will be displayed in neon console SQL EDITOR

# preventing sql injection


def preventing_sql_injection(id: int):
    with Session(engine) as session:
        result = session.exec(select(Hero).where(Hero.id == id))
        hero = result.first()
        print(hero)

# Benefits of using sqlModel, or any other ORM:
        # Editor Support
        # autocomplete


if __name__ == "__main__":
    create_db_and_tables()
    adding_heroes()
    # getting_heroes()
    # getting_specific_hero(3)
    # preventing_sql_injection(3)
