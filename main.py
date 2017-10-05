from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['passwordverify']
    if len(username) < 3 or len(username) > 20:
        nameerror = "<p class='error'>Please choose a username between 3 and 20 characters.</p>"
        return render_template('login.html') + nameerror
    for character in username:
        if character == " ":
            nameerror = "<p class='error'>Your username cannot contain any spaces.</p>"
            return render_template('login.html') + nameerror
    if (not password) or (password.strip() == ""):
        nopwerror = "<p class='error'>Please enter a password.</p>"
        return render_template('login.html') + nopwerror
    if password != verifypassword:
        pwerror = "<p class='error'>Your passwords do not match.</p>"
        return render_template('login.html') + pwerror
    return render_template('welcome.html', username=username)



@app.route('/')
def index():
    usererror = request.args.get("nameerror")
    nopasserror = request.args.get("nopwerror")
    passerror = request.args.get("pwerror")
    return render_template('login.html',
    usererror=usererror and cgi.escape(usererror, quote=True), 
    nopasserror=nopasserror and cgi.escape(nopasserror, quote=True), 
    passerror=passerror and cgi.escape(passerror, quote=True))

app.run()