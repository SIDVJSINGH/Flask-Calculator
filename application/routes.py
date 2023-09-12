from flask import Flask, render_template, request, redirect
from application import app, db

import sqlite3


@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    result = eval(expression)

    # Save the calculation to the database
    save_calculation(expression, result)

    return render_template('calculator.html', result=result)

def save_calculation(expression, result):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS calculations (id INTEGER PRIMARY KEY, expression TEXT, result REAL)")

    cursor.execute("INSERT INTO calculations (expression, result) VALUES (?, ?)", (expression, result))

    conn.commit()
    conn.close()

# You can see history here
@app.route('/history')
def history():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("SELECT expression, result FROM calculations ORDER BY id DESC")
    history = cursor.fetchall()
    conn.close()
    return render_template('history.html', history=history)

#For Cleariing History         
@app.route('/clear-history', methods=['POST'])
def clear_history():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM calculations")
    conn.commit()
    conn.close()
    return redirect('/history')
