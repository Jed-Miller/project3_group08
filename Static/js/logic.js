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

//Create the map.
// let myMap = L.map("map",
// {
//     center: [0,0],
//     zoom: 0,
//     //layers: [outdoors, techHubs]
// });
// L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
//     {attribution:`&copy; <a href="https://www.openstreetmap.org/copyright">
//                  OpenStreetMap</a> contributors`})
//     .addTo(myMap)
//Create the map chart.

//Perform a GET request to the data for map
d3.json(mapData).then((data) => 
{
    console.log(data);
    createFeatures(data.features);
    // createFeatures(data.features);


    //Create function for the size of the circle based on the average salary in US dollars.
    function circleSize(avgSalary) {
        return avgSalary * 4;
    };

    function colorDepth(costIndex) {
        if (costIndex < 30) {
            return "#000000";
        }
        else if (costIndex < 40) {
            return "#008000";
        }
        else if (costIndex < 50) {
            return "#00BFFF";
        }
        else if (costIndex < 60) {
            return "#483D8B";
        }
        else if (costIndex < 70) {
            return "#9932CC";
        }
        else if (costIndex < 80) {
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
            layer.bindPopup(`<h4>${feature.properties.name}<h4><hr>\
            <h5>Average Salary in USD: ${feature.properties.avg_salary_usd}<h5>\
            <h5>Cost of Living Index: ${feature.properties.cost_of_living_index}<h5>\
            <h5>Cost of Living for Single Person in USD: ${feature.properties.cost_of_living_single_usd}<h5>\
            <h5>Cost of Living for Family of 4 in USD: ${feature.properties.cost_of_living_family4_usd}<h5>\
            <h5>Median Home Price in USD: ${feature.properties.median_home_price_usd}<h5>`);
        }

        // Create a GeoJSON layer that contains the features array on the mapData object.
        // Run the onEachFeature function once for each piece of data in the array.
        let techHubs = L.geoJSON(costLiving,
            {
                onEachFeature: onEachFeature,
            
            pointToLayer: function(feature, latlng) {

                let circleMarkerFeatures = 
                {
                    radius: circleSize(feature.properties.avg_salary_usd),
                    fillColor: colorDepth(feature.properties.cost_of_living_index),
                    color: "black",
                    fillOpacity: 0.8,
                    weight: 0.5,
                    stroke: true
                }
                return L.circle(latlng, circleMarkerFeatures);
            }
        });

        //Send the techHubs layer to the createMap function.
        createMap(techHubs);
    }

    //Create the createMap function.
    function createMap(techHubs)
    {
        //Create the base layers from mapbox.
        let outdoors = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/outdoors-v12/tiles/{z}/{x}/{y}?access_token={access_token}', 
        {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        zoom: 13,
        access_token: api_key
        })

        let satellite = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v12/tiles/{z}/{x}/{y}?access_token={access_token}', 
        {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        zoom: 13,
        access_token: api_key
        });

        //Create a basemaps object.
        let baseMaps =
        {
            Outdoors: outdoors,
            Satellite: satellite
        };

        //Create an overlay object to hold our overlay.
        let overlayMaps =
        {
            TechHub: techHubs
        };

        //Create the map.
        let myMap = L.map("map",
        {
            center: [0,0],
            zoom: 2.49,
            layers: [outdoors, techHubs]
        });

        //Create a layer control.
        //Pass it to the baseMaps and overlayMap
        //Add the control to the map
        L.control.layers(baseMaps, overlayMaps, {
            collapsed: false
        }).addTo(myMap);

        //Create legend
        let legend = L.control({position: "bottomright"});
        legend.onAdd = function() {
            let div = L.DomUtil.create("div", "info legend"),
            indexLevel = [20,30,40,50,60,70,80,90];

            div.innerHTML += "<h5 style='text-align: right'>CLI</h5>"

            for (var i = 0; i < indexLevel.length; i ++) {
                div.innerHTML +=
                '<i style="background:' +colorDepth(indexLevel[i] + 1) + '"></i> ' + indexLevel[i] + (indexLevel[i + 1] ? '&ndash;' + indexLevel[i + 1] + '<br>' : '+');
            }
            return div;
        };

            legend.addTo(myMap);
    }
});

initMenu();

