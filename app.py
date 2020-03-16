from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home_page():
    html = """
        <html>
            <body>
                <h1>Home Page</h1>
                <p>Welcome to my page</P>
                <a href='/hello'> Go to hello page</a>
            </body
        </html>    
    """
    return html


@app.route('/hello')
def say_hello():
    html = """
        <html>
            <body>
                <h1>Hello</h1>
                <p>This is the hello page</P>
            </body
        </html>    
    """
    return html


@app.route('/goodbye')
def say_bye():
    return 'Good Bye'


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
