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
        f"<h1>Welcome to our Data Science Salaries by Countries Flask<h1><br>"
        f"<h3>Available Routes:<br/>"
        f"----------------------<h3>"
        f"<h4>/api/v1.0/complete_data<br/>"
        f"Returns all data from database.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/cost_of_living_overview<br/>"
        f"Returns list of tech_hubs and their cost of living metrics.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/salary_data_by_country/country_id<br/>"
        f"Returns salary and cost of living data for user-provided country.<br/>"
        f"<br><h3>Available countries and their ids<br>"
        f"----------------------<h3>"
        f"<h4>Australia == AU<br>"
        f"Brazil == BR<br>"
        f"Canada == CA<br>"
        f"Denmark == DE<br>"
        f"Spain == ES<br>"
        f"France == FR<br>"
        f"Great Britain == GB<br>"
        f"Greece == GR<br>"
        f"India == IN<br>"
        f"Mexico == MX<br>"
        f"Netherlands == NE<br>"
        f"Portugal == PT<br>"
        f"United States == US<h4><br>"
    )

@app.route("/api/v1.0/complete_data")
def complete():
    """List complete dataset data."""
    test_data = pd.read_csv("Data/complete_joined_data.csv")
    return jsonify(test_data.to_dict(orient='records'))
    

@app.route("/api/v1.0/cost_of_living_overview")
def overview():
    """List cost of living overview data data."""
    test_data = pd.read_csv("popup_data.csv")
    return jsonify(test_data.to_dict(orient='records'))

"""List selected country data."""
@app.route("/api/v1.0/salary_data_by_country/<country_id>")
def country(country_id): 
    if country_id == "AU": 
        test_data = pd.read_csv("AU_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "BR":
        test_data = pd.read_csv("BR_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "CA":
        test_data = pd.read_csv("CA_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "DE":
        test_data = pd.read_csv("DE_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "ES":
        test_data = pd.read_csv("ES_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "FR":
        test_data = pd.read_csv("FR_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "GB":
        test_data = pd.read_csv("GB_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "GR":
        test_data = pd.read_csv("GR_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "IN":
        test_data = pd.read_csv("IN_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "MX":
        test_data = pd.read_csv("MX_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "NL":
        test_data = pd.read_csv("NL_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "PT":
        test_data = pd.read_csv("PT_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "US":
        test_data = pd.read_csv("US_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    else:
        return (
        f"Wrong country id inputted. Please try again.<br>"
        f"<h3>Available countries and their ids<br>"
        f"----------------------<h3>"
        f"<h4>Australia == AU<br>"
        f"Brazil == BR<br>"
        f"Canada == CA<br>"
        f"Denmark == DE<br>"
        f"Spain == ES<br>"
        f"France == FR<br>"
        f"Great Britain == GB<br>"
        f"Greece == GR<br>"
        f"India == IN<br>"
        f"Mexico == MX<br>"
        f"Netherlands == NE<br>"
        f"Portugal == PT<br>"
        f"United States == US<h4><br>"
        )
        
@app.route("/api/v1.0/test")
def render():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)