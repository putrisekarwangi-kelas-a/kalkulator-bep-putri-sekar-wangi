from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_bep(biaya_tetap, harga_jual, biaya_variabel):
    nilai_margin_kontribusi = harga_jual - biaya_variabel

    if nilai_margin_kontribusi <= 0:
        return None

    return biaya_tetap / nilai_margin_kontribusi

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None

    biaya_tetap = ""
    harga_jual = ""
    biaya_variabel = ""
    tahun_produksi = ""

    if request.method == "POST":
        biaya_tetap = request.form["biaya_tetap"]
        harga_jual = request.form["harga_jual"]
        biaya_variabel = request.form["biaya_variabel"]
        tahun_produksi = request.form["tahun_produksi"]

        try:
            bt = float(biaya_tetap)
            hj = float(harga_jual)
            bv = float(biaya_variabel)
            tp = int(tahun_produksi)

            if bt < 0 or hj < 0 or bv < 0:
                error = "Input tidak boleh negatif."
            else:
                hasil = hitung_bep(bt, hj, bv)
                if hasil is None:
                    error = "Harga jual harus lebih besar dari biaya variabel."
        except ValueError:
            error = "Masukkan angka yang valid."

    return render_template(
        "index.html",
        hasil=hasil,
        error=error,
        biaya_tetap=biaya_tetap,
        harga_jual=harga_jual,
        biaya_variabel=biaya_variabel,
        tahun_produksi=tahun_produksi,
    )

if __name__ == "__main__":
    app.run(debug=True)