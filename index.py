from flask import Flask, render_template
from data import data
from flask import Flask, render_template,request,redirect
import datetime


app = Flask(__name__)


# добавлять в файл data.py

def get_data():
    with open('data.py', 'r', encoding="utf-8") as f:
        data = f.read()
    return data

def write_data(data):
    with open('data.py', 'w', encoding="utf-8") as f:
        f.write(data)

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/add_card', methods=['POST'])
def add_card(): 
    card = {}
    card['id'] = str(datetime.datetime.now())[-6:-1]
    card['wifiname'] = request.form['wifiname']
    card['wifispeed'] = request.form['wifispeed']
    card['wifidelay'] = request.form['wifidelay']
    card['wifipricemonth'] = request.form['wifipricemonth']
    card['wifimaxusers'] = request.form['wifimaxusers']

    # код который распаковывает картинку
    data.append(card)
    write_data(f"data = {data}")
    return redirect('/')

@app.route('/admin')
def admin():
    return render_template('admin.html', data=data)

@app.route('/delete_card', methods=['POST'])
def delete_card():
    id = request.form['id']
    for card in data:
        print(str(id))
        if str(card['id']) == str(id):
            data.remove(card)
    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
