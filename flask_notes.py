##################### FLASK ##################
# Setting up (all command lines besides pip go in GitBash)
    # 1) Create Venv
    # 2) pip install flask (within folder & venv)
    # 3) create app.py
    # 4) from flask import Flask
       # app = Flask(__name__)
    # 5) flask run

    # ctrl + 'c' to stop server

# Run in development mode
#*turns on debug mode & auto-refreshes when changes are made
    # commandline: 'export FLASK_ENV=development'  (this'll last until terminal or venv is closed -- can also keep this in .bash_profile folder)
    # commandline: 'flask run'

# Adding routes (url request)
@app.route('/hello') #this is the 'decorator & influence the function that comes immediately after it
def say_hello():
    return "Hello There!!!"


from flask import Flask, request

app = Flask(__name__)


@app.route('/')  # home page
def home_page():
    html = "<br><a href= '/hello'>Go to Hello Page<a>"
    return "Welcome to the prettiest home page ever!" + html


@app.route('/hello')
def say_hello():
    """Return simple "Hello" Greeting."""

    html = "<html><body><h1>Hello There!!!</h1><p>This is the Hello Page</p></body></html>"
    return html


@app.route('/goodbye')
def say_bye():
    return "Good Bye!"


# reads url query string
# request.args is a dict-like object for query parameters
# vv Example utilizes query string such as: 127.0.0.1:5000/search?term=dog&sort=date vv
@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args['sort']
    return f"<h1>Search Result For: {term}</h1><p>Sorted by: {sort}</p>"


########## handling post requests (usually comes from a <form>) ##################
# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You just made a post request"

# Commandline: curl -X POST http://127.0.0.1:5000/post

# Creating form = 'GET' & submitting form = 'POST'
@app.route("/add-comment")
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type="text" placeholder="comment" name='comment'/>
        <input type="text" placeholder="username" name='username'/>
        <button>Submit</button>
    </form>

    """


# ^^^ Pulls data from form
# request.form is a dict-like object of POST parameters
@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    user = request.form['username']
    return f"""
    <b>SAVED YOUR COMMENT:</b> {comment}
    <p><b>Username:</b>{user}</p>
    """


# Dynamic routes (wrap in brackets '<>')
# bracket keyword is automatically passed into function as an argument
# bracket keyword and argument need to match

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}


# 'int' must be transmutable to an int, otherwise it'll break
@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post Not Found")
    return f"<p>{post}</p>"


# Route w/ multiple variables
@app.route('/r/<subreddit>/comments/<int: post_id>')
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} <br> From the {subreddit} Subreddit</h1>"