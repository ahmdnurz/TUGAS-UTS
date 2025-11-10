from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER_NAMA = "AHMAD NUR YULHAIDIR"
USER_NIM = "TEKOM E | 250210502030"

data_hasil = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bangun = request.form['bangun']
        return redirect(url_for('hitung', bangun=bangun))
    return render_template('index.html', nama=USER_NAMA, nim=USER_NIM)

@app.route('/hitung/<bangun>', methods=['GET', 'POST'])
def hitung(bangun):
    if request.method == 'POST':
        hasil = None
        data_input = {}

        if bangun == 'Balok':
            p = float(request.form['p']); l = float(request.form['l']); t = float(request.form['t'])
            hasil = p * l * t; data_input = {'Panjang': p, 'Lebar': l, 'Tinggi': t}
        elif bangun == 'Kubus':
            s = float(request.form['s'])
            hasil = s ** 3; data_input = {'Sisi': s}
        elif bangun == 'Tabung':
            r = float(request.form['r']); t = float(request.form['t'])
            hasil = 3.14 * r**2 * t; data_input = {'Jari-jari': r, 'Tinggi': t}
        elif bangun == 'Kerucut':
            r = float(request.form['r']); t = float(request.form['t'])
            hasil = (1/3) * 3.14 * r**2 * t; data_input = {'Jari-jari': r, 'Tinggi': t}
        elif bangun == 'Bola':
            r = float(request.form['r'])
            hasil = (4/3) * 3.14 * r**3; data_input = {'Jari-jari': r}
        elif bangun == 'Limas Segiempat':
            p = float(request.form['p']); l = float(request.form['l']); t = float(request.form['t'])
            hasil = (1/3) * p * l * t; data_input = {'Panjang alas': p, 'Lebar alas': l, 'Tinggi': t}

        data_hasil.append({
            'nama': USER_NAMA,
            'nim': USER_NIM,
            'bangun': bangun,
            'input': data_input,
            'volume': round(hasil, 2)
        })
        return redirect(url_for('hasil'))

    return render_template('hitung.html', bangun=bangun)

@app.route('/hasil')
def hasil():
    return render_template('hasil.html', hasil=data_hasil)

if __name__ == '__main__':
    app.run(debug=True)
