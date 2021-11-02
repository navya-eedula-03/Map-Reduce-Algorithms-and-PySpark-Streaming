# T1

### mapper.py

This code reads the input file and splits the line according to tab spaces. These key-value pairs are passed as output to the reducer.

### reducer.py

Key-value pairs of the source and destination pages are taken from the mapper. The absolute path of the v file is passed as an argument and opened in write mode. The key values in the dictionary are the source pages and the list of destination pages are the corresponding values. 

If the source page does not exist as a key in the dictionary, it is created and appended the corresponding destination value, else a destination page is appended to an existing source page.

The page ranks of the source and destination are stored in the v file and the output of the reducer function is the adjacency list.

# T2

### mapper.py

The previous input of the adjacency list is passed as input the mapper. The absolute paths of the v file and embeddings file are passed as arguments and are opened in read mode.

If a key of the input has multiple destination pages, then the square brackets are removed and split according to the delimiter (,) using the map function, else only the square brackets are removed. All the destination pages are appended to 'vall'. 

For every destination page, the corresponding dot product and then the similarity matrix is computed. The contribution matrix is printed as output.

The pages that have no outgoing links and only incoming links are printed as (0, page, 0).

### reducer.py

The input of the reducer file is the contribution matrix. Here, 'key2' (destination) contributes to 'key1' (source) with contribution 'value'. The page ranks are computed according to the formula. If a page has no outgoing links, then it is simply multiplied by 0.85 else the summation of all the destination pages is computed and then multiplied by 0.85.

Finally, the dictionary is sorted in lexicographical order and the value 0.15 is added to obtain the final page rank. The output of the reducer is each page and its corresponding page rank. 
This computation is done until convergence is achieved via [iterative.sh](http://iterative.sh).
