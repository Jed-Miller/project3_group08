--techHubs query
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

--complete_joined query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id

--India query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'IN';

--Us query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'US';

--Canada query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'CA';

--Great Britain query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'GB';

--Spain query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'ES';

--Denmark query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'DE';

--France query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE 
ds.company_location = 'FR';

--Brazil query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'BR';

--Portugal query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'PT';

--Netherlands query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'NL';

--Greece query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'GR';

--Mexico query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'MX';

--Australia query
SELECT ds.*, clc.tech_hub,
		clc.lat, clc.long, clc.cost_of_living_index,
		clc.cost_of_lving_single_usd, clc.cost_of_living_family4_usd, 
		clc.median_home_price_usd
FROM data_science_salaries ds
INNER JOIN cost_of_living_cleaned clc
ON ds.company_location = clc.country_id
WHERE ds.company_location = 'AU';

