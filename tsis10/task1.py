import psycopg2
import csv

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = con.cursor()

#cur.execute(
#    "CREATE TABLE PhoneBook (id SERIAL PRIMARY KEY, First_name VARCHAR(30), Last_name VARCHAR(50), Phone VARCHAR(30), Email VARCHAR(200));")

def from_csv():
    path = 'tsis10/'
    Name = 'PhoneBook.csv'
    file = open(path+Name, 'r')
    file_list = csv.reader(file)
    for row in file_list:
        cur.execute(
            "INSERT INTO PhoneBook (First_Name, Last_Name, Phone, Email) VALUES (%s, %s, %s, %s)", 
            (row[0], row[1], row[2], row[3])
        )
    con.commit()

def Update():
    New_Phone = '4437-419-46'
    cur.execute(
        "UPDATE PhoneBook SET Phone = %s WHERE id = %s", (New_Phone, 4)
    )
    con.commit()

def from_console():
    first_name = 'Kasym'
    last_name = 'Zhomart'
    phone = '8707-224-6936'
    email = 'myandasik05@gmail.com'
    cur.execute(
        "INSERT INTO PhoneBook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, phone, email)
    )
    con.commit()

def query_data():
    cur.execute(
        "SELECT * FROM PhoneBook WHERE First_Name = %s",
        ('Kasym',)
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records found")
    else:
        for row in rows:
            print(row)

def delete_data():
    cur.execute(
        "DELETE FROM PhoneBook WHERE Last_Name = %s",
        ('Jones',)
    )
    con.commit()

#from_csv()
#Update()
#from_console()
# query_data()
delete_data()

cur.close()
con.close()
