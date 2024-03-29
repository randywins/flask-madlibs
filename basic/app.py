from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():
    """Generate and show form to ask for words"""

    prompts = story.prompts

    return render_template("questions.html", promps=prompts)

@app.route("/story")
def show_story():
    """Show story"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)

