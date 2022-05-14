## File I/O

## Solution
eo
In this exercise, the goal was to count the number of unique "words" in a plain text file, such as Hamlet.

We follow the standard pattern for reading data from files: open a file-like object from a path, read information from it into Python, and then do something with that information (perhaps even writing it to another file!).

In this case, we use a collections.Counter() to keep track of word counts. It is also valid to use a dictionary mapping words to their counts (taking care to default words to zero occurrences), but we might as well leverage Python's great built-in Counter tool.

Once we have a place for words to land, we open up the file, and read each of its lines (as a string)! We split the line (from the file) on whitespace, call each of the resulting chunks "words," and finally update our Counter object with these new words.

Lastly, we use the Counter.most_common method (neat, right? Great for interviews) to get the ten most common words and their counts, and print out the results to the console.