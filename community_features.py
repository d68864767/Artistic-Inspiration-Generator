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

def get_shared_prompts():
    """
    Function to retrieve shared prompts from the database.
    """
    cur.execute("SELECT * FROM shared_prompts;")
    shared_prompts = cur.fetchall()
    return shared_prompts

def share_prompt(data):
    """
    Function to share a prompt and store it in the database.
    """
    user_id = data['user_id']
    prompt_id = data['prompt_id']
    title = data['title']
    description = data['description']

    insert = sql.SQL(
        "INSERT INTO shared_prompts (user_id, prompt_id, title, description) VALUES ({}, {}, {}, {});"
    ).format(sql.Identifier(user_id), sql.Identifier(prompt_id), sql.Identifier(title), sql.Identifier(description))

    cur.execute(insert)
    conn.commit()

def get_prompt_ratings():
    """
    Function to retrieve prompt ratings from the database.
    """
    cur.execute("SELECT * FROM ratings;")
    ratings = cur.fetchall()
    return ratings
```
