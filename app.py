from flask import Flask, url_for, redirect, request, render_template, jsonify

app = Flask(__name__)

@app.route('/dinner', methods=['GET','POST'])
def dinner_selection():
    if request.method == 'POST':
        data = request.get_json()
        mtkid = data['mtkid']
        processed_text = mtkid.upper()
        print(processed_text)
        print(data['date_val'])
        dates = data['date_val'].split(";")
        for selectedDates in dates:
            print(selectedDates)
        return jsonify({'success': "added date"})
    elif request.method == 'GET':
        return render_template('calendar.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# from flask import Flask, render_template, request
# from datetime import date
# import tkinter
# from tkinter import messagebox
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return render_template('home.html')
#
# @app.route('/', methods=['POST'])
# def login():
#     x = set()
#     a = []
#     mtkid = request.form['mtkid']
#     print(mtkid)
#     processed_text = mtkid.upper()
#     today = str(date.today())
#     print(today)
#     f = open(today, "a+")
#     f.write(mtkid + "\n")
#     f.close()
#     return ('Thank you for choosing the dates!')
#
# if __name__=='__main__':
#     app.run()