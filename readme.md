CARA MENJALANKAN APPS
1. input syntax sql ini di db

        CREATE DATABASE tokomusik;
        USE tokomusik;

        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );

        CREATE TABLE products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price INT NOT NULL
        );

        CREATE TABLE orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product_id INT,
            quantity INT,
            total_price INT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );

2. Atur db di database.py masing2 service appnya
3. jalanin ini command python -m app_product.app
4. jalanin ini command python -m app_order.app
5. jalanin ini command python -m app_user.app
6. commandnya jalanin di terminal yang berbeda (gak perlu change directory langsung aja)
7. jalanin frontend di pages dashboard (caranya klik kanan terus live server di pagenya)
8. masukin ini data dummies ke sql di phpmyadmin
