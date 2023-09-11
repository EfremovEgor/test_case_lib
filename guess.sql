CREATE TABLE Products (
    ID SERIAL PRIMARY KEY,
    product varchar(255) NOT NULL,
    categories INTEGER[] DEFAULT array[]::INTEGER[]
);


INSERT INTO Products(product,categories)
VALUES ('product1',ARRAY[1,2])
INSERT INTO Products(product,categories)
VALUES ('product2',ARRAY[2,3])
INSERT INTO Products(product,categories)
VALUES ('product3',ARRAY[]::INTEGER[])
INSERT INTO Products(product,categories)
VALUES ('product4',ARRAY[4])
INSERT INTO Products(product,categories)
VALUES ('product5',ARRAY[1,3])

CREATE TABLE Categories (
    ID SERIAL PRIMARY KEY,
    category varchar(255) NOT NULL,
    products INTEGER[] DEFAULT array[]::INTEGER[]
);
INSERT INTO Categories(category,products)
VALUES ('category1',ARRAY[1,5])
INSERT INTO Categories(category,products)
VALUES ('category2',ARRAY[1,2])
INSERT INTO Categories(category,products)
VALUES ('category3',ARRAY[2,5])
INSERT INTO Categories(category,products)
VALUES ('category4',ARRAY[1,4])
INSERT INTO Categories(category,products)
VALUES ('category5',ARRAY[]::INTEGER[])

WITH unnested_products as (SELECT product,UNNEST(categories) FROM products) 
SELECT unnested_products.product,categories.category from unnested_products 
INNER JOIN categories on unnested_products.unnest = categories.id