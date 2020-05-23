from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def check():
    return render_template('index.html')

d = {'shanan': 'brother', 'ishu': 'brother', 'Sunita': 'mummy', 'nik':'wife'}
@app.route('/search', methods=['POST'])
def check2():
    checkr = request.form['checkr']
    the_results = d[checkr]
    return render_template('search.html', rcheck = checkr, the_results= the_results)

if __name__ == '__main__':
    app.run(debug = True)