// Bring in complete joined dataset.
const salaryLivingData = "/api/v1.0/complete_data";

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

initMenu();

