# Import the dependencies.
import pandas as pd
import json

from sqlalchemy import create_engine, func


from flask import Flask, jsonify, render_template

with open("Data/mapData.json", "r") as f:
        mapGEO = f.read()
        loaded_JSON = json.loads(mapGEO)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

engine = create_engine('postgresql+psycopg2://postgres:postgres\
@localhost:5432/project03_group08')
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
         f"----------------------<h3>"
        f"<h4>/api/v1.0/data_science_salaries_top7<br/>"
        f"Returns salaries from top 7 job titles in data base.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/cost_of_living_geoJSON<br/>"
        f"Returns geoJSON file of cost_living_metrics<br/>"
        f"----------------------<br>"
        f"/api/v1.0/salary_data_by_country/country_id<br/>"
        f"Returns salary and cost of living data for user-provided country.<br/>"
         f"----------------------<br>"
        f"/api/v1.0/countryList<br/>"
        f"Returns list of countries within the dataset.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/companySizeExperience/Australiabr/>"
        f"Returns list of average salaries based off company size and employee experience level.<br/>"
        f"----------------------<br>"
        f"/api/v1.0/rendered_HTML<br/>"
        f"Returns rendered version of analytics project<br/>"
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
    with engine.connect() as connection:
        query ="""
        SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
        FROM data_science_salaries ds
        INNER JOIN cost_of_living_cleaned clc
        ON ds.company_location = clc.country_id"""
        test_data = pd.read_sql_query(query, connection)
    return jsonify(test_data.to_dict(orient='records'))

@app.route("/api/v1.0/data_science_salaries_top7")
def top7():
    """List complete dataset data."""
    with engine.connect() as connection:
        query ="""
        SELECT job_title, salary_in_usd
        FROM data_science_salaries
        WHERE job_title IN('Data Engineer', 'Data Analyst', 'Data Scientist',
                        'Machine Learning Engineer', 'Analytics Engineer',
                        'Research Scientist', 'Data Architect')"""
        test_data = pd.read_sql_query(query, connection)
    return jsonify(test_data.to_dict(orient='records'))

"""List cost of living overview data data."""
@app.route("/api/v1.0/cost_of_living_geoJSON")
def geoJSON():
    
    return jsonify(loaded_JSON)
    # THE VINNY WAY (The pretty way)
    # mapGEO = pd.read_json("Data/mapData.json")
    # results = mapGEO.to_json(orient="records")
    # parsed = json.loads(results)
    # return parsed


"""List selected country data."""
@app.route("/api/v1.0/salary_data_by_country/<country_id>")
def countrySalary(country_id): 

    with engine.connect() as connection:
        query =f"""
        SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
        FROM data_science_salaries ds
        INNER JOIN cost_of_living_cleaned clc
        ON ds.company_location = clc.country_id
        WHERE ds.company_location = '{country_id}';"""
        test_data = pd.read_sql_query(query, connection)
        if test_data.empty:
            return jsonify({"Error": "Wrong Entry"})
    return jsonify(test_data.to_dict(orient='records'))

@app.route("/api/v1.0/companySizeExperience/<country>")
def barData(country): 

    with engine.connect() as connection:
        query =f"""
        SELECT clc.country, ds.company_size, ds.experience_level, ROUND(avg(ds.salary_in_usd))
        FROM data_science_salaries ds
        INNER JOIN cost_of_living_cleaned clc
        ON ds.company_location = clc.country_id
        WHERE clc.country = '{country}'
        GROUP BY clc.country, ds.company_size, ds.experience_level"""
        test_data = pd.read_sql_query(query, connection)
    return jsonify(test_data.to_dict(orient='records'))

@app.route("/api/v1.0/countryList")
def countryList(): 

    with engine.connect() as connection:
        query =f"""
        SELECT country
        FROM cost_of_living_cleaned
        ORDER BY country asc;"""
        test_data = pd.read_sql_query(query, connection)
    return jsonify(test_data.to_dict(orient='records'))

@app.route("/api/v1.0/rendered_HTML")
def renderWelcome():
    return render_template("index.html")

@app.route("/api/v1.0/map")
def renderMap():
    return render_template("map.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9595,debug=True)