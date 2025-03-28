CREATE TABLE fact_orders ( 
    order_id SERIAL PRIMARY KEY,  
    customer_id INT NOT NULL,  
    order_value DECIMAL(10,2) NOT NULL,  
    order_date DATE NOT NULL,  
    CONSTRAINT fk_orders_clients FOREIGN KEY (customer_id) 
        REFERENCES dim_clients(customer_id)
);
