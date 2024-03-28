# Introduction to Database Management

This Python script utilizes SQLModel to interact with a PostgreSQL database, managing a table of heroes with their respective details.

## Features

- **Database Initialization**: Set up the database and tables automatically.
- **Hero Creation**: Define hero entries with names, secret identities, and optional ages.
- **Batch Insertion**: Add multiple heroes to the database in one go.
- **Data Retrieval**: Fetch all heroes or a specific hero by ID.
- **SQL Injection Prevention**: Safeguard against SQL injection attacks.

## Requirements

- SQLModel
- psycopg


## Usage

To create the database and tables, run:

```python
create_db_and_tables()
```

To add predefined heroes to the database, run:

```python
adding_heroes()
```

To retrieve all heroes, uncomment and run:
```python
getting_heroes()
```

To fetch a specific hero by ID, uncomment and run with the desired ID:
```python
getting_specific_hero(id)
```

To prevent SQL injection while fetching a hero by ID, uncomment and run:
```python
preventing_sql_injection(id)
```


## Note
The script includes a demonstration of a raw SQL query and how to prevent SQL injection using SQLModel’s ORM capabilities.

### Disclaimer
Always ensure you have proper backups before running any scripts that modify your database.
