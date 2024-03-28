# Introduction to SQL Model

This Python application utilizes SQLModel with a PostgreSQL database to manage a table of heroes, each with a unique identifier, name, secret identity, and an optional age attribute.

## Configuration

The application attempts to load the database configuration from a `.env` file. If this file is not found, it defaults to a standard configuration. The `DATABASE_URL` is expected to be in the `.env` file, which is then parsed and modified to fit the PostgreSQL connection string format required by the database driver.

## Database Model

The `Hero` class defines the structure of the heroes table in the database. It includes fields for the hero's ID, name, secret name, and age.

## Database Operations

The application defines functions to interact with the database:
- `create_db_and_tables()`: Sets up the database tables based on the SQLModel definitions.
- `add()`: Adds a new hero instance to the database.
- `update(id: int)`: Updates the details of an existing hero in the database.
- `delete(id: int)`: Removes a hero from the database.

## Usage

To use the application:
1. Ensure you have a PostgreSQL database accessible and the `.env` file configured with the `DATABASE_URL`.
2. Run the script to create the database tables.
3. Use the `add`, `update`, and `delete` functions to manage heroes in the database.


## Example

Here's how you can add a new hero to the database:

```python
hero = Hero(name="Deadpond", secret_name="Dive Wilson")
add(hero)
```


To update a hero’s age:
```python
update(id=1, age=50)
```

To delete a hero:
```python
delete(id=1)
```


Please replace id with the actual ID of the hero you wish to update or delete.

**Dependencies**
-   SQLModel
-   Starlette
-   PostgreSQL
-   Psycopg (PostgreSQL adapter)

Make sure to install these dependencies before running the application.

Notes
The code includes comments to guide you through each step and function.
Uncomment the relevant lines in the 

`if __name__ == "__main__":`  block to perform database operations.

