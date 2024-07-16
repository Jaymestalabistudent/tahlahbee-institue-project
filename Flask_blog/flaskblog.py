from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Tahlahbee Institute',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 08, 2024'
    },
    {
        'author': 'Institute',
        'title': 'Blog Post 2',
        'content': 'New post content',
        'date_posted': 'August 09, 2024'
    },
    {
       'author': 'tahlahbee institute',
        'title': 'Blog Post 3',
        'content': 'New post content',
        'date_posted': 'August 10, 2024'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


@app.route("/layout")
def layout():
    return render_template('layout.html', title = 'layout')


@app.route("/login")
def login():
    return render_template('login.html', title = 'login Please')

@app.route("/register")
def register():
    return render_template('register.html',  title = 'Register Please')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/tahlahbee")
def tahlahbee():
    return render_template('tahlahbee.html', title = 'test page')

@app.route("/info")
def info():
    return render_template('info.html', title = 'Information')

@app.route("/spotify")
def spotify():
    return render_template('spotify.html', title = 'Music and Podcast')

@app.route("/video")
def video():
    return render_template('video.html', title = 'Movies and Series')

if __name__ == '__main__':
    app.run(debug=True)