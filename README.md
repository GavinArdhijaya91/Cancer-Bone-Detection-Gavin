🦴 BoneScan AI: Osteosarcoma Detection System
BoneScan AI adalah sistem berbasis Deep Learning yang dirancang untuk mendeteksi potensi kanker tulang (Osteosarcoma) melalui citra X-Ray. Menggunakan arsitektur ResNet50, sistem ini mampu mengenali pola anomali pada kepadatan tulang dengan tingkat presisi yang lebih tinggi dibandingkan model CNN standar.

🚀 Panduan Instalasi
Ikuti langkah-langkah berikut untuk menjalankan proyek di lingkungan lokal Anda:

1. Persiapan Environment
Pertama, buat dan aktifkan virtual environment agar library tidak bentrok dengan sistem utama.
_______________________________

# Membuat virtual environment
python -m venv venv_media

# Mengaktifkan venv
# Windows:
venv_media\Scripts\activate
# Mac/Linux:
source venv_media/bin/activate
_______________________________

Lalu install library-nya

# Menginstall
pip install flask tensorflow numpy opencv-python
# Note: Library os adalah bawaan Python, jadi Anda tidak perlu untuk menginstall ulang.
________________________________

3. Struktur Folder
Pastikan struktur folder Anda terlihat seperti ini:

Plaintext
Project/
├── app.py              # Logic Flask & AI
|___training.py         # Training Data untuk model
├── model_bone.h5       # File Model (.H5)
├── static/
│   ├── uploads/        # Folder foto yang masuk
│   └── outputs/        # Folder hasil kotak merah
└── templates/
    └── frontend.html   # Tampilan Web

(Untuk nama folder dikreasikan sendiri tidak papa, hanya saja Anda perlu mengubah path folder pada app.py)

___________________________________

4. Cara Menjalankan
- Buka Terminal di VSCODE/berbagai IDE, yang berada di folder proyek Anda
- Pastikan 'venv_media' sudah aktif
- Lakukan pengetikan pada Terminal seperti ini:
python app.py

# Buka browser dan akses: http://localhost:5000 atau http://IP_LAPTOP:5000 (untuk akses via HP).

____________________________________

⚠️ Peraturan & Kebijakan Penggunaan
Sistem ini memiliki batasan untuk bisa dijalankan programnya.
Di antaranya adalah:

1. Format File
Anda hanya boleh mengupload file dengan format (.JPG, .PNG, dan .JPEG).
Selain itu, Anda tidak bisa mengupload bahkan dianalisis.

2. Kategori Foto
Anda hanya boleh mengupload foto berupa hasil rontgen dengan menggunakan alat x-ray, jika Anda mengupload foto dengan kategori selain yang disebutkan tadi, maka foto tersebut tidak dapat dinyatakan valid untuk dianalisis.

3. Nama File
Usahakan nama file yang mau dianalisis tidak mengandung spasi (contoh: rontgen punggung.jpg), karena hal tersebut akan menyebabkan error dan tidak bisa diproses.
Untuk jalan alternatifnya, Anda bisa menambahkan simbol di sela-sela suatu nama file (contoh: "_" atau "-") sebagai pemisah antara satu kata dengan yang lain (contoh: rontgen_punggung.jpg).

`DISCLAIMER`
`Program ini hanyalah sebagai acuan untuk memprediksi apakah orang tersebut berpotensi terkena kanker tulang atau tidak, jadi tidak ada suatu keputusan mutlak yang dihasilkan dari proses analisis program ini. Dengan demikian, ketika hasil dari program ini menyatakan bahwa tulang Anda terdeteksi kanker karena adanya area yang mencurigakan, konsultasikan hal ini lebih lanjut ke dokter spesialis untuk dianalisis lebih lanjut terkait kebenarannya.`

🙏 THANK YOU 🙏