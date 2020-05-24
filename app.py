<<<<<<< HEAD
from flask import Flask, render_template, jsonify

from scrape import scrape

from database import getLatest, update



# Create an instance of our Flask app.
app = Flask(__name__)

#update()
#index
@app.route('/')
def index():
    # call to database to get latest data
    data = getLatest()
    return render_template('index.html', data = data )

@app.route('/update')
def updateMe():

    # call to database.py to update data
    update()

    return index()

#run the app
if __name__ == '__main__':
=======
from flask import Flask, render_template, jsonify

from scrape import scrape

from database import getLatest, update



# Create an instance of our Flask app.
app = Flask(__name__)

#update()
#index
@app.route('/')
def index():
    # call to database to get latest data
    data = getLatest()
    return render_template('index.html', data = data )

@app.route('/update')
def updateMe():

    # call to database.py to update data
    update()

    return index()

#run the app
if __name__ == '__main__':
>>>>>>> 2251c79e3f08eddc4e5b4faace0417255cc6f6af
    app.run(debug=True)