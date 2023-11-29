from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key='futfygkbkjbkbdlkeougxx'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='laytonmatheka7@gmail.com'
app.config['MAIL_PASSWORD']='qamfnggyldkpbhje'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

mail = Mail(app)


@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/sem1-1')
def sem1_1():
    return render_template('sem1-1.html')


@app.route('/sem1-2')
def sem1_2():
    return render_template('sem1-2.html')


@app.route('/sem2-1')
def sem2_1():
    return render_template('sem2-1.html')


@app.route('/sem2-2')
def sem2_2():
    return render_template('sem2-2.html')


@app.route('/sem3-1')
def sem3_1():
    return render_template('sem3-1.html')


@app.route('/sem3-2')
def sem3_2():
    return render_template('sem3-2.html')


@app.route('/sem4-1')
def sem4_1():
    return render_template('sem4-1.html')


@app.route('/sem4-2')
def sem4_2():
    return render_template('sem4-2.html')

@app.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        description = request.form['description']
        html_content = render_template('response.html', name=name, email=email, description=description)
        try:
            msg = Message(subject=subject, sender = email, html=html_content, recipients= ['laytonmatheka7@gmail.com'])
            mail.send(msg)
            flash(f"Thanks {name} your message has been send Successfully",'success')
            return redirect(url_for('index'))
        except Exception as error:
            flash("Mail not sent please check your internet",'danger')
            return redirect(url_for('index'))
        


if __name__ == '__main__':
    app.run(debug=True)