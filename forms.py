from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """form for adding a pet"""
    allowed_species = ['dog', 'cat', 'porcupine']
    min_age = 0
    max_age = 30

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=allowed_species)
    photo_url = StringField("Photo URL", validators=[URL(), optional()])
    age = IntegerField("Age", validators=[NumberRange(min=min_age, max=max_age,
                                                      message=f"Age must be between {min_age} and {max_age}")])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """for for editing a pet"""
    photo_url = StringField("Photo URL", validators=[URL(), optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")
