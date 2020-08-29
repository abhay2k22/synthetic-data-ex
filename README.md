# Synthetic data examples
### Prerequisite 
Install SDV : follow https://github.com/sdv-dev/SDV <br>
Installation packages: requirement.txt

## Example-1
#### Generate series data on single column value using frequency distributions of attributes as probability weights. 
In this example we used covid specific data which share the number of covid cases per gender and age. 
This data having fields Reporting Date, Country, Gender, Age & # of cases. 
1. This is covid specific data, which share the number of covid cases per gender and age. This data having fields Reporting Date, Country, Gender, Age & # of cases. You can find data sheet [here](https://github.com/abhay2k22/synthetic-data-ex/blob/master/example-1/data.csv).
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex1/1.png)

2. Count of Unique values contained by attribute
(This will serve as probability weights)
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex1/2.png)

3. Number of Rows to in data set

![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex1/3.png)

4. Generating data using numpy’s random choice method.
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex1/4.png)

5. Data Comparison Original v/s Synthetic Data
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex1/5.png)
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex1/6.png)

## Example-2
#### Using SDV tool to identifying the relationships between different attributes and unique identifier with-in table and generate synthetic data accordingly. 
#### SDV tool allows users to statistically model a table, relational dataset.

1. Data set contains user specific information like gender, country, age and user_id (it’s a unique identifier in this data set).
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex2/7.png)

2. Fit and save model using SDV. Then use the same model to generate synthetic data. 
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex2/8.png)

3. Show generated synthetic data

![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex2/9.png)

4. Statistical Comparison of Synthetically generated Data v/s Real Data.
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex2/10.png)

## Example-3
#### Using SDV tool to identifying the foreign key relationships between different tables and generate synthetic data accordingly. 
#### SDV tool allows users to statistically model a table, relational dataset.

1. Test data contain user specific and its web session details. These two tables related with each other with user_id column.
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex3/11.png)
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex3/12.png)

2. Fit and save model using SDV. Then use the same model to generate synthetic data.
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex3/13.png)

3. Synthetic Data
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex3/14.png)

4. Comparison of Synthetically generated Data v/s Real Data.
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex3/15.png)
![dataset](https://github.com/abhay2k22/synthetic-data-ex/blob/master/img/ex3/16.png)

