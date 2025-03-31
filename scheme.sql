CREATE TABLE users (int id PRIMARY KEY,
                    username VARCHAR unique NOT NULL,
                    email VARCHAR unique,
                    password VARCHAR);

INSERT INTO users (username, email, password) VALUES
    ("admin", "admin@email.com", "admin123"),
    ("user", "user@email.com", "user123"),
    ("test","test@email.com", "test123");


CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR NOT NULL,
                    author VARCHAR NOT NULL,
                    pages INTEGER);


INSERT INTO books (name, author, pages) VALUES
    ("kniha1", "autor1", 123),
    ("kniha2", "autor2", 234),
    ("kniha3", "autor3", 345);