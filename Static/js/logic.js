// Bring in complete joined dataset.
const salaryLivingData = "Data/complete_joined_data";

// Initialize the dropdown menu.
function initMenu()
{
    // Fetch the dropdown menu.
    let dropDownMenu = d3.select("#selDataset");

    // Fetch the JSON data and console log it.
    d3.json(salaryLivingData).then((data) => 
    {
        console.log(data);
    }
    
}