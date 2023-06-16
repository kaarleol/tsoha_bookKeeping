from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT B.title, B.author, B.publication_date, B.genre, U.username FROM book B, users U WHERE B.added_by=U.user_id ORDER BY B.title")
    result = db.session.execute(sql)
    return result.fetchall()

def send(title, author, publication_date, genre):
    added_by = users.user_id()
    if added_by == 0:
        return False
    sql = text("INSERT INTO book (title, author, publication_date, genre, added_by) VALUES (:title, :author, :publication_date, :genre, :added_by)")
    db.session.execute(sql, {"title":title, "author":author, "publication_date":publication_date, "genre":genre, "added_by":added_by})
    db.session.commit()
    return True