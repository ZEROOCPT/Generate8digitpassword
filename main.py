from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def awalan():
    awal = '''<h1> Selamat datang <h1>
     <a href="/random_pass">Generate 8 digit password:</a>'''
    return awal


@app.route("/random_pass")
def gen_pass():
    elements = "abcdklmnopqz+-/*!&efghij$#?=@rstuvwxy<>"
    password = ""

    for i in range(8):
        password += random.choice(elements)

    return password
app.run(debug=True)