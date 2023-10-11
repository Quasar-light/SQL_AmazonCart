--always create the tables that don't have a foreign key first
CREATE TABLE IF NOT EXISTS customer(customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30), 
    last_name VARCHAR(30), 
    address VARCHAR(150), 
    billing_info VARCHAR(100)
); 

-- Brand table creation (the dash, dash is how to make comments in sql)
CREATE TABLE IF NOT EXISTS brand(
    seller_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(150),
    contact_number VARCHAR(15),
    address VARCHAR(150)
);

-- INVETORY TABLE CREATION
CREATE TABLE IF NOT EXISTS inventory(
    upc SERIAL PRIMARY KEY,
    product_amount INTEGER
);

--product table creation
CREATE TABLE IF NOT EXISTS product(
    item_id SERIAL PRIMARY KEY,
    amount NUMERIC(5,2),
    prod_name VARCHAR(100),
    upc INTEGER NOT NULL, --constraint on the upc colum
    seller_id INTEGER NOT NULL
    FOREIGN KEY(seller_id) REFERENCES brand(seller_id),
    FOREIGN KEY(upc) REFERENCES inventory(upc)
);

-- Orders table creation
CREATE TABLE IF NOT EXISTS orders( --had to make order(s) instead of order because order is already a key
    order_id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE
    sub_total NUMERIC(8,2)
    total_cost NUMERIC(10,2),
    upc INTEGER NOT NULL,
    FOREIGN KEY(upc) REFERENCES invetory(upc)
);

-- cart table creation
CREATE TABLE IF NOT EXISTS cart(
    cart_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);





