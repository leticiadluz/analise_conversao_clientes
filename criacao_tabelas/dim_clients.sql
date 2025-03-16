CREATE TABLE dim_clients ( 
    customer_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')),
    age INT CHECK (age >= 0),
    average_ticket VARCHAR(10) 
);