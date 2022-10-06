from flask import Flask, render_template, request
from db import parseCSV, compare

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    categories = parseCSV()[0]
    countries = parseCSV()[1]
    if request.method == "POST":
        '''
        matches = []
        for match in range(1): #number of matches
            matches.append(request.form.get(str(match)))
        '''
        match = request.form.get("matchOne")
        print(match)
        #result = compare(match)


    return render_template("main.html",
                           title='Tourney',
                           heading = 'Tourney',
                           categories = categories,
                           countries = countries)

if __name__ == '__main__':
    app.run()
