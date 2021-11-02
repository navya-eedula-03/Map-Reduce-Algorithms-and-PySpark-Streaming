# T1

The city.csv was read and converted to an RDD after dropping the rows that had null values. The data was filtered with country  given as input and df3 now has key-value pairs of city-AverageTemperature. These key-value pairs are grouped according to key and a lambda function was written to find all the cities where the temperature was greater than average temperature for the country. A count function was performed to count all the occurrences and returned as output.

# T2

The two files, city.csv and global.csv where read into df and dfg respectively while setting the header options as true. Each of the columns in the files were type-casted to suitable data types - date and float.

The city dataset was grouped according to country and the aggregate function max() was performed to obtain the maximum of average temperature for each date. A natural join was performed according to dt (date) to retrieve all the dates where the country’s maximum average temperature on a date turned out to be higher than the worldwide land average temperature on the same date. These values were counted, sorted and returned as output.
