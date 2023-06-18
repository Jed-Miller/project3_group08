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
	clc.median_home_price_usd;



