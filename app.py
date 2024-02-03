from flask import Flask, render_template
from roadmap_data import roadmap  # Import the roadmap data
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():

    current_year = datetime.now().year
    # Convert each links array to a JSON string for each item
    for category, items in roadmap.items():
        for item, links in items.items():
            items[item] = json.dumps(links)  # Convert list of dicts to a JSON string

    return render_template('index.html', roadmap=roadmap, current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
