from flask import Flask, render_template
from models import get_all_items

app = Flask(__name__)

@app.route('/')
def index():
    data = get_all_items()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
