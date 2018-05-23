import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Star(db.Model):
    __tablename__ = 'stars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    movies = db.relationship('Movie', backref='star', cascade='delete')


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    about = db.Column(db.Text)
    year = db.Column(db.Integer)
    star_id = db.Column(db.Integer, db.ForeignKey('stars.id'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/movies')
def movies():
    movies = Movie.query.all()
    return render_template('all-movies.html', movies=movies)

@app.route('/movies/add', methods=['GET','POST'])
def add_movies():
    stars = Star.query.all()
    if request.method == 'GET':
        return render_template('movies-add.html', stars=stars)
    if request.method == 'POST':
        title = request.form['title']
        about = request.form['about']
        year = request.form['year']
        star_name = request.form['star_name']
        star = Star.query.filter_by(name=star_name).first()
        movie = Movie(title=title, about=about, year=year, star=star)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('movies'))


@app.route('/movies/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    stars = Star.query.all()
    if request.method == 'GET':
        return render_template('movies-edit.html', movie=movie, stars=stars)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.about = request.form['about']
        movie.year = request.form['year']
        star_name = request.form['star']
        star = Star.query.filter_by(name=star_name).first()
        movie.star = star
        db.session.commit()
        return redirect(url_for('movies'))


@app.route('/movies/delete/<int:id>', methods=['GET', 'POST'])
def delete_movies(id):
    movie = Movie.query.filter_by(id=id).first()
    stars = Star.query.all()
    if request.method == 'GET':
        return render_template('movies-delete.html', movie=movie, stars=stars)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('movies'))


@app.route('/stars')
def stars():
    stars = Star.query.all()
    return render_template('all-stars.html', stars=stars)


@app.route('/stars/add', methods=['GET','POST'])
def add_stars():
    stars = Star.query.all()
    if request.method == 'GET':
        return render_template('stars-add.html', stars=stars)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        star = Star(name=name, age=age)
        db.session.add(star)
        db.session.commit()
        return redirect(url_for('stars'))


@app.route('/stars/edit/<int:id>', methods=['GET', 'POST'])
def edit_stars(id):
    star = Star.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('stars-edit.html', star=star)
    if request.method == 'POST':
        star.name = request.form['name']
        star.age = request.form['age']
        db.session.commit()
        return redirect(url_for('stars'))


@app.route('/stars/delete/<int:id>', methods=['GET', 'POST'])
def delete_stars(id):
    star = Star.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('stars-delete.html', star=star)
    if request.method == 'POST':
        db.session.delete(star)
        db.session.commit()
        return redirect(url_for('stars'))

if __name__ == '__main__':
    app.run()
