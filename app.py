from flask import Flask, request, render_template

app = Flask(__name__)

data_penyakit = {
    "flu": {
        "gejala": ["demam", "batuk", "menggigil", "sakit kepala", "nyeri otot"],
        "diagnosis": "Anda mungkin terkena flu."
    },
    "infeksi tenggorokan": {
        "gejala": ["demam", "sakit tenggorokan", "kesulitan menelan", "pembengkakan kelenjar"],
        "diagnosis": "Anda mungkin mengalami infeksi tenggorokan."
    },
    "demam berdarah": {
        "gejala": ["demam tinggi", "ruam", "nyeri sendi", "mual", "darah dalam muntahan"],
        "diagnosis": "Anda mungkin mengalami demam berdarah."
    },
    "flu biasa": {
        "gejala": ["batuk", "pilek", "sakit tenggorokan", "kelesuan", "nyeri otot"],
        "diagnosis": "Anda mungkin terkena flu biasa."
    },
    "COVID-19": {
        "gejala": ["demam", "batuk kering", "kelelahan", "hilangnya indera penciuman", "sesak napas"],
        "diagnosis": "Anda mungkin terinfeksi COVID-19."
    },
    "radang paru-paru": {
        "gejala": ["demam", "batuk", "sesak napas", "nyeri dada", "kehilangan nafsu makan"],
        "diagnosis": "Anda mungkin mengalami radang paru-paru."
    },
    "alergi": {
        "gejala": ["bersin", "gatal-gatal", "mata berair", "sesak napas"],
        "diagnosis": "Anda mungkin mengalami alergi."
    },
    "gastroenteritis": {
        "gejala": ["mual", "muntah", "diare", "kram perut", "demam"],
        "diagnosis": "Anda mungkin mengalami gastroenteritis."
    },
    "tuberkulosis": {
        "gejala": ["batuk berdarah", "demam", "berat badan menurun", "malam berkeringat"],
        "diagnosis": "Anda mungkin menderita tuberkulosis."
    },
    "infeksi saluran kemih": {
        "gejala": ["nyeri saat berkemih", "sering berkemih", "darah dalam urine"],
        "diagnosis": "Anda mungkin mengalami infeksi saluran kemih."
    },
    "hipertensi": {
        "gejala": ["sakit kepala", "nyeri dada", "pusing", "penglihatan kabur"],
        "diagnosis": "Anda mungkin menderita hipertensi."
    },
}

def backward_chaining(gejala):
    diagnosis_terbaik = None
    jumlah_gejala_terbaik = 0

    for penyakit, detail in data_penyakit.items():
        jumlah_gejala_cocok = sum(g in gejala for g in detail["gejala"])
        if jumlah_gejala_cocok > jumlah_gejala_terbaik:
            diagnosis_terbaik = detail["diagnosis"]
            jumlah_gejala_terbaik = jumlah_gejala_cocok

    if diagnosis_terbaik:
        return diagnosis_terbaik
    return "Diagnosis tidak ditemukan."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def diagnose():
    symptoms_input = request.form.get('symptoms', '')
    gejala = [s.strip() for s in symptoms_input.split(',')]  
    diagnosis = backward_chaining(gejala)
    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True, port=5001)