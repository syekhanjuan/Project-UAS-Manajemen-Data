# Project-UAS-Manajemen-Data

<div align="center">
  <img src="https://img.shields.io/badge/OS-Linux%20(WSL)-orange?style=flat-square&logo=linux" alt="Linux">
  <img src="https://img.shields.io/badge/Container-Docker-blue?style=flat-square&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/Language-Python%20%2B%20Bash-yellow?style=flat-square&logo=python" alt="Python & Bash">
  <img src="https://img.shields.io/badge/Framework-Flask%20%2B%20Pandas-lightgrey?style=flat-square" alt="Flask & Pandas">
</div>

---

## 👨‍🎓 Identitas
* **Nama** : Syekhan Maula Juantana
* **NRP** : 3325600065
* **Program Studi** : Sains Data Terapan
* **Institusi** : Politeknik Elektronika Negeri Surabaya (PENS)

---

## 📋 Deskripsi Proyek
Repositori ini merupakan dokumentasi komprehensif dari pengerjaan Ujian Akhir Semester (UAS). Proyek ini dibagi menjadi dua bagian utama yang mencakup kompetensi **Administrasi Sistem Linux** dan **Virtualisasi menggunakan Docker Container**. 

Seluruh *script* dan konfigurasi telah diuji dan beroperasi penuh secara lokal pada ekosistem *Windows Subsystem for Linux (WSL)* distribusi Ubuntu.

---

## 📁 Struktur Repositori & Penjelasan Teknis

### 🛠️ Bagian 1: Otomatisasi Administrasi Sistem Linux (`/Tugas_1`)
Direktori ini memuat instrumen Bash *scripting* untuk mengotomatisasi tugas-tugas *System Administrator*:

1. **Manajemen User (`buat_user.sh`)**
   * Program perulangan (*looping*) otomatis untuk membaca daftar nama dari file teks (`daftar_user.txt`) dan mengintegrasikannya ke dalam sistem menggunakan perintah `useradd`.
   * Dilengkapi dengan fitur validasi eksistensi *user* dan penyetelan *password* masal menggunakan format `namauser@123` via `chpasswd`.
2. **Monitoring Storage (`cek_hdd.sh`)**
   * *Script* pemantauan yang mengombinasikan `df`, `awk`, dan `sed` untuk mengekstraksi parameter persentase ruang partisi utama, lalu mengkalkulasi rasio *free space* sisa penyimpanan dalam bentuk notifikasi dinamis.
3. **Penjadwalan Backup Otomatis (`cron_schedule.txt`)**
   * Ekstraksi konfigurasi *daemon* `crontab`. Sistem sukses dijadwalkan untuk mengeksekusi kompresi arsip (Tarball `.tar.gz`) dari direktori `/etc` dan menyimpannya ke dalam partisi disk *loopback* 50MB di direktori `/backup` secara periodik (setiap tanggal 9 dan setiap hari Kamis).

### 🐳 Bagian 2: Virtualisasi Container & Analisis Data (`/Tugas_2`)
Direktori ini berisi implementasi *microservice* aplikasi analisis data yang sepenuhnya dikontainerisasi:

* **Sistem Analisa Nilai Akademik**: Sebuah *dashboard* analitik berbasis *web* untuk memantau performa kelas.
* **Logika Data**: Mengutilisasi *library* **Pandas** untuk melakukan komputasi statistik atas *dataset* (`data_mahasiswa.csv`), termasuk menghitung persentase nilai (Tugas, UTS, UAS), rata-rata kelas, hingga agregasi nilai tertinggi/terendah.
* **Web Server & Tampilan**: Disajikan melalui protokol HTTP menggunakan *framework* **Flask**. Antarmuka dibangun menggunakan kombinasi *CSS Bootstrap 5* untuk kerangka responsif dan *Chart.js* untuk render visualisasi *bar chart* interaktif.
* **Isolasi Lingkungan (`Dockerfile`)**: Lingkungan operasi terisolasi menggunakan *base image* Python yang ringan, mencakup perintah instalasi dependensi (`requirements.txt`) secara otomatis.

---

## ⚙️ Petunjuk Menjalankan Aplikasi (Tugas 2)
Untuk mereplikasi *environment* dan melakukan inisiasi *dashboard* analisa data melalui Docker, eksekusi perintah berikut di lingkungan terminal Linux/WSL:

```bash
# 1. Masuk ke direktori aplikasi
cd Tugas_2

# 2. Build image Docker
docker build -t analisa-uas .

# 3. Eksekusi dan jalankan Container (Detached Mode)
docker run -d -p 8080:5000 --name dashboard-uas analisa-uas
