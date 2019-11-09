from flask import Flask, render_template, redirect, request

from account_manager import AccountManager

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/redirect/login', methods=['POST'])
def redirect_login():
    username = request.form['username']
    password = request.form['password']
    account_manager = AccountManager()
    identity_id = account_manager.signin(username=username, password=password)
    if identity_id:
        return redirect(f'/blog?identity_id={identity_id}')
    else:
        return redirect('/login')


@app.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/blog/edit', methods=['GET'])
def blog_edit():
    return render_template('blog_edit.html')


@app.route('/blog/save', methods=['GET'])
def blog_save():
    return redirect('/blog')


@app.route('/blog/todo')
def blog_to_do_list():
    return render_template('blog_base.html', body='to_do_list.html')


@app.route('/blog/page/create')
def create_page():
    return render_template('markdown-editor/index.html')


@app.route('/blog/page/save', methods=['POST'])
def save_page():
    title = request.form['title']
    contents = request.form['contents']
    return title + '\n' + contents


if __name__ == '__main__':
    app.run()
