# Synthetic data examples
### Prerequisite 
Install SDV : follow https://github.com/sdv-dev/SDV <br>
Check requirement.txt

## Example-1
#### Generate series data on single column value using frequency distributions of attributes as probability weights. 
In this example we used covid specific data which share the number of covid cases per gender and age. 
This data having fields Reporting Date, Country, Gender, Age & # of cases. 

## Example-2
#### Using SDV tool to identifying the relationships between different attributes and unique identifier with-in table and generate synthetic data accordingly. 
#### SDV tool allows users to statistically model a table, relational dataset.
Data set contains user specific information like gender, country, age and user_id (it’s a unique identifier in this data set).

## Example-3
#### Using SDV tool to identifying the foreign key relationships between different tables and generate synthetic data accordingly. 
#### SDV tool allows users to statistically model a table, relational dataset.
Test data contain user specific and its web session details. These two tables related with each other with user_id column.
