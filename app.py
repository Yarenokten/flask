from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yaren')
def i_index():
    user_name = "yaren"
    return render_template('index.html', name=user_name)

@app.route('/deneme')
def ansayfa():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
