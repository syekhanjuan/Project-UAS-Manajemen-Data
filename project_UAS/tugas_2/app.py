from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def analisa():
    # Membaca data CSV
    df = pd.read_csv('data_mahasiswa.csv')
    
    # Perhitungan Nilai Akhir
    df['Nilai_Akhir'] = (df['Tugas'] * 0.3) + (df['UTS'] * 0.3) + (df['UAS'] * 0.4)
    
    # Statistik untuk Dashboard
    rata_rata = round(df['Nilai_Akhir'].mean(), 2)
    nilai_max = round(df['Nilai_Akhir'].max(), 2)
    nilai_min = round(df['Nilai_Akhir'].min(), 2)
    total_mhs = len(df)

    # Menyiapkan data untuk Grafik (Chart.js)
    labels = df['Nama'].tolist()
    data_grafik = df['Nilai_Akhir'].tolist()

    # Template HTML dengan Bootstrap 5 & Chart.js
    html_template = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>UAS - Dashboard Analisa Nilai</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { background-color: #f4f7f6; }
            .card { border: none; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .header-section { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 40px 0; border-bottom-left-radius: 30px; border-bottom-right-radius: 30px; margin-bottom: 30px; }
        </style>
    </head>
    <body>

    <div class="header-section text-center">
        <h1>SISTEM ANALISA NILAI MAHASISWA</h1>
        <p>Project UAS - Virtualisasi & Docker Container</p>
    </div>

    <div class="container">
        <div class="row text-center mb-4">
            <div class="col-md-3">
                <div class="card p-3 bg-primary text-white">
                    <h5>Rata-rata Kelas</h5>
                    <h2>{{ rata_rata }}</h2>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card p-3 bg-success text-white">
                    <h5>Nilai Tertinggi</h5>
                    <h2>{{ nilai_max }}</h2>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card p-3 bg-warning text-dark">
                    <h5>Nilai Terendah</h5>
                    <h2>{{ nilai_min }}</h2>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card p-3 bg-info text-white">
                    <h5>Total Mahasiswa</h5>
                    <h2>{{ total_mhs }}</h2>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-md-7 mb-4">
                <div class="card p-4">
                    <h4 class="mb-3">Visualisasi Nilai Akhir</h4>
                    <canvas id="myChart"></canvas>
                </div>
            </div>

            <div class="col-md-5 mb-4">
                <div class="card p-4">
                    <h4 class="mb-3">Detail Nilai</h4>
                    <div class="table-responsive">
                        {{ table_html | safe }}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('myChart');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: {{ labels | safe }},
                datasets: [{
                    label: 'Nilai Akhir Mahasiswa',
                    data: {{ data_grafik | safe }},
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: { y: { beginAtZero: true, max: 100 } }
            }
        });
    </script>
    </body>
    </html>
    """
    
    return render_template_string(
        html_template, 
        rata_rata=rata_rata, 
        nilai_max=nilai_max, 
        nilai_min=nilai_min, 
        total_mhs=total_mhs,
        labels=labels,
        data_grafik=data_grafik,
        table_html=df.to_html(classes='table table-hover table-striped', index=False)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
