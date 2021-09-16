# Report

### [https://docs.google.com/forms/d/e/1FAIpQLSecvOf85Lld8KePDfXVoZfIKCuBV5UAELuzn0u1dhd1AuYtFg/viewform](https://docs.google.com/forms/d/e/1FAIpQLSecvOf85Lld8KePDfXVoZfIKCuBV5UAELuzn0u1dhd1AuYtFg/viewform)

## Task 1:

### mapper.py

The .json file was piped as input and stripped to remove the leading and trailing spaces. The required data were filtered according to the parameters specified (description, severity, sunrise_sunset, visibility, precipitation, and weather condition) using nested if statements to pass into reducer.py. The output from this file is the hour in which the accident took place(using datetime module from the attribute Start_Time) for all the accidents that satisfy the previously stated conditions. These values are streamed onto stdin.

### reducer.py

The corresponding values were taken as input from mapper.py (from stdin), stripped, and appended to a list. These list values are used to:

(a) Find what hours of the day accidents have taken place. We are using a set to find these unique values. 
The set is then converted back to a list and sorted.
(b) The number of accidents that took place in that hour. This is implemented by using a simple count() function.

## Task 2:

### mapper.py

The starting coordinates (latitude and longitude) are sent to the specified URL using the POST request which returns the json payloads containing the state and city. Three arguments, namely, ending latitude, ending longitude, and maximum distance are fed into the command line. The dist() function calculates the Euclidian distance between the pair of coordinates which is then compared to the previously passed distance. The output of mapper.py is a string of the following format:  
state  city

### reducer.py

The output of mapper.py is taken as input from STDIN using the sys module. This input is lexicographically sorted where sorting is performed by Hadoop. Every line is split by using the first occurence of space. This extracts the state from the input. A nested if-else construct is written to check for and execute the following conditions:  
a) Within the same state, the counter is incremented till a different state is found.  
b) For every city, a similar approach is followed where the count of the city is calculated and printed for each occurence of that city.  
Finally, the total count of the number of accidents that took place in the state is printed.  
The above steps are implemented in a loop for every unique state.
