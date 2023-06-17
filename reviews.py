from db import db
import users
from sqlalchemy.sql import text

def get_list():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("SELECT B.title, B.author, B.publication_date, B.genre, R.read_status, R.rating, R.review, U.username FROM User_Books R, book B, Users U WHERE R.book_id=B.book_id AND R.user_id=:user_id AND R.user_id=U.user_id ORDER BY R.rating")
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def send(book_id, read_status, rating, review):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO user_books (user_id, book_id, read_status, rating, review) VALUES (:user_id, :book_id, :read_status, :rating, :review)")
    db.session.execute(sql, {"user_id":user_id, "book_id":book_id, "read_status":read_status, "rating":rating, "review":review})
    db.session.commit()
    return True