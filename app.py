#Campus Lost & Found
#Created by Keya Sen , Computer Science, May 2026 
#Institution : New Alipore College 
#This code was developed for coursework. Do not redistribute or submit as your own work.
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lost', methods=['GET', 'POST'])
def lost():
    submitted = False
    
    if request.method == 'POST':
        student_name = request.form['student_name']
        roll_number = request.form['roll_number']
        item_name = request.form['item_name']
        category_name = request.form['category_name']
        last_seen = request.form['last_seen']
        date_lost = request.form['date_lost']
        description = request.form['description']
        contact_number = request.form['contact_number']

        print("---- NEW LOST ITEM REPORT ----")
        print("Name:", student_name)
        print("Roll No:", roll_number)
        print("Item:", item_name)
        print("Category:", category_name)
        print("Last Seen:", last_seen)
        print("Date Lost:", date_lost)
        print("Description:", description)
        print("Contact:", contact_number)
        print("------------------------------")
        
        submitted = True

    return render_template('report_lost.html', submitted=submitted)

@app.route('/found', methods=['GET', 'POST'])
def found():
    submitted = False
    
    if request.method == 'POST':
        student_name = request.form['student_name']
        roll_number = request.form['roll_number']
        item_name = request.form['item_name']
        category_name = request.form['category_name']
        last_seen = request.form['last_seen']
        date_lost = request.form['date_lost']
        description = request.form['description']
        item_now = request.form['item_now']
        contact_number = request.form['contact_number']

        print("---- NEW FOUND ITEM REPORT ----")
        print("Name:", student_name)
        print("Roll No:", roll_number)
        print("Item:", item_name)
        print("Category:", category_name)
        print("Last Seen:", last_seen)
        print("Date Lost:", date_lost)
        print("Description:", description)
        print("Item now:", item_now)
        print("Contact:", contact_number)
        print("------------------------------")
        
        submitted = True

    return render_template('report_found.html', submitted=submitted)

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
