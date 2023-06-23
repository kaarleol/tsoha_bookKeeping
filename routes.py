from app import app
from flask import render_template, request, redirect, session
import books, users, reviews, favorites, futurereading

@app.route("/")
def index():
    list = reviews.get_list()
    if list:
        return render_template("index.html", count=len(list), reviews=list)
    else:
        return render_template("index.html", count=0, reviews=None)
    

@app.route("/allbooks")
def allbooks():
    dropdown_options = ['Luettu', 'Kesken']
    list = books.get_list()
    return render_template("allbooks.html", count=len(list), books=list, dropdown_options=dropdown_options)

@app.route("/newbook")
def newbook():
    return render_template("newbook.html")


@app.route("/newfavorite")
def newfavorite():
    list = favorites.get_list()
    if list:
        return render_template("newfavorite.html", count=len(list), favorites=list)
    else:
        return render_template("newfavorite.html", count=0, favorites=None)

@app.route("/newfuture")
def newfuture():
    list = futurereading.get_list()
    if list:
        return render_template("newfuture.html", count=len(list), futures=list)
    else:
        return render_template("newfuture.html", count=0, futures=None)


@app.route("/addbook", methods=["POST"])
def addbook():
    title = request.form["title"]
    author = request.form["author"]
    publication_date = request.form["publication_date"]
    genre = request.form["genre"]
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    
    if books.send(title, author, publication_date, genre):
        return redirect("/")
    else:
        return render_template("error.html", message="Kirjan lisäys ei onnistunut")
    
@app.route("/deletebook", methods=["POST"])
def deletebook():
    book_id = request.form["book_id"] 
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if book_id:
        if books.delete(book_id):
            return redirect("/allbooks")
        else:
            return render_template("error.html", message="Merkinnän poistaminen ei onnistunut")
    else:
        return render_template("error.html", message="Kirjan poistaminen ei onnistunut")
    
@app.route("/addreview", methods=["POST"])
def addreview():
    book_id = request.form["book_id"]
    read_status = request.form["read_status"]
    rating = request.form["rating"]
    review = request.form["review"]

    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if reviews.send(book_id, read_status, rating, review):
        return redirect("/")
    else:
        return render_template("error.html", message="Merkinnän lisäys ei onnistunut. Kaikki kentät pitää täyttää")
    
@app.route("/deletereview", methods=["POST"])
def deletereview():
    id = request.form["id"]
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if id:
        if reviews.delete(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Merkinnän poistaminen ei onnistunut")
    else:
        return render_template("error.html", message="Merkinnän poistaminen ei onnistunut")    
    
@app.route("/addfavorite", methods=["POST"])
def addfavorite():
    book_id = request.form["book_id"]

    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if favorites.send(book_id):
        return redirect("/newfavorite")
    else:
        return render_template("error.html", message="Suosikin lisäys ei onnistunut")    
    
@app.route("/deletefavorite", methods=["POST"])
def deletefavorite():
    id = request.form["id"]

    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if id:
        if favorites.delete(id):
            return redirect("/newfavorite")
        else:
            return render_template("error.html", message="Merkinnän poistaminen ei onnistunut")
    else:
        return render_template("error.html", message="Suosikin poistaminen ei onnistunut")
    
@app.route("/addfuture", methods=["POST"])
def addfuture():
    book_id = request.form["book_id"]

    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if futurereading.send(book_id):
        return redirect("/newfuture")
    else:
        return render_template("error.html", message="Lukulistan muutos ei onnistunut")  
    
@app.route("/deletefuture", methods=["POST"])
def deletefuture():
    id = request.form["id"]

    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Unauthorized action.")
    if id:
        if futurereading.delete(id):
            return redirect("/newfuture")
        else:
            return render_template("error.html", message="Merkinnän poistaminen ei onnistunut")
    else:
        return render_template("error.html", message="Merkinnän poistaminen ei onnistunut")
    
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if len(username)==0 or len(password1)==0:
            return render_template("error.html", message="Käyttäjänimi ja salasana eivät voi olla tyhjiä")
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
