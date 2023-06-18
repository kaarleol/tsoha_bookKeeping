from db import db
import users
from sqlalchemy.sql import text

def get_list():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("SELECT B.book_id, F.id, B.title, B.author, B.publication_date, B.genre, U.username FROM future_reading F, book B, Users U WHERE F.book_id=B.book_id AND F.user_id=:user_id AND F.user_id=U.user_id ORDER BY B.title")
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def send(book_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO future_reading (user_id, book_id) VALUES (:user_id, :book_id)")
    db.session.execute(sql, {"user_id":user_id, "book_id":book_id})
    db.session.commit()
    return True

def delete(id):
    sql = text("DELETE FROM future_reading F WHERE F.id = :id")
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True