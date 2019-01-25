# mortgage-database
Using SQLite and Python, create a database from Fannie Mae's and Freddie Mac's aquisition and performance datasets

## Project Status: Work-in-Progress
After a few previous versions and a long break, I couldn't figure out where I left off. I decided to make a new, modular approach to the database. Instead of one python script to do everything, I'm breaking it down into a series of scripts to be run sequentially. I'm putting a greater focus onto breaking complex tasks into smaller tasks.

### Script 0 - Configuration
#### Status: Ongoing
* Useful code for multiple scripts.
* Variables that are used by multiple scripts.

### Script 1 - Create raw data SQLite database & tables
#### Status: Complete
* Initiallizes the database if doesn't exist
* Creates 4 tables as defined by the following SQL scripts
  * raw_fannie_origination.sql
  * raw_fannie_performance.sql
  * raw_freddie_origination.sql
  * raw_freddie_performance.sql
* NOTE: If you look at any of the .sql files, you'll probably notice that the only datatypes I declare are text and numeric. SQLite does not use "static typing" like the majority of SQL databases. If I were to specify datatypes like varchar(30), SQLite would interpret it as datatype text. There's only 5 storage classes in SQLite, and there are 5 datatype affinities. None, Text, Numeric, Real, Integer. Specific datatype declarations are translated into the closest match for storage class, and retreiving values from storage into datatype is translated into the best-preserving datatype affinity anyways.

### Script 2 - Populate raw tables with data
#### Status: Complete

* Creates a list of every file in ../import/
* Using the filenames, it determines the corresponding table
* Line-by-line, it sends SQL INSERT instructions to the DB
* At the end of the file, it commits all changes
* Continues to work through all the files in the directory
* I felt it was important to do it this way because I wanted the database to be easily updatable. The user can dump a bunch of new data text files into /import/ and the program will import them to where they belong. This is an improvement over past versions that needed a complete set of data files, or to have multiple nested for statements redone. If you only want 1 year's of data, just copy the relevant text files into the folder.

### Script 3 - Create database & tables for cleaned, combined data
#### Status: Not started
