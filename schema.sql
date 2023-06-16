CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE Book (
  book_id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  publication_date DATE NOT NULL,
  genre VARCHAR(255) NOT NULL,
  added_by INT,
  FOREIGN KEY (added_by) REFERENCES Users(user_id)
);

CREATE TABLE User_Books (
  user_id INT,
  book_id INT,
  read_status VARCHAR(50) NOT NULL,
  rating INT,
  review TEXT,
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE Book_Genre (
  genre_id INT PRIMARY KEY,
  genre_name VARCHAR(255) NOT NULL
);

CREATE TABLE User_Favorites (
  user_id INT,
  book_id INT,
  favorite_date DATE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User(user_id),
  FOREIGN KEY (book_id) REFERENCES Book(book_id)
);