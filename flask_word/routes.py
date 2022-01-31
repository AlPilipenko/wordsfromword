from flask import render_template, url_for, request, flash, redirect
from flask_word import app
from flask_word.forms import SubmittedWordOn, SubmittedWordOff


"app adding additional functionality to existing func"
"'GET','POST'  - to get and post requests"

@app.route('/',methods=['GET','POST'])   # what we type in browser to go on different pages  | aka @app - 'decorator'| '/' - homepage
@app.route('/on',methods=['GET','POST'])
def main_page_on():
    word_form = SubmittedWordOn()
    if word_form.validate_on_submit():
        "bootstrap category 'danger' for the alert insteas of 'success'"
        flash(f'word submited: {word_form.word.data}', 'success')
        return render_template('home_page_on.html',word_form=word_form)
    "render_template - allows to return created html templates"
    return render_template('home_page_on.html',word_form=word_form)


@app.route('/off',methods=['GET','POST'])
def main_page_off():
    word_form = SubmittedWordOff()
    if word_form.validate_on_submit():
        flash(f'word submited: {word_form.word.data}', 'success')
        return render_template('home_page_off.html',word_form=word_form)
    return render_template('home_page_off.html',word_form=word_form)
