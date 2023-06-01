from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    """Form to edit movie details."""
    edit_rating = StringField(
        "Your rating out of 10 e.g. 7.5", validators=[DataRequired()]
    )
    your_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddForm(FlaskForm):
    """Form to take in a movie title that can be searched for"""
    add_movie = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
