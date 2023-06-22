// Bring in complete joined dataset.
const salaryLivingData = "/api/v1.0/complete_data";
const mapData = "/api/v1.0/cost_of_living_geoJSON";
const countryList = "/api/v1.0/countryList";
// const sizeExperience = "/api/v1.0/companySizeExperience";

// Initialize the dropdown menu.
function initMenu()
{
    // Fetch the dropdown menu.
    let dropDownMenu = d3.select("#selDataset");

    // Fetch the JSON data and console log it.
    d3.json(countryList).then((data) => 
    {
        console.log(data);

        //Set the country names variable.
        let countryNames = data.data

        //Iterate through the country names onto the dropdown menu
        countryNames.forEach((countryName) =>
        {
            dropDownMenu.append("option").text(countryName).property("value", countryName);
        });

        countryName = countryNames[0];

        groupedBars(countryName);
    })
    
};

// Create the world map function.
function worldMap( ) {
//Perform a GET request to the data for map
d3.json(mapData).then((data) => 
{
    console.log(data);
    createFeatures(data.features);

    //Create function for the size of the circle based on the average salary in US dollars.
    function circleSize(avgSalary) {
        return avgSalary * 4;
    };

    //Create a colorDepth function based off the cost of living index
    function colorDepth(costIndex) {
        if (costIndex < 30) {
            return "#0ad2ff";
        }
        else if (costIndex < 40) {
            return "#0fffdb";
        }
        else if (costIndex < 50) {
            return "#2962ff";
        }
        else if (costIndex < 60) {
            return "#b4e600";
        }
        else if (costIndex < 70) {
            return "#ff8c00";
        }
        else if (costIndex < 80) {
            return "#9500ff";
        }
        else if (costIndex < 90) {
            return "#ff0059";
        }
        else {
            return "#22052d";
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
            <h5>Cost of Living Index (Housing Not Included): ${feature.properties.cost_of_living_index}<h5>\
            <h5>Cost of Living for Single Person in USD (Housing Not Included): ${feature.properties.cost_of_living_single_usd}<h5>\
            <h5>Cost of Living for Family of 4 in USD (Housing Not Included): ${feature.properties.cost_of_living_family4_usd}<h5>\
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
        console.log("Welcome")
        
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
            center: [15,20],
            zoom: .8,
            minZoom: 2.3,
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

            div.innerHTML += "<h5 style='text-align: right'>CL Index</h5>"

            for (var i = 0; i < indexLevel.length; i ++) {
                div.innerHTML +=
                '<i style="background:' + colorDepth(indexLevel[i] + 1) + '"></i> ' + indexLevel[i] + (indexLevel[i + 1] ? '&ndash;' + indexLevel[i + 1] + '<br>' : '+');
            }
            return div;
        };

            legend.addTo(myMap);
    }
});
}

function groupedBars()
{
    let countryName = d3.select("#selDataset").node().value
    
    d3.json(`/api/v1.0/companySizeExperience/${countryName}`).then(data => 
    {
        console.log(data)
        
        let companySize = [];
        let experienceLevel = [];
        let avgSalary = [];


        for (let prop of data.data)
        {
            console.log(`key: ${prop}, value: ${obj[prop]}`);
            // experienceLevel.push(i["Experience Level"])
            // avgSalary.push(i["Avg Salary"])
        };



        // let dom = document.getElementById('chart-container');
        // let myChart = echarts.init(dom, null, {
        // renderer: 'canvas',
        // useDirtyRect: false
        // });
        // let app = {};

        // let option;

        // option = {
        //     legend: {},
        //     tooltip: {},
        //     dataset: {
        //       source: [
        //         ['Company Size', '2012', '2013', '2014', '2015'],
        //         ['Entry Level', 41.1, 30.4, 65.1, 53.3],
        //         ['Mid/Intermediate Level', 86.5, 92.1, 85.7, 83.1],
        //         ['Senior Level', 24.1, 67.2, 79.5, 86.4]
        //         ['Executive Level', 24.1, 67.2, 79.5, 86.4]
        //       ]
        //     },
        //     xAxis: [
        //       { type: 'category', gridIndex: 0 },
        //       { type: 'category', gridIndex: 1 }
        //     ],
        //     yAxis: [{ gridIndex: 0 }, { gridIndex: 1 }],
        //     grid: [{ bottom: '55%' }, { top: '55%' }],
        //     series: [
        //       // These series are in the first grid.
        //       { type: 'bar', seriesLayoutBy: 'row' },
        //       { type: 'bar', seriesLayoutBy: 'row' },
        //       { type: 'bar', seriesLayoutBy: 'row' },
        //       // These series are in the second grid.
        //       { type: 'bar', xAxisIndex: 1, yAxisIndex: 1 },
        //       { type: 'bar', xAxisIndex: 1, yAxisIndex: 1 },
        //       { type: 'bar', xAxisIndex: 1, yAxisIndex: 1 },
        //       { type: 'bar', xAxisIndex: 1, yAxisIndex: 1 }
        //     ]
        //   };
          
        //   if (option && typeof option === 'object') {
        //     myChart.setOption(option);
        //   }
          
        //   window.addEventListener('resize', myChart.resize);
    })
}


initMenu();
worldMap();

