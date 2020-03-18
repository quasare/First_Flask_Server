from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/form')
def show_form():
    return render_template("form.html")


COMPLIMENTS = ["cool", "smart", "bold", 'calm', "Determined"]


@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')


@app.route('/spell/<word>')
def spell_work(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)


@app.route('/greet')
def get_greeting():
    nice_thing = choice(COMPLIMENTS)
    username = request.args['username']
    return render_template('greet.html', username=username, compliment=nice_thing)


@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliment=wants, compliments=nice_things)


@app.route('/hello/')
def say_hello():

    return render_template("hello.html")


@app.route('/lucky')
def show_lucky_num():
    "Example of simple dynamic template"

    num = randint(1, 10)

    return render_template("lucky.html", lucky_num=num, msg="You are so lucky")

@app.route('/search')
def search():
    term = request.args['term']
    sort = request.args['sort']
    return f'<h1>Search Results For: {term}</h1> <p> sorting by: {sort}</p>'


# @app.route('/post', methods=["POST"])
# def post_demo():
#     return "You made a post request"


@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
      <h1>Add Comment </h1>  
      <form method="POST">
        <input type='text' placeholder='coment' name="comment">
        <input type='text' placeholder='username' name="username">
        <button>Submit</button>
      </form>
      """


@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""

    comment = request.form["comment"]
    username = request.form['username']
    # TODO: save that into a database!

    return f"""
    <h1>Saved Your Comment"</h1>
    <ul>
        <li>Username: {username} </p>
        <li>Coment: {comment} </li>
    </ul>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f'<h1>Browsing the {subreddit} Subreddit </h1>'


@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f'<h1>Viewing comments for post with id: {post_id} from the {subreddit} subreddit</h1>'


POSTS = {
    1: 'I Like Tacos',
    2: 'I want a Aston Martin',
    3: 'Squiggly Doodle',
    4: 'Bow Wow'
}


@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, 'Post not found')
    return f"<p>{post}</p>"


USERS = {
    "whiskey": "Whiskey The Dog",
    "spike": "Spike The Porcupine",
}


@app.route('/user/<username>')
def show_user_profile(username):
    """Show user profile for user."""

    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"
