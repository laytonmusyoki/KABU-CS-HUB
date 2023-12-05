from flask import Flask, render_template, request, redirect, url_for, flash,session,make_response
from flask_mysqldb import MySQL
from urllib.parse import quote
from io import BytesIO
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

# connection=pymysql.connect(
#     host='',
#     user='kabucshub',
#     password='kabucshub',
#     database='kabu_hub'
# )


app.config['MYSQL_HOST']="db4free.net"
app.config['MYSQL_USER']="kabucshub"
app.config['MYSQL_PASSWORD']="kabucshub"
app.config['MYSQL_DB']="kabucshub"
mysql=MySQL(app)


@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/sem1-1')
def sem1_1():
    semester="Semester1.1"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem1-1.html',notes=notes,papers=papers)


@app.route('/sem1-2')
def sem1_2():
    semester="Semester1.2"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem1-2.html',notes=notes,papers=papers)


@app.route('/sem2-1')
def sem2_1():
    semester="Semester2.1"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem2-1.html',notes=notes,papers=papers)


@app.route('/sem2-2')
def sem2_2():
    semester="Semester2.2"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem2-2.html',notes=notes,papers=papers)


@app.route('/sem3-1')
def sem3_1():
    semester="Semester3.1"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem3-1.html',notes=notes,papers=papers)


@app.route('/sem3-2')
def sem3_2():
    semester="Semester3.2"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem3-2.html',notes=notes,papers=papers)


@app.route('/sem4-1')
def sem4_1():
    semester="Semester4.1"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem4-1.html',notes=notes,papers=papers)


@app.route('/sem4-2')
def sem4_2():
    semester="Semester4.2"
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE semester=%s",(semester,))
    notes=cur.fetchall()
    cur.execute("SELECT * FROM papers WHERE semester=%s",(semester,))
    papers=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('sem4-2.html',notes=notes,papers=papers)

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
        

@app.route('/news')
def news():
    return render_template('check.html')


@app.route('/useful_links')
def useful_links():
    return render_template('useful_links.html')



@app.route('/admin_authorization',methods=['POST','GET'])
def admin_validation():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        code=request.form['code']
        if username=='' or password=='' or code=='':
            flash('All fields are required','danger')
            return render_template('validate.html')
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s AND auth_code=%s",(username,password,code))
        user=cur.fetchone()
        mysql.connection.commit()
        cur.close()
        if user is not None:
            session['username']=user[1]
            flash(f'Logged in as {username}','success')
            return redirect(url_for('notes'))
        else:
            flash('Wrong credentials','warning')
            return render_template('validate.html',username=username,password=password,code=code)
    return render_template('validate.html')



@app.route('/notes',methods=['POST','GET'])
def notes():
    if 'username' not in session:
        flash('Please you need to be authorized','warning')
        return redirect(url_for('index'))
    else:
        if request.method=='POST':
            semester=request.form['semester']
            code=request.form['code']
            file=request.files['pdf']
            cur=mysql.connection.cursor()
            cur.execute("INSERT INTO notes(semester,code,file_name,pdf) VALUES(%s,%s,%s,%s)",(semester,code,file.filename,file.read(),))
            mysql.connection.commit()
            cur.close()
            flash(f'{semester} {code} notes has been added','success')
            return redirect(url_for('index'))
        else:
            return render_template('notes.html')


@app.route('/papers',methods=['POST','GET'])
def papers():
    if 'username' not in session:
        flash('Please you need to be authorized','warning')
        return redirect(url_for('index'))
    else:
        if request.method=='POST':
            semester=request.form['semester']
            code=request.form['code']
            file=request.files['pdf']
            cur=mysql.connection.cursor()
            cur.execute("SELECT * FROM papers WHERE pdf=%s",(file))
            data=cur.fetchone()
            cur.execute("INSERT INTO papers(semester,code,file_name,pdf) VALUES(%s,%s,%s,%s)",(semester,code,file.filename,file.read(),))
            mysql.connection.commit()
            cur.close()
            print(semester)
            flash(f'{semester} {code} papers has been added','success')
            return redirect(url_for('index'))
        else:
            return render_template('papers.html')


@app.route('/download/<table>/<id>')
def download(table,id):
    cur=mysql.connection.cursor()
    if table=="notes":
        cur.execute("SELECT * FROM notes WHERE id=%s",(id))
        notes=cur.fetchone()
        mysql.connection.commit()
        cur.close()
        response=make_response(notes[4])
        response.headers['Content-Type']='application/pdf'
        response.headers['Content-Disposition']=f"attachment; filename='{notes[3]}'"
        return response
    else:
        cur.execute("SELECT * FROM papers WHERE id=%s",(id))
        papers=cur.fetchone()
        mysql.connection.commit()
        cur.close()
        response=make_response(papers[4])
        response.headers['Content-Type']='application/pdf'
        response.headers['Content-Disposition']=f"attachment; filename='{papers[3]}'"
        return response
    



@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
        flash('You have been logged out','warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)