from flask import Flask, render_template, url_for
app = Flask(__name__)


my_posts = [{'title': 'Post 1', 'author': 'Nikhil', 'content':'It is the first blog', 'date':'21 September, 2018'},
            {'title': 'Post 2', 'author': 'Prabhakar', 'content':'It is the second blog', 'date':'22 September, 2018'},
            {'title': 'Post 3', 'author': 'Styler', 'content':'It is the third blog', 'date':'23 September, 2018'}]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=my_posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)