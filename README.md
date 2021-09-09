# Report

### [https://docs.google.com/forms/d/e/1FAIpQLSecvOf85Lld8KePDfXVoZfIKCuBV5UAELuzn0u1dhd1AuYtFg/viewform](https://docs.google.com/forms/d/e/1FAIpQLSecvOf85Lld8KePDfXVoZfIKCuBV5UAELuzn0u1dhd1AuYtFg/viewform)

## Task 1:

### mapper.py

The .json file was piped as input and stripped to remove the leading and trailing spaces. The required data were filtered according to the parameters specified (description, severity, sunrise_sunset, visibility, precipitation, and weather condition) using nested if statements to pass into reducer.py. The output from this file is the hour in which the accident took place (computed from Start_Time variable using datetime module) for all the accidents that satisfy the previously stated conditions. 

### reducer.py

The corresponding values were taken as input from mapper.py, stripped, and appended to a list. These list values are used to:

(a) Find what hours of the day accidents have taken place. We are using a set to find these unique values. 
The set is then converted back to a list and sorted.
 (b) The number of accidents that took place in that hour. This is implemented by using a simple count() function.


