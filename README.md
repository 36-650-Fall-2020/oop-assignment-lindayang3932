
 
# Assignments Repository

In this repository, you'll work on your homework assignments and submit your completed assignments for review by the TAs.

### OOPY Concepts Used:




Classes: For this assignment, I created four classes. Three classes to read and process county, country, and state data sets and one abstract class to define file processing methods. More specifically, the read_country class reads and processes the us.csv file and the read_state class reads and processes the us-states.csv file. The read_county class reads and processes the us-counties.csv file and obtains user inputs. Lastly, the abstract class read_module is used to ensure that the read_country class and its children implement methods to process the csv file and to reformat the date. 

Objects: The three non abstract classes are used to create objects. The objects are defined in the main.py file. We have an three objects: one for county, country, and state data file.

Initalizers/Constructors: When initializing the objects in the main.py we use the constructor in the parent class, which is the read_country class. The constructor in read_country is used in the read_state and read_county classes. This constructor takes a file name as in input. 

Class attributes and methods: Each non-abstract class has attributes to store the file name and pandas dataframe. The methods and attributes in the read_country class are inherited by the read_state and read_county classes. The attributes in read_country are: file, data_frame (original data frame), USA_stats (output data frame after manipulatin original file). The methods in this class are:  constructor, read_file, date_format, and country_stats (used to calculate the deaths and cases for the us.csv file). These methods and attributes are inherited to the read_state. Read_state has a one attribute to store the pandas data frame and one method to calculate state-level statistics. Read_county inherirates the methods and attributes from the read_state and the read_country classes. The read_county class has attributes and classes that aren't inherited by any other classes

Inheritance: My read_country class is a parent to the read_state class which is also a parent to the read_county classes. Thus read_state inherates methods, constructors, and attributes from read_country. Similarly, read_county inherates methods, constructors, and attributes from read_country and read_state.

Abstract classes: read is my only abstract class. The read class has two abstract methods read_file() and date_reformat(). I chose these to be my abstract methods that the child class read_country would have to implement because all files need to be read and the date column needs to be reformatted regardless of data file type. 

![alt](https://github.com/36-650-Fall-2020/oop-assignment-lindayang3932/blob/master/sonarcube.png)