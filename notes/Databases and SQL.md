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

