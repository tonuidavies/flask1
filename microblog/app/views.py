from app import app,render_template, redirect, url_for, request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
app.route('/login',methods=['GET','POST'])
def login():
    error=none
    if request=='POST':
        if request.form['username'] !='admin' or request.form['password'] !='admin':
            error= 'Please enter correct name or password'
            else:
                return redirect(url_for('home'))
    return render_template ('login.html', error=error)
 