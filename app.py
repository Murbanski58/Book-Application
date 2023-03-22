from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

book_list = [
    {"title": "The Hobbit", "Author": "J.R.R Tolkien", "Pages": "295", "Classification": "fiction", "Details":"read, recommend", "Acquisition": "library"}
]


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

       
        print(title)
        print(author)
        print(pages)
        print(classification)
        print(acquisition)
        print(details)

        details_string = ",".join(details)

        book_dict = {
            "Title": title,
            "Author": author,
            "Pages": pages,
            "Classification": classification,
            "Details": details,
            "Acquisition": acquisition,
        }
        print(book_dict)
        book_list.append(book_dict)
        print(book_list)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/about")
def about():
    return render_template(
        "about.html", pageTitle="About Page"
    )

if __name__ == "__main__":
    app.run(debug=True)
