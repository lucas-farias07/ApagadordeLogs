import psycopg2
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define your database connection parameters
conn = psycopg2.connect(
    dbname="TesteApagador",
    user="postgres",
    password="controle34",
    host="localhost",
    port="5432"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    log_level VARCHAR(10),
    message TEXT
);
"""
cur.execute(create_table_query)

# Insert 10,000 fake logs
insert_query = "INSERT INTO logs (timestamp, log_level, message) VALUES (%s, %s, %s)"
logs = []
for _ in range(10000):
    timestamp = fake.date_time_this_year()
    log_level = fake.random_element(elements=("INFO", "WARNING", "ERROR", "DEBUG"))
    message = fake.sentence(nb_words=6)
    logs.append((timestamp, log_level, message))

# Execute insert query in batches for efficiency
cur.executemany(insert_query, logs)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Inserted 10,000 fake logs successfully.")