```python
import psycopg2
from psycopg2 import sql

# Establish a connection to the database
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

def create_tables():
    """
    Function to create tables in the database.
    """
    users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    prompts_table = """
    CREATE TABLE IF NOT EXISTS prompts (
        id SERIAL PRIMARY KEY,
        prompt TEXT NOT NULL,
        theme VARCHAR(50),
        emotion VARCHAR(50),
        genre VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    submissions_table = """
    CREATE TABLE IF NOT EXISTS submissions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        prompt_id INTEGER REFERENCES prompts(id),
        submission TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    ratings_table = """
    CREATE TABLE IF NOT EXISTS ratings (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        prompt_id INTEGER REFERENCES prompts(id),
        rating INTEGER CHECK (rating >= 1 AND rating <= 5),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cur.execute(users_table)
    cur.execute(prompts_table)
    cur.execute(submissions_table)
    cur.execute(ratings_table)

    conn.commit()

if __name__ == "__main__":
    create_tables()
```

