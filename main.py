from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Selamat datang di Kalkulator Web Milik Mara Hahaha 🚀"

@app.route("/tambah")
def tambah():
    a = request.args.get("a", default=0, type=int)
    b = request.args.get("b", default=0, type=int)
    return f"Hasil {a} + {b} = {a+b}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
