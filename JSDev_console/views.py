"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from JSDev_console import app

@app.route("/")
@app.route("/index.<language>")
@app.route("/default.<language>")
def home(language: str="html"):
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

