from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Kalkulator Web</title>
</head>
<body>
    <h2>Kalkulator Web</h2>
    <form method="post">
        <input type="text" name="angka1" placeholder="Angka 1"><br><br>
        <input type="text" name="angka2" placeholder="Angka 2"><br><br>
        <select name="op">
            <option value="+">Tambah</option>
            <option value="-">Kurang</option>
            <option value="*">Kali</option>
            <option value="/">Bagi</option>
        </select><br><br>
        <button type="submit">Hitung</button>
    </form>
    {% if hasil is not none %}
        <h3>Hasil: {{ hasil }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def kalkulator():
    hasil = None
    if request.method == "POST":
        try:
            a = float(request.form["angka1"])
            b = float(request.form["angka2"])
            op = request.form["op"]

            if op == "+":
                hasil = a + b
            elif op == "-":
                hasil = a - b
            elif op == "*":
                hasil = a * b
            elif op == "/":
                hasil = "Error (bagi 0)" if b == 0 else a / b
        except:
            hasil = "Input tidak valid!"
    return render_template_string(html, hasil=hasil)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

