# GMIT Data Representation Module Project 2020.
## Higher Diploma in Data Analytics, Lecturer: Andrew Beatty
### Karolina Szafran-Belzowska, G00376368

This project has been carried out as an assignment of the Data Representation module of the Higher Diploma In Data Analytics at GMIT.

### The repository contains:


- README.md file
- .gitignore
- (not yet) mySQL database
- Python 'DAO' programme to access the mySQL database, this programme consumes an API. (EmployeeDAO.py, testEmployeeDAO.py- it was used to test the DAO.)
- Python 'application' to run a Flask server (server.py)
- createDBproject.py - code to create the database ('dr_project')
- (not yet)Several html pages and associated JavaScript and css files as a user interface



### DAO
DAO stands for Data Access Object. The EmployeeDAO.py file consists of a number of functions which access the database and perform CRUD operations. 
It is a pattern that provides an abstract interface to some type of database or other persistence mechanism. The DAO provides some specific data operations without exposing details of the database[1].

###

### MySQL database & table
Database = dr_project
Table = employee

MySQL command to create employee table:
```
create table employee (
    employee_ID int NOT NULL PRIMARY KEY,
    employee_Name varchar(100),
    employee_Dept_ID int,
    employee_Salary int
);
```









### References
[1] https://en.wikipedia.org/wiki/Data_access_object, 05/12/2020
