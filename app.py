from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1>Hay, {name}! Selamat datang!</h1>'

@app.route('/user_login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        user = request.form['username']  # Mengambil data dari form POST
        return redirect(url_for('welcome', name=user))
    else:
        return render_template('login.html')  # Jika GET, kembali ke halaman login

@app.route('/')
def home():
    return render_template('login.html')  # Halaman awal menampilkan form login

if __name__ == '__main__':
    app.run(debug=True)
