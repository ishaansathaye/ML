# Databases and SQL for Data Science Notes

### Intro Databases
- SQL language to manipulate databases
- SQL (Structured Query Language)
    - Language used for relational databases
    - Query data
- Data
    - Facts (words, numbers)
- Database
    - Repo of data
    - Provides the functionality of adding, modifying and querying that data
    - Different kinds of DBs store data in different forms
    - Data stored in tabular form is a **relational database**
- RDBMS (Relational Database Management System)
    - Set of software tools that control the data
    - Backbone of applications
- __Commands__
    - CREATE
    - INSERT
    - SELECT
    - UPDATE
    - DELETE
- **Creating a Database Instance on Cloud**
    - Database Service Instance = logical abstractions for managing workloads in a database
    - Python uses SQL to communicate with Database Instance

### Basic SQL
- DDL (Data Definition Language): define, change, or drop data
- DML (Data Manipulation Language): read and modify data
- **CREATE TABLE Statement**
    - DDL statement used to create a table 
    - General Syntax:
    ```SQL
    create table TABLENAME (
    COLUMN1 datatype,
    COLUMN2 datatype,
    COLUMN3 datatype,
        ...
    ) ;
    ```
- **SELECT Statement**
    - DML statement used to read and modify data
    - WHERE predicate = used in search condition
    - Output is called a result set
    - General Syntax:
    ```SQL
    select COLUMN1, COLUMN2, ... from TABLE1 ;
    select * from COUNTRY //Retrieve all the coloumns
    select * from COUNTRY where ID < 5 ;
    ```
    - COUNT()
        - Built-in function that retrieves the number of rows matching the query criteria
    - DISTINCT
        - Used to remove duplicate values from a result set
    - LIMIT
        - Used for restricting the number of rows retrieved from that database
- **INSERT Statement**
    - DML statement used to insert new rows
    - General Syntax:
    ```SQL
    INSERT INTO [TableName]
    <([ClolumnName],...)>
    VALUES([Value],...)
    ```
- **UPDATE AND DELETE Statements**
    - Update statement used to alter data
    - General Syntax:
    ```SQL
    UPDATE [TableName]
    SET [[ColumnName]=[Value]]
    <WHERE [Condition]>
    ```
    - Delete statement used to remove rows
    - General Syntax:
    ```SQL
    DELETE FROM [TableName]
    <WHERE[Condition]>
    ```

### Relational Database Concepts
- Information Model = abstract model for designers and operators
    - Hierarchical Model
- Data Models = concrete and detailed model for implementors
    - Relational Model
        - Most used, allows for data independence, and data stored in tables
        - ER Model (Entity-Relationship Model)
            - Used as a tool to design relational databases
            - Building blocks: entities and attributes
- Types of Relationships between Entities
    - Building blocks of a relationship 
        - Entities sets, relationship sets, and crows foot notations
    - One to One Relationship
    - One to Many or Many to One Relationship
    - Many to Many Relationship
- Mapping Entities to Tables
    - Entity becomes the table 
    - Attributes become the columns
- Relational Model Concepts
    - Building blocks:
        - Relation
            - Relational Schema: name and attributes of the relation
            - Relational Instance: table made up of attributes or columns
            - Degree = the number of attributes in relation
            - Cardinality = the number of tuples
        - Sets

### String Patterns, Ranges, Sorting, and Grouping
- String Patterns
    - Use 'like' predicate for patterns and use '%'
    - Instead of comparison operators use: between...and/IN
- Sorting Result Sets
    -  Alphabetical: order by
    - order by desc = descending order
    - order by 2 = specifying column sequence number
- Grouping Result Sets
    - distinct() = eliminates duplicates
    - group by = grouped elements 
    - having = used with 'group by' 

### Functions, Sub-Queries, Multiple Tables
- Built-in Functions
    - Aggregate or Column Functions = input collection and output single value
        - SUM(), MIN(), MAX(), AVG()
    - Scalar and String Functions = perform operations on every input value
        - ROUND(), LENGTH(), UCASE(), LCASE()
    - DATE
        - YYYYMMDD
    - TIME
        - HHMMSS
    - TIMESTAMP
        - YYYXXDDHHMMSSZZZZZZ
- Sub-Queries and Nested Selects
    - Sub-query = a query inside another query
    - Sub-query can be thought of as nested for loops
- Querying Multiple Tables
    - Ways to access multiple tables in the same query:
        - Sub-queries
        - implicit JOIN
        - JOIN operators (INNER JOIN, OUTER JOIN...)

### Accessing databases using Python
- Python supports Relational Databases
- A user uses python script to use API calls to access databases
- Writing code using __DB-API__
    - Apply this code to any database with python
    - Connection Objects
        - Database connections
        - manage transactions
    - Cursor Objects
        - Database queries
    - Connection Methods
    ```python
        cursor()
        commit()
        rollback()
        close()
    ```
    - Cursor Methods
    ```python
        callproc()
        execute()
        executemany()
        fetchone()
        fetchmany()
        fetchall()
        nextset()
        Arraysize()
        close()
    ```
    - Sample Code using DB-API
    ```python
    from dbmodule import connect

    #Create connection object
    Connection = connect('databasename','username','pswd')

    #Create a cursor object
    Cursor = connection.cursor()

    #Run Queries
    Cursor.execute('select * from mytable')
    Results = cursor.fetchall()

    #Free resources
    Cursor.close()
    Connection.close()
    ```
- Connecting to database using **ibm_db API**
    ```python
    import ibm_db
    
    driver = ''
    database = ''
    hostname = ''
    port = ''
    protocol = ''
    uid = ''
    pwd = ''

    try: 
        conn = ibm_db.connect(dsn, '', '')
        print('Connected')
    except:
        print('Unable to connect to database!')
    
    ibm_db.close(conn)
    ```

### Using JOIN operations to work with multiple tables
- JOIN operator
    - Combines rows from two or more tables
    - Based on a relationship
- Inner Join
    - Matches results from tables
- Left Outer Join
    - Matches all rows from the left table and any matching rows from the right table
- Right Outer Join
    - Matches all rows from the right table and any matching rows from the left table
- Full Outer Join
    - Matches all row from both tables

### Working with Real-World Data Sets and built-in SQL Functions
- 
