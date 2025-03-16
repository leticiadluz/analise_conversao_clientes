CREATE TABLE fact_conversions ( 
    customer_id INT PRIMARY KEY,  
    test_group INT CHECK (test_group IN (0,1)) NOT NULL,  
    converted INT CHECK (converted IN (0,1)) NOT NULL,  
    communication VARCHAR(20), -- Definir um tamanho adequado para a string
    CONSTRAINT fk_conversions_clients FOREIGN KEY (customer_id) 
        REFERENCES dim_clients(customer_id)
);
