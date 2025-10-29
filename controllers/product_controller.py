# controllers/product_controller.py
from flask import Blueprint, render_template, request, redirect, url_for
from models.product import Product
from database import db  # <-- Perubahan di sini

# Membuat Blueprint
product_bp = Blueprint('product', __name__)

# Route untuk halaman utama (Read)
@product_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Route untuk menambah produk baru (Create)
@product_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_product = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=float(request.form['price']),
            qty=int(request.form['qty'])
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('product.index'))
    return render_template('add_product.html')

# Route untuk mengedit produk (Update)
@product_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.qty = int(request.form['qty'])
        db.session.commit()
        return redirect(url_for('product.index'))
    return render_template('edit_product.html', product=product)

# Route untuk menghapus produk (Delete)
@product_bp.route('/delete/<int:id>')
def delete(id):
    product_to_delete = Product.query.get_or_404(id)
    db.session.delete(product_to_delete)
    db.session.commit()
    return redirect(url_for('product.index'))