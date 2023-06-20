// Bring in complete joined dataset.
const salaryLivingData = "/api/v1.0/complete_data";
const mapData = "/api/v1.0/cost_of_living_geoJSON";

// Initialize the dropdown menu.
function initMenu()
{
    // Fetch the dropdown menu.
    let dropDownMenu = d3.select("#selDataset");

    // Fetch the JSON data and console log it.
    d3.json(salaryLivingData).then((data) => 
    {
        console.log(data);

        //Set country names variable.
        let countryNames = new Set();

        //Iterate through the country names onto the dropdown menu, appending each key value to the the dropdown as a new option.
        data.forEach((countryName) =>
        {
            countryNames.add(countryName.country)
            countryList = Array.from(countryNames);
        });
        
        countryList.forEach((country) =>
        {
            dropDownMenu.append("option").text(country).property("value", country);
        });
        
    })
    
};

//Perform a GET request to the data for map
d3.json(mapData).then((data) => 
{
    console.log(data);
    // createFeatures(data.features);
});

//Create function for the size of the circle based on the average salary in US dollars.
function circleSize(salary_usd) {
    return avg_salary_usd;
};

function colorDepth(cost_index) {
    if (cost_index < 30) {
        return "#7CFC00";
    }
    else if (cost_index < 40) {
        return "#008000";
    }
    else if (cost_index < 50) {
        return "#00BFFF";
    }
    else if (cost_index < 60) {
        return "#483D8B";
    }
    else if (cost_index < 70) {
        return "#9932CC";
    }
    else if (cost_index < 80) {
        return "#DC143C";
    }
    else {
        return "#A52A2A";
    }
}

// Create a create features function
function createFeatures(costLiving) {
    //Define a function that displays each feature in the features array.
    // Give each feature a popup that tells the cost of living metrics.
    function onEachFeature(feature, layer)
    {
        layer.bindPopup(`<h2>${feature.properties.name}<h2><hr>\
        <h3>Average Salary in USD: ${feature.properties.avg_salary_usd}<h3>\
        <h3>Cost of Living Index: ${feature.properties.cost_of_living_index}<h3>\
        <h3>Cost of Living for Single Person in USD: ${feature.properties.cost_of_living_single_usd}<h3>\
        <h3>Cost of Living for Family of 4 in USD: ${feature.properties.cost_of_living_family4_usd}<h3>\
        <h3>Median Home Price in USD: ${feature.properties.median_home_price_usd}<h3>`);
    }

    // Create a GeoJSON layer that contains the features array on the mapData object.
    // Run the onEachFeature function once for each piece of data in the array.
    let techHubs = L.geoJSON(quakeData,
        {
            onEachFeature: onEachFeature,
        
        pointToLayer: function(feature, latlng) {

            let circleMarkerFeatures = 
            {
                radius: circleSize(feature.properties.avg_salary_usd),
                fillColor: colorDepth(feature.properties.cost_of_living_index),
                color: "black",
                fillOpacity: 0.6,
                weight: 0.5,
                stroke: true
            }
            return L.circle(latlng, circleMarkerFeatures);
        }
    });

    //Send the techHubs layer to the createMap function.
}

//Create the createMap function.
//function 

initMenu();

