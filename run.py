from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfXC-MZAAAAAPO3actwmSr-YcgHZAuX4Ww0JRL1'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfXC-MZAAAAANGEuGE9UQJjCVbn5N66vOtpqAYg'
app.config['TESTING'] = True


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required'), Length(min=5, max=10, message='Must be from 5 to 10 symbol')])
    password = PasswordField('password', validators=[InputRequired('Password is required'), AnyOf(values=['password', 'secret'])])
    recaptcha = RecaptchaField()


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/hobby')
def hobby():
    return render_template("hobby.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>The username is {}. The password is {}.'.format(form.username.date, form.password.data)
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)