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

def get_user_data():
    """
    Function to retrieve user data from the database.
    """
    cur.execute("SELECT * FROM users;")
    user_data = cur.fetchall()
    return user_data

def rate_prompt(data):
    """
    Function to rate a prompt and store the rating in the database.
    """
    user_id = data['user_id']
    prompt_id = data['prompt_id']
    rating = data['rating']

    insert = sql.SQL(
        "INSERT INTO ratings (user_id, prompt_id, rating) VALUES ({}, {}, {});"
    ).format(sql.Identifier(user_id), sql.Identifier(prompt_id), sql.Identifier(rating))

    cur.execute(insert)
    conn.commit()

    return {"status": "success", "message": "Rating submitted successfully."}
```

