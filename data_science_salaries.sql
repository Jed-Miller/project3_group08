-- DROP TABLES IF THEY EXIST
DROP TABLE IF EXISTS data_science_salaries CASCADE;
DROP TABLE IF EXISTS cost_of_living_cleaned CASCADE;
DROP TABLE IF EXISTS country_id CASCADE;

CREATE TABLE country_id (
	country_id varchar PRIMARY KEY NOT NULL
);

CREATE TABLE data_science_salaries (
	id int PRIMARY KEY NOT NULL,
	work_year int NOT NULL,
	experience_level varchar NOT NULL,
	employment_type varchar NOT NULL,
	job_title varchar NOT NULL,
	salary int NOT NULL,
	salary_currency varchar NOT NULL,
	salary_in_usd int NOT NULL,
	employee_residence varchar NOT NULL,
	remote_ratio int NOT NULL,
	company_location varchar NOT NULL,
	company_size varchar NOT NULL,
	FOREIGN KEY (company_location) REFERENCES country_id(country_id)
);

CREATE TABLE cost_of_living_cleaned (
	id int PRIMARY KEY NOT NULL,
	country varchar NOT NULL,
	country_id varchar NOT NULL,
	tech_hub varchar NOT NULL,
	lat float NOT NULL,
	long float NOT NULL,
	cost_of_living_index float NOT NULL,
	cost_of_lving_single_usd float NOT NULL,
	cost_of_living_family4_usd float NOT NULL,
	median_home_price_usd int NOT NUll,
	FOREIGN KEY (country_id) REFERENCES country_id(country_id)
);

