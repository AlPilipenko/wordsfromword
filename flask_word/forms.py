from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from flask import request

from flask_word import word_factory

class SubmittedWordOn(FlaskForm):
    "Validates that submited word is valid"
    word = StringField('Type anything here (between 2 and 15 symbols):', validators=[DataRequired(), Length(min=2, max=15)],
                        render_kw={"placeholder": "..."})

    submit = SubmitField('process')


    def processed_word_info(flask_form_object, w):
        if w == None:
            return {}

        return word_factory.word_maker(w)

class SubmittedWordOff(FlaskForm):
    "Validates that submited word is valid"
    word = StringField('Type anything here (between 2 and 25 symbols):', validators=[DataRequired(), Length(min=2, max=25)],
                        render_kw={"placeholder": "..."})

    submit = SubmitField('process')


    def processed_word_info(flask_form_object, w):
        if w == None:
            return {}
    
        return word_factory.word_maker(w)
