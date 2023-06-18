SELECT ds.company_location, 
		clc.tech_hub,
		ROUND(avg(ds.salary_in_usd), 2) AS "Average Salary in US Dollars",
		clc.cost_of_living_index,
		clc.cost_of_lving_single_usd,
		clc.cost_of_living_family4_usd,
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
GROUP BY ds.company_location, 
	clc.tech_hub,
	clc.cost_of_living_index,
	clc.cost_of_lving_single_usd,
	clc.cost_of_living_family4_usd,
	clc.median_home_price_usd
ORDER BY ds.company_location asc;
	
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'IN';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'US';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'CA';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'GB';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'ES';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'DE';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'FR';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'BR';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'PT';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'NL';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'GR';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'MX';

SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'AU';

