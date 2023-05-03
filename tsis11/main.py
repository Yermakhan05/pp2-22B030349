import psycopg2

def main():

    try:
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'postgres',
            user = 'postgres',
            password = 'postgres',
        )

        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook_table(
                    id  SERIAL PRIMARY KEY,
                    first_name VARCHAR(30) NOT NULL,
                    last_name VARCHAR(30) NOT NULL,
                    phone_num VARCHAR(30) NOT NULL
        )''')
        conn.commit()

        print(
        '''
        1 - Get records by pattern
        2 - Insert new user
        3 - Insert new users
        4 - Querying data from the tables with pagination (by limit and offset)
        5 - Deleting data from tables by username or phone
        ''')

        COMMAND = int(input())
        if COMMAND == 1:
            pattern = input()

            cur.execute('''
            CREATE OR REPLACE FUNCTION getting_records(pattern VARCHAR)
            RETURNS table(id INTEGER, first_name VARCHAR, last_name VARCHAR, phone_num VARCHAR)
            AS $$
            BEGIN 
              RETURN QUERY
              SELECT * FROM phonebook_table WHERE phonebook_table.first_name LIKE '%' || pattern || '%' OR phonebook_table.last_name LIKE '%' || pattern || '%' OR phonebook_table.phone_num LIKE '%' || pattern || '%';
            END
            $$ language plpgsql
            ''')
            conn.commit()

            cur.execute(f'''SELECT * FROM getting_records('{pattern}')''')
            res = cur.fetchall()

            for row in res: print(row)

        if COMMAND == 2:
            cur.execute('''
            CREATE OR REPLACE PROCEDURE insert_user(name VARCHAR, lastname VARCHAR, phone VARCHAR)
            LANGUAGE plpgsql
            AS $$
            BEGIN
              IF EXISTS(SELECT 1 FROM phonebook_table WHERE first_name = name AND last_name = lastname) THEN
                UPDATE phonebook_table SET phone_num = phone WHERE first_name = name AND last_name = lastname;
              ELSE
                INSERT INTO phonebook_table(first_name, last_name, phone_num) VALUES (name, lastname, phone);
              END IF;
            END;
            $$;''')
            conn.commit()

            name = input('Enter name:')
            lastname = input('Enter lastname:')
            phone = input('Enter phone number:')
            cur.execute(f'''CALL insert_user('{name}', '{lastname}','{phone}')''')
            conn.commit()

        if COMMAND == 3:
            cur.execute('''
            CREATE OR REPLACE PROCEDURE insert_users(
              IN names_list text[],
              IN surnames_list text[],
              IN phones_list text[]
            )
            LANGUAGE plpgsql
            AS $$
            DECLARE
              i integer;
              invalid_phones text[];
            BEGIN
              IF array_length(names_list, 1) != array_length(surnames_list, 1) OR array_length(names_list, 1) != array_length(phones_list, 1) 
              THEN  RAISE EXCEPTION 'Input arrays must have the same length';
              END IF;
            
              FOR i IN 1..array_length(names_list, 1) LOOP
                IF phones_list[i] ~ '\D' THEN
                  invalid_phones := array_append(invalid_phones, phones_list[i]);
                ELSE
                  INSERT INTO phonebook_table (first_name, last_name, phone_num)
                  VALUES (names_list[i], surnames_list[i], phones_list[i]);
                END IF;
              END LOOP;
            
              IF array_length(invalid_phones, 1) > 0 THEN
                RAISE NOTICE 'The following phone numbers are invalid: %', invalid_phones;
              END IF;
            END;
            $$;''')
            conn.commit()


            names = input().split()
            surnames = input().split()
            phones = input().split()

            cur.execute("CALL insert_users(%s, %s, %s)", (names, surnames, phones))
            conn.commit()

        if COMMAND == 4:
            cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
                    RETURNS SETOF phonebook_table
                    AS $$
                    SELECT * FROM phonebook_table
                        ORDER BY first_name
                        LIMIT a OFFSET b;
                    $$
                    language sql;""")
            conn.commit()

            Limit = input('Enter limit:')
            Offset = input('Enter offset:')

            cur.execute(f'''SELECT * FROM paginating({Limit}, {Offset});''')

            res = cur.fetchall()

            for row in res:
                print(row)

        if COMMAND == 5:
            cur.execute('''
            CREATE OR REPLACE PROCEDURE delete_from_phonebook(IN search_text TEXT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
              DELETE FROM phonebook_table
              WHERE first_name ILIKE '%' || search_text || '%'
              OR last_name ILIKE '%' || search_text || '%'
              OR phone_num ILIKE '%' || search_text || '%';
            END;
            $$;''')
            conn.commit()

            pattern = input()
            cur.execute(f'''Call delete_from_phonebook('{pattern}')''')

        conn.commit()
        cur.close()
        conn.close()

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    main()