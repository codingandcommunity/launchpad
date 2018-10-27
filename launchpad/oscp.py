from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '\xa4>\xb5\xd3m\xcb\r\xb2\xf93\xd1\xc1~\x8bQ\xe4'

posts = [
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Need help with...',
		'date_posted': 'September 30, 2018'
	},
	{
		'author': 'John Smith',
		'title': 'test post',
		'content': 'Second post content',
		'date_posted': 'September 1, 2018'
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html",posts=posts)

@app.route("/about")
def about():
	return render_template("about.html",title='About')

@app.route("/myprojects")
def myprojects():
	return render_template("myprojects.html",title='My Projects')

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title = 'Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
