from flask import Flask, render_template, redirect, request
from forms import SignUpForm
from healthcheck import HealthCheck
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thecodex'

#health = HealthCheck(app, "/healthcheck")
@app.route('/healthcheck')
def health():
    return str(200)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/blog')
def blog():
    return render_template('blog.html', author = "Bob")

@app.route('/signup/<signup_name>')
def signupname(signup_name):
    return 'This blog is for '+ str(signup_name) 

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)

