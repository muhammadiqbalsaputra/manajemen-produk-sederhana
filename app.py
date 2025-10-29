# app.py
from flask import Flask
from database import db  # Impor db dari file database.py

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi koneksi ke database MySQL di XAMPP
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/latihan_controller_view'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Hubungkan objek db dengan aplikasi Flask
db.init_app(app)

# Impor dan daftarkan blueprint dari controller
# Impor ini sekarang aman dilakukan di sini
from controllers.product_controller import product_bp
app.register_blueprint(product_bp)

# Buat tabel di database jika belum ada
with app.app_context():
    db.create_all()

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)