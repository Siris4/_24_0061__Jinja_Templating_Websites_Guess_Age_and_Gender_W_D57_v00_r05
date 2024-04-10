
from flask import Flask, render_template
import random
import datetime as dt
import requests


app = Flask(__name__)

@app.route('/guess/<name>')  #we need to parse the name, so we would add angled brackets
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    print("Gender Data:", gender_data)  # prints gender data for debugging

    gender = gender_data['gender']

    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data = age_response.json()
    print("Age Data:", age_data)  # prints age data for debugging

    age = age_data['age']

    this_year = dt.datetime.now().year
    MY_NAME = "Gavin M."
    return render_template('guess_05_W_.html', person_name=name.title(),
                           guess_users_gender=f'I think you are {gender},',
                           guess_users_age=f'and perhaps you are {age} years old.',
                           CURRENT_YEAR=f'Copyright {this_year} - Built by {MY_NAME}')

if __name__ == "__main__":
    app.run(debug=True)