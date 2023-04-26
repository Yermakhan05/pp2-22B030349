import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Open a cursor to perform database operations
cur = conn.cursor()

value = 2
# cur.execute("SELECT * from transactions where customer_id = %s;", (value,))
results = cur.fetchone()

# Close the cursor and connection
cur.close()
conn.close()