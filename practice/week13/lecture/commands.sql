-- table - customers1; id, first_name, last_name
-- table - transactions; id, amount, type_op, date, customer_id

CREATE TABLE customers1 (
      id SERIAL PRIMARY KEY
    , first_name VARCHAR(30)
    , last_name VARCHAR(50)
);


CREATE TABLE transactions1 (
    id SERIAL PRIMARY KEY
    , type_op VARCHAR(3)
    , amount NUMERIC
    , date DATE
    , customer_id INT NOT NULL
    , FOREIGN KEY (customer_id) REFERENCES customers1(id) ON DELETE CASCADE
);
INSERT INTO transactions1 (id, type_op, amount, customer_id)
VALUES (1, 'DBT', 366, 2);
commit;

-- DROP TABLE transactions;

INSERT INTO customers1 (first_name, last_name)
VALUES ('roman', 'sv');

INSERT INTO customers1 (first_name, last_name)
VALUES ('bayazid', 'yr');
commit;

rollback;
-- sequence

ALTER TABLE customers1
ADD COLUMN region VARCHAR(10);

UPDATE customers1
SET region = 'ASTANA'
WHERE id = 8;


DELETE FROM customers1
WHERE id = 1;
TRUNCATE TABLE customers1;


select
    *
from customers1
    left join transactions1
        on customers1.id = transactions1.customer_id;

select * from customers1 where id = 2;



SELECT
--     *
    id
    , type_op
    , customer_id
    , amount
--     , date

FROM transactions1;

INSERT INTO customers1 (region) VALUES ("Almaty") WHERE first_name = 'roman';
