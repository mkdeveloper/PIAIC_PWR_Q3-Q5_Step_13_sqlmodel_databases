# Importing necessary classes and functions from libraries
from typing import Optional
from sqlmodel import Session, select, SQLModel, Field, create_engine
from starlette.config import Config
from starlette.datastructures import Secret

# Attempt to load configuration from a .env file
try:
    Config = Config(".env")
except:
    # If loading fails, create a default configuration
    Config = Config()

# Retrieve the DATABASE_URL from the configuration, cast it as a Secret
database_url = Config("DATABASE_URL", cast=Secret)

# Convert the database URL to a string and replace 'postgresql' with 'postgresql+psycopg'
# This is needed for the database driver to understand the connection string
database_connection_string = str(database_url).replace(
    "postgresql", "postgresql+psycopg")

# Create a database engine that will manage connections to the database
# 'echo=True' enables logging of all the SQL statements executed
engine = create_engine(database_connection_string, echo=True)

# Define a Hero model that will be used to represent a table in the database


class Hero(SQLModel, table=True):
    # Unique identifier for each hero, automatically assigned if not provided
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # The hero's name
    secret_name: str  # The hero's secret identity
    age: Optional[int] = None  # The hero's age, which is optional


# Create the database tables based on the SQLModel definitions
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Create instances of the Hero model
# A new hero instance
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# Another new hero instance
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")

# Function to add a hero to the database


def add():
    with Session(engine) as session:  # Start a new database session
        session.add(hero_1)  # Add the new hero to the session
        # To Add multiple hero instances to the session
        # session.add_all([hero_1, hero_2])
        session.commit()  # Commit the changes to the database
        # Refresh the instance with the new data from the database
        session.refresh(hero_1)
        # session.refresh(hero_2)


# Function to update a hero's details in the database


def update(id: int):
    with Session(engine) as session:  # Start a new database session
        # Prepare a query to select the hero with id
        statement = select(Hero).where(Hero.id == id)
        # Execute the query and get the first result
        hero = session.exec(statement).first()
        hero.age = 50  # Update the hero's age
        session.commit()  # Commit the changes to the database
        # Refresh the instance with the new data from the database
        session.refresh(hero)


# Function to delete a hero from the database


def delete(id: int):
    with Session(engine) as session:  # Start a new database session
        # Prepare a query to select the hero with id
        statement = select(Hero).where(Hero.id == id)
        # Execute the query and get the first result
        hero = session.exec(statement).first()
        session.delete(hero)  # Delete the hero from the session
        session.commit()  # Commit the changes to the database
        return hero


if __name__ == "__main__":
    create_db_and_tables()
    # Calling the add function to execute it
    # add()

    # Uncomment the following line to execute the update function
    # update(2)

    # Uncomment the following line to execute the delete function
    delete(2)
