from flask import Flask, render_template
from roadmap_data import roadmap  # Import the roadmap data
from datetime import datetime
import json
import copy

app = Flask(__name__)

@app.route('/')
def index():
    current_year = datetime.now().year
    temp_roadmap = copy.deepcopy(roadmap)  # Create a deep copy of the roadmap

    # Convert each links array to a JSON string for each item
    for category, items in temp_roadmap.items():
        for item, links in items.items():
            json_string = json.dumps(links)  # Convert list of dicts to a JSON string
            print(f"JSON for {item}: {json_string}")  # Print the specific JSON string
            items[item] = json_string

    return render_template('index.html', roadmap=temp_roadmap, current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
