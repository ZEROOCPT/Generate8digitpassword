from flask import Flask
import random
app = Flask(__name__)

@app.route("/")

def awalan():
    awal = '''<h1> Selamat datang <h1>
     <a href="/random_fact">View a random fact!</a>
    <a href="/random_pass">View a random password!</a>'''
    return awal


@app.route("/random_fact")
def fakta_fakta():
    fakta =  ["Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka","Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50 persen orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.","Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan","Menurut sebuah studi tahun 2019, lebih dari 60persen orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja",]
    return f'<p>{random.choice(fakta)}</p>'

@app.route("/random_pass")
def gen_pass():
    elements = "abcdklmnopqz+-/*!&efghij$#?=@rstuvwxy<>"
    password = ""

    for i in range(8):
        password += random.choice(elements)
    return password

app.run(debug=True)
