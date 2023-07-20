from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        greeting = f"Hello, {name}! Welcome to My Flask App!"
        return render_template('BOOTSTRAP CODE.html', greeting=greeting)
    return render_template('BOOTSTRAP CODE.html', greeting=None)

if __name__ == '__main__':
    app.run(debug=False,port=8000)
