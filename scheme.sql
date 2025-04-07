CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR,
    role VARCHAR NOT NULL
);

INSERT INTO users (username, email, password, role) VALUES
    ("admin", "admin@email.com", "admin123", "admin"),
    ("user", "user@email.com", "user123", "user"),
    ("test", "test@email.com", "test123", "user");

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    pages INTEGER,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO books (name, author, pages, user_id) VALUES
    ("kniha1", "autor1", 123, 1),
    ("kniha2", "autor2", 234, 1),
    ("kniha3", "autor3", 345, 2);