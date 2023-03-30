from flask import Flask, request, render_template, redirect, url_for, flash 

app = Flask(__name__)

app.config.update(
    SECRET_KEY = "bananas"
)

book_list = [
    {"title": "The Hobbit", "author": "J.R.R Tolkien", "pages": "295", "classification": "fiction", "details":"read, recommend", "acquisition": "library"}
]

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Home Page", books=book_list
    )



@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        classification = form["classification"]
        acquisition = form["acquisition"]
        details = form.getlist("details")


        details_string = ",".join(details)

        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details_string,
            "acquisition": acquisition,
        }
        print(book_dict)
        book_list.append(book_dict)
        print(book_list)
        <div class="alert alert-success" role="alert">
        Record successfully added!
        flash('Record successfully added.' category = "success")
        </div>
        \
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/about", methods=["GET"])
def about():
    return render_template(
        "about.html", pageTitle="About Page"
    )

if __name__ == "__main__":
    app.run(debug=True)
