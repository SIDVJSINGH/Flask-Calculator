from flask import Flask, render_template, request, redirect, jsonify
from application import app, mongo
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json('data') # object received from frontend
        try:
            expression = data['expression'] # expression from data object
            result = data['result'] # result from data object
            user = data['user'] # user from data object
            
            # Create a new collection for each user (if it doesn't exist)
            user_collection = mongo.db[user]
            
            user_collection.insert_one({"expression": expression,
                            "result": result,
                            "user": user,
                       "date": datetime.now()})

            return jsonify({'message': 'Data saved successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 418
        
    return render_template('home.html')

# @app.route('/history', methods=['GET'])
# def history():
#     history = list(user_collection.find({'user'==user}))
#     return render_template('history.html', history=history)