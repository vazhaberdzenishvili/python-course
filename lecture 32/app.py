from flask import Flask, render_template, request, redirect, url_for
from models import db, Car

app = Flask(__name__)

host = 'localhost'
port = '5432'
user = 'postgres'
password = '12345678'
database = 'flask'

app.secret_key = 'SecretApp'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{
    user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    all_data = Car.query.all()

    return render_template('index.html', cars=all_data)


@app.route('/insert', methods=['GET', 'POST'])
def insert():

    if request.method == 'POST':
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        car = Car(manufacturer, model, instock, price)

        db.session.add(car)
        db.session.commit()

        return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):

    car = Car.query.get(id)

    if car:
        car.manufacturer = request.form['manufacturer']
        car.model = request.form['model']
        car.instock = request.form['instock']
        car.price = request.form['price']

        db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_car(id):
    car = Car.query.get(id)

    db.session.delete(car)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
