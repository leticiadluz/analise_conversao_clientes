CREATE TABLE fato_conversoes (
    customer_id INT PRIMARY KEY,  
    control_group INT CHECK (control_group IN (0,1)) NOT NULL, 
    converted INT CHECK (converted IN (0,1)) NOT NULL,  
    CONSTRAINT fk_conversoes_clientes FOREIGN KEY (customer_id) 
        REFERENCES dim_clientes(customer_id)
);