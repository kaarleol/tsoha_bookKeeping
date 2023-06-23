from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT B.book_id, B.title, B.author, B.publication_date, B.genre, U.username, B.added_by FROM book B, users U WHERE B.added_by=U.user_id ORDER BY B.title")
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

def delete(book_id):
    sql = text("DELETE FROM book B WHERE B.book_id = :book_id")
    db.session.execute(sql, {"book_id":book_id})
    db.session.commit()
    return True

def edit(book_id, title, author, publication_date, genre):
    sql = text("UPDATE book SET title=:title, author=:author, publication_date=:publication_date, genre=:genre WHERE book_id=:book_id")
    db.session.execute(sql, {"title":title, "author":author, "publication_date":publication_date, "genre":genre, "book_id":book_id})
    db.session.commit()
    return True