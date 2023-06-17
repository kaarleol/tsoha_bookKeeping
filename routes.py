from app import app
from flask import render_template, request, redirect
import books, users, reviews

@app.route("/")
def index():
    list = reviews.get_list()
    if list:
        return render_template("index.html", count=len(list), reviews=list)
    else:
        return render_template("index.html", count=0, reviews=None)
    

@app.route("/allbooks")
def allbooks():
    list = books.get_list()
    return render_template("allbooks.html", count=len(list), books=list)

@app.route("/newbook")
def newbook():
    return render_template("newbook.html")

@app.route("/newreview")
def newreview():
    dropdown_options = ['Luettu', 'Kesken']
    return render_template('newreview.html', dropdown_options=dropdown_options)


@app.route("/addbook", methods=["POST"])
def addbook():
    title = request.form["title"]
    author = request.form["author"]
    publication_date = request.form["publication_date"]
    genre = request.form["genre"]
    if books.send(title, author, publication_date, genre):
        return redirect("/")
    else:
        return render_template("error.html", message="Kirjan lisäys ei onnistunut")
    
@app.route("/addreview", methods=["POST"])
def addreview():
    book_id = request.form["book_id"]
    read_status = request.form["read_status"]
    rating = request.form["rating"]
    review = request.form["review"]
    if reviews.send(book_id, read_status, rating, review):
        return redirect("/")
    else:
        return render_template("error.html", message="Merkinnän lisäys ei onnistunut")
    

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
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
