import flask

app = flask.Flask(__name__)

posts = []


@app.route('/')
def homepage():
    return flask.render_template('home.html')


@app.route('/blog')
def blog_page():
    return flask.render_template('blog.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    if flask.request.method == 'POST':
        title = flask.request.form['title']
        content = flask.request.form['content']
        global posts

        posts.append({
            'title': title,
            'content': content
        })

        return flask.redirect(flask.url_for('blog_page'))
    return flask.render_template('new_post.html')


@app.route('/post/<string:title>')
def see_post(title):
    global posts

    for post in posts:
        if post['title'] == title:
            return flask.render_template('post.html', post=post)

    return flask.render_template('post.html', post=None)


if __name__ == '__main__':
    app.run()
