CREATE TABLE dim_clientes (
    customer_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')),
    age INT CHECK (age >= 0),
    segment_id INT,
    CONSTRAINT fk_segmento FOREIGN KEY (segment_id) REFERENCES dim_segmentos(segment_id)
);