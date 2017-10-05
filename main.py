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
        nameerror = "Please choose a username between 3 and 20 characters."
        return render_template('login.html', usererror=nameerror)
    for character in username:
        if character == " ":
            nameerror = "Your username cannot contain any spaces."
            return render_template('login.html', usererror=nameerror)
    if (not password) or (password.strip() == ""):
        nopwerror = "Please enter a password."
        return render_template('login.html', nopasserror=nopwerror)
    if password != verifypassword:
        pwerror = "Your passwords do not match."
        return render_template('login.html', passerror=pwerror)
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