Project: Exploring Near-Earth Objects
5 minutes remaining


8 of 9 concepts completed
Submission
Deliverables
Upon completing this project, you'll have modified at least models.py, extract.py, database.py, filters.py, and write.py. If you went above-and-beyond with any Stand Out Suggestions, include your changes alongside an EXTENSIONS.md file describing your changes so that the reviewers can understand what you've done.

Over the course of this project (specifically, in Task 4), you've likely created several output files. You should remove these files before submitting your project.

Submitted Files
Before you submit the project, confirm that it includes all of the required files:

Task List





Rubric
In addition to the functionality requirements detailed above, your submission will be assessed on how well it follows best practices in Python. Roughly speaking, "best practices" can be divided into two categories - mechanics and design. Good Python mechanics adhere to PEP 8 - the style guide for Python code - and PEP 257 - docstring conventions. These address rules for naming, spacing, commenting, and several common programming patterns. Additionally, good general programming mechanics that you are expected to follow include removing starter code markings, removing extraneous print statements, and documenting your code. Python design refers to the higher-level organization of your code - the interfaces and implementation boundaries defined by your code objects. Many interface and implementation boundaries are already imposed by the organization of the starter code; however, there are still several situations (particularly in Tasks 3 and 4) in which the organization of your code can reflect poorly on or reflect well on the organization of the problem and your choice of solution.  

Complete details on grading criteria are available in the Project Rubric.

PROJECT SPECIFICATION
Investigating Near-Earth Objects

Functionality

CRITERIA

Produce classes that represent near-Earth objects and their close approaches. (Task 1)

MEETS SPECIFICATIONS 

The NearEarthObject class represents a near-Earth object.

The constructor assigns attributes for:
designation: The NEO’s primary designation.
name: The NEO’s IAU name (could be empty, or None)
diameter: The NEO’s diameter, in kilometers, or NaN.
hazardous: Whether the NEO is potentially hazardous
approaches: A collection of this NEO’s CloseApproaches (initially an empty collection).
The CloseApproach class represents a close approach to Earth by an NEO.
The constructor assigns attributes for:
time: The date and time, in UTC, at which the NEO passes closest to Earth.
distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
velocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
neo: A reference to the NearEarthObject that is making the close approach (initially None).
An additional attribute, to store the NEO’s primary designation before the CloseApproach is linked to its NearEarthObject
Additionally, each of these classes should implement a __str__ method that produces a human-readable description of the contents of the object.

Load data from CSV and JSON files into Python objects. (Task 2a)

The load_neos function loads NEO data from a CSV file.

The function opens the given file for reading.
The function uses the csv module to parse the file contents into a standard Python data structure (e.g. list, dict, etc).
The function converts this raw data into a collection of NearEarthObjects
The function returns a collection of NearEarthObjects
The load_approaches method loads close approach data from a JSON file.

The function opens the given file for reading.
The function uses the json module to parse the file contents into a dict.
The function converts this raw data into a collection of CloseApproach objects.
The function returns a collection of CloseApproach objects.
Data from the extraneous columns (CSV) and fields (JSON) shouldn’t be bound to the constructed NearEarthObjects and CloseApproaches.

Link together Python objects and any required metadata in a database wrapper that supports basic inspection. (Task 2b)

The NEODatabase constructor captures and preprocesses a collection of NEOs and close approaches.

The constructor captures and saves its arguments, a collection of NearEarthObject and a collection of CloseApproaches.
The constructor precomputes auxiliary data structures to assist with the get_neo_by_designation and get_neo_by_name methods.
At the end of the constructor, the .neo attribute is set on each close approach to the matching NearEarthObject.
At the end of the constructor, the .approaches attribute is populated for each NearEarthObject with a collection of its close approaches.
The get_neo_by_designation method fetches an NEO by its primary designation, or returns None if no matches are found.

The get_neo_by_name method fetches an NEO by its name, or returns None if no matches are found.

Convert user-specified criteria to a collection of filters. (Task 3a)

The create_filters function produces a collection that can be used by the query method to perform a search of close approaches.

The function respects the --date filter mode.
The function respects the --start-date filter mode.
The function respects the --end-date filter mode.
The function respects the --min-distance filter mode.
The function respects the --max-distance filter mode.
The function respects the --min-velocity filter mode.
The function respects the --max-velocity filter mode.
The function respects the --min-diameter filter mode.
The function respects the --max-diameter filter mode.
The function respects the --hazardous and --not-hazardous filter modes.
The filters accurately produce results based on the user-specified options.

Query the collection of CloseApproach with a collection of filters. (Task 3b)

The NEODatabase’s query method generates a stream of CloseApproaches that match the filters returned by create_filters.

A CloseApproach is generated if and only if it passes all predicates.
The method generates a stream of matching results, and doesn’t precompute all matching results up front.
Limit the values produced by an iterator to at most a maximum number. (Task 3c)

The limit function slices an iterator to its first n elements, at most.

The function is correct even if the first argument isn’t an in-memory buffered aggregate data type (i.e. list, tuple, etc). That is, the function doesn’t slice directly into the iterator.
The function doesn’t limit the results if the second argument is 0 or None.
Write data from Python to CSV files or JSON files. (Task 4)

The write_to_json function writes a stream of CloseApproach objects to a file in JSON format.

The function opens the file for writing.
The function prepares the stream of results according to the JSON output format specification in the instructions.
The function uses the json module to write the data to the file.
Produce error-free code.

Submitted code passes all test cases and runs without error.

Style (Mechanics)

CRITERIA
MEETS SPECIFICATIONS
Produce Python code that satisfies PEP 8.

Submitted code follows the guidelines of PEP 8 - the Style Guide for Python.

Write Python comments that satisfy PEP 257.

Submitted code follows the docstring conventions of PEP 257.

Each module contains a module-level comment describing the purpose of the module. Complex functions, classes, and methods include a docstring annotating the primary action of the callable in the imperative mood, any additional clarifications, followed by descriptions of parameters and return values.

Submit code free from starter code markings.

There are no # TODO comments left in the submitted code. Portions of comments that say # ELABORATE have been filled in with a description of the corresponding code.

Style (Design)

CRITERIA
MEETS SPECIFICATIONS
Divide attributes appropriately among the NearEarthObject class and the CloseApproach class.

Attributes of NearEarthObjects and CloseApproaches are captured in the constructor from the supplied arguments.

Instances of NearEarthObject don’t have attributes of individual close approaches.

Instances of CloseApproachdon’t have attributes of the associated NEO (except for the primary designation needed to initially link the close approach to its NEO.

Attach functionality to classes only when appropriate.

Standalone functions are used when the functional operation doesn’t depend on external state and does not conceptually belong on an object.

Design a coherent system to filter objects by user-specified criteria.

The logic backing the filter system is consistent and doesn’t contain excess duplicated code.

Consume and produce streams of data as iterables.

Represents concrete data (buffered file contents, static collections of NEOs or close approaches, auxiliary data structures) as concrete.

Represents streaming data (close approaches that match criteria, limited stream of results) as streaming.

Suggestions to Make Your Project Stand Out!
Produce an exciting visualization of the NEO data set. Imagine a series of graphs, in which you plot the relationship between various features, or an infographic-style diagram highlighting interesting elements of the dataset and some key conclusions. Before you begin, take some more time to poke around the data itself. Are there any surprising observations that you can make? Are there any interesting questions that you would like to answer with the data?
Produce an interface to explore other attributes of the data. There are tons of extra fields in our data files representing information about NEOs and their close approaches that we didn’t get to explore in this project.
Explore ways to optimize the performance of your code. See how fast you can make your program run. Submit a writeup demonstrating your choice of benchmark, how you profiled the Python code, and how/why you made any optimizing changes.
Use NASA’s web API to download close approach data for other solar system bodies, such as Mars. You might have to also download new data on more small bodies in the solar system (not just NEOs anymore!).
From a fixed location (such as your house) predict where you should look in the night sky (and when!) to observe a given NEO. For this, you’ll need to use NASA’s tools for calculating ephemerides (trajectories of celestial bodies).
Explore something else that’s new to you! Ask yourself any question about NEOs that you find interesting, and see if you can answer it with the data and build an interactive tool to explore it.
