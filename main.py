import json
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from my_forms import EditForm, AddForm
from movie_data_finder import MovieDataFinder

# Create App
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favorite_movies.db"
db = SQLAlchemy(app)

# Add Bootstrap
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(300), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.Text, unique=True)
    img_url = db.Column(db.String, unique=True, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    my_movies = Movie.query.order_by(Movie.rating).all()
    for x in range(len(my_movies)):
        my_movies[x].ranking = len(my_movies) - x
    db.session.commit()
    return render_template("index.html", movie_list=my_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.add_movie.data
        movie_list = MovieDataFinder()
        data = movie_list.find_movies(movie_title)
        return render_template("select.html", choices=data)
    return render_template("add.html", form=add_form)


@app.route("/select")
def process_selection():
    """Gets relevant data for the chosen movie,
    records to the database, and redirects to
    the update page.
    """
    img_url = "https://image.tmdb.org/t/p/w500/"
    new_movie = Movie(
        title=request.args.get("title"),
        year=request.args.get("release").split("-")[0],
        img_url=f"{img_url}{request.args.get('img')}",
        description=request.args.get("description"),
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("add_movie", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Allows user to rate a movie and write a review."""
    form = EditForm()
    movie_id = request.args.get("id")
    movie = db.session.get(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(request.form["edit_rating"])
        movie.review = request.form["your_review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    db.session.delete(db.session.get(Movie, movie_id))
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
