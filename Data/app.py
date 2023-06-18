# Import the dependencies.
import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"----------------------<br>"
        f"/api/v1.0/test<br/>"
        f"Returns Date and Precipitation for latest year.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/stations<br/>"
        f"Returns list of stations and their info.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/tobs<br/>"
        f"Return data for the most active station (USC00519281).<br/>"
        f"----------------------<br/>"
        f"/api/v1.0/start/<start><br/>"
        f"Returns min, max, and average temperatures from user-provided start date to the end of the dataset.<br/>"
        f"----------------------<br/>"
        f"/api/v1.0/start_end/<start>/<end><br/>"
        f"Returns min, max, and average temperatures from user-provided start and end date<br/>"
    )

@app.route("/api/v1.0/test")
def test():
    """List test data."""
    test_data = pd.read_csv("test.csv")
    return jsonify(test_data.to_dict(orient='records'))



if __name__ == '__main__':
    app.run(debug=True)