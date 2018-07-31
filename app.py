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
        finalDates = data['date_val'].replace('/', '-')
        print(finalDates)
        splitDates = finalDates.split("; ")

        for selectedDates in splitDates:
            print(selectedDates)
        return jsonify({'success': "added date"})

    elif request.method == 'GET':
        return render_template('calendar.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
    app.run()