For the first part, you needed to open data files with the CSV library and create data structures from their data. In each case, we start with an empty dictionary ({}), open a file for reading, create a CSV reader, and loop through the CSV lines of the file. Inside the loop body, each line is a list of the columns of that row of the file, and we associate one values with another (the precise indices aren't particularly transparent, and are determined from the actual structure of the CSV file. To read the routes, we map from a source to a list of destinations, so we have to first ensure a default value, and then append to the list. Python provides a built-in collections.defaultdict class that is particularly well-suited to this task, although we haven't covered it in this course.


This step was a little tougher - requiring you to run the first few steps of exploration of a BFS-like algorithm. The find_paths function progressively builds out a frontier of destination airports reachable in an increasing number of steps, as well as the paths to each visited destination airport. To get to the next frontier, you can take each new outbound edge from the old frontier, and create a new path to each of the newly reachable destinations. At the end, we return just the paths from the source airport to the destination airport.

It's worth noting that this isn't a particularly efficient implementation, and there are many valid ways to accomplish the same goal. The overall result, though, is a collection of paths from a source airport to a destination airport with at most max_segments steps.

The main function connects all of our functions, and builds a mapping from path length -> path, before dumping the result to a JSON file. And that's it!


