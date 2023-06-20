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
        f"/api/v1.0/rendered_HTML<br/>"
        f"Returns rendered version of analytics project<br/>"
        f"----------------------<br>"
        f"/api/v1.0/cost_of_living_geoJSON<br/>"
        f"Returns geoJSON file of cost_living_metrics<br/>"
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
        f"----------------------<br>"
        f"/api/v1.0/cost_of_living_overview<br/>"
        f"Returns list of tech_hubs and their cost of living metrics.<br/>"
    )

@app.route("/api/v1.0/complete_data")
def complete():
    """List complete dataset data."""
    test_data = pd.read_csv("Data/complete_joined_data.csv")
    return jsonify(test_data.to_dict(orient='records'))
    
"""List cost of living overview data data."""
@app.route("/api/v1.0/cost_of_living_geoJSON")
def geoJSON():
    
    test_data = {
    "type" : "FeatureCollection",
        "features" : [{ 
            "type" : "Feature", 
            "properties" : {  
                "name" : "Melbourne, Australia", 
                "avg_salary_usd" : "$80033.43",
                "cost_of_living_index" : "80.6",
                "cost_of_living_single_usd" : "$1147.30",
                "cost_of_living_family4_usd" : "$4101.20",
                "median_home_price_usd" : "$1023000"
            }, 
            "geometry" : { 
                "type" : "Point", 
                "coordinates" : [144.9632, -37.8142176] 
            }
        }, {
         
        "type" : "Feature", 
        "properties" : {  
            "name" : "Sao Paulo, Brazil", 
            "avg_salary_usd" : "$40579.20",
            "cost_of_living_index" : "44.2",
            "cost_of_living_single_usd" : "$660.90",
            "cost_of_living_family4_usd" : "$2392.40",
            "median_home_price_usd" : "$290691"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [-46.6333824, -23.5506507] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Toronto, Canada", 
            "avg_salary_usd" : "$131917.69",
            "cost_of_living_index" : "72.6",
            "cost_of_living_single_usd" : "$1103",
            "cost_of_living_family4_usd" : "$3986.30",
            "median_home_price_usd" : "$951040"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [-79.383184, 43.653226] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Copenhagen, Denmark", 
            "avg_salary_usd" : "$88288.80",
            "cost_of_living_index" : "82.1",
            "cost_of_living_single_usd" : "$1199.90",
            "cost_of_living_family4_usd" : "$4294.70",
            "median_home_price_usd" : "$240000"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [12.568337, 55.676098] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Barcelona, Spain", 
            "avg_salary_usd" : "$57676.06",
            "cost_of_living_index" : "57.4",
            "cost_of_living_single_usd" : "$845",
            "cost_of_living_family4_usd" : "$2950.50",
            "median_home_price_usd" : "$968274"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [2.173404, 41.385063] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Paris, France", 
            "avg_salary_usd" : "$66138.74",
            "cost_of_living_index" : "76.9",
            "cost_of_living_single_usd" : "$1125.70",
            "cost_of_living_family4_usd" : "$4021.50",
            "median_home_price_usd" : "$1628182"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [2.3483915, 48.8534951] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "London, England", 
            "avg_salary_usd" : "$86890.05",
            "cost_of_living_index" : "83.6",
            "cost_of_living_single_usd" : "$1303.2",
            "cost_of_living_family4_usd" : "$4457.6",
            "median_home_price_usd" : "$1689022"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [-0.127758, 51.507351] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Thessaloniki, Greece", 
            "avg_salary_usd" : "$51792.50",
            "cost_of_living_index" : "56.3",
            "cost_of_living_single_usd" : "$863",
            "cost_of_living_family4_usd" : "$2852.90",
            "median_home_price_usd" : "$235872"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [22.9352716, 40.6403167] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Bangalore, India", 
            "avg_salary_usd" : "$30197.74",
            "cost_of_living_index" : "25.5",
            "cost_of_living_single_usd" : "$368.60",
            "cost_of_living_family4_usd" : "$1290.30",
            "median_home_price_usd" : "$121749"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [77.594566, 12.971599] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Guadalajara, Mexico", 
            "avg_salary_usd" : "$97151.10",
            "cost_of_living_index" : "44",
            "cost_of_living_single_usd" : "$642.30",
            "cost_of_living_family4_usd" : "$2337.20",
            "median_home_price_usd" : "$122460"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [-103.338396, 20.6720375] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Eindhoven, Netherlands", 
            "avg_salary_usd" : "$78738.31",
            "cost_of_living_index" : "69.7",
            "cost_of_living_single_usd" : "$1028.8",
            "cost_of_living_family4_usd" : "$3598.70",
            "median_home_price_usd" : "$328700"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [5.478633, 51.4392648] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "Lisbon, Portugal", 
            "avg_salary_usd" : "$50538.71",
            "cost_of_living_index" : "52.5",
            "cost_of_living_single_usd" : "$747.80",
            "cost_of_living_family4_usd" : "$2632.50",
            "median_home_price_usd" : "$714000"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [-9.1365919, 38.7077507] 
        }
    }, {
        "type" : "Feature", 
        "properties" : {  
            "name" : "San Jose, California", 
            "avg_salary_usd" : "$151822.01",
            "cost_of_living_index" : "87.6",
            "cost_of_living_single_usd" : "$1359.40",
            "cost_of_living_family4_usd" : "$4808.80",
            "median_home_price_usd" : "$1090308"
        }, 
        "geometry" : { 
            "type" : "Point", 
            "coordinates" : [-121.894956, 37.339386] 
        }
    }]
    }
    return jsonify(test_data)

"""List selected country data."""
@app.route("/api/v1.0/salary_data_by_country/<country_id>")
def country(country_id): 
    if country_id == "AU": 
        test_data = pd.read_csv("Data/AU_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "BR":
        test_data = pd.read_csv("Data/BR_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "CA":
        test_data = pd.read_csv("Data/CA_data.csv")
        return jsonify(test_data.to_dict(orient='records'))
    elif country_id == "DE":
        test_data = pd.read_csv("Data/DE_data.csv")
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
        
@app.route("/api/v1.0/rendered_HTML")
def render():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)