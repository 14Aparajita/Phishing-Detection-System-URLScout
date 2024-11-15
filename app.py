from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from API import get_prediction
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


app = Flask(__name__)
app.config['SECRET_KEY'] = '080e6cbaf658085222c3b95c1f7e16d31b02835503af140b'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'url_prediction'

mysql = MySQL(app)

# path to trained model
model_path = r"path to file\Malicious_URL_Prediction.h5"

# Flask-WTF forms
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

class ReportForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Report URL')

# Landing Page Route
@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if username already exists
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', [username])
        user = cur.fetchone()

        if user:
            flash('Username already exists. Please choose a different username.')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            cur.execute('INSERT INTO users (username, password, email, phone) VALUES (%s, %s, %s, %s)', 
                        (username, hashed_password, form.email.data, form.phone.data))
            mysql.connection.commit()
            cur.close()
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

# User Authentication Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', [username])
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[2], password):  # user[2] is the hashed password
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('enter_url'))
        else:
            flash('Login failed. Check your username and/or password.')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('landing'))

# Main Routes
@app.route('/enter_url', methods=['GET', 'POST'])
def enter_url():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    form = ReportForm()
    if form.validate_on_submit():
        url = form.url.data
        return redirect(url_for('show_prediction', url=url))
    print(form.errors)
    return render_template('enter_url.html', form=form)

@app.route('/prediction')
def show_prediction():
    url = request.args.get('url')
    prediction = None
    if url:
        prediction = get_prediction(url, model_path)
    return render_template('show_prediction.html', prediction=prediction, url=url)

# Contact Page Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        
        # Save contact query to the database
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contact_queries (name, email, message) VALUES (%s, %s, %s)', 
                    (name, email, message))
        mysql.connection.commit()
        cur.close()
        
        flash('Message sent successfully!')
        return redirect(url_for('landing'))
    return render_template('contact.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/report', methods=['POST'])
def report():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    url = request.form['url']
    prediction = get_prediction(url, model_path)
    if prediction > 65:
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO reported_urls (url, prediction_percentage) VALUES (%s, %s)', (url, prediction))
        mysql.connection.commit()
        cur.close()
        flash('URL reported successfully!')
    else:
        flash('URL prediction percentage is too low to report.')
        
    return redirect(url_for('enter_url'))

if __name__ == '__main__':
    app.run(debug=True)
