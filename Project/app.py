from flask import Flask, render_template, request
from autocorrector import correct_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected = ""
    if request.method == 'POST':
        user_input = request.form['text']
        corrected = correct_text(user_input)
    return render_template('index.html', corrected=corrected)

if __name__ == '__main__':
    app.run(debug=True)





