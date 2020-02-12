# Collection of Scripts

Set of scripts that I frequently use, or small scripts for specific jobs. They are categorized according to the language and maybe their usability.
___

### [Shell_Bash][1]
1. [test_gzip.sh][2]<br>Test and measures the speed of gzip utility to compress and uncompress a specific file.<br>It creates an .xls file to store the results. of the start time and the time elapsed. The measurements are in milliseconds and the compress ratio is set as best in order to emphasize to machine's performance.

### [Python][3]
1. [cluster_dietary_value][4]<br>Use unsupervised learning and kmeans algorithm to cluster the dietary values of a given list of foods. The database is just for the demo and the script can be used according to user's need. It reads from an ORACLE database the attributes of foods and store them to a pandas dataframe as independent variables. It makes use of PCA for dimensionality reduction. Every time a user update the database with a new food, the script finds it and categorize it to its cluster. Finally, it commits the changes and close the connection. 










[1]:https://github.com/GkouskosV/collection-of-scripts/tree/master/Shell_Bash
[2]:https://github.com/GkouskosV/collection-of-scripts/blob/master/Shell_Bash/test_gzip.sh
[3]:https://github.com/GkouskosV/collection-of-scripts/tree/master/Python
[4]:https://github.com/GkouskosV/collection-of-scripts/blob/master/Python/cluster_dietary_value.py
