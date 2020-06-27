# Data Analysis with Python Notes

### Importing Datasets
- Importing and Exporting Data in Python
    - Format
    - File Path of dataset
    - Importing a CSV into Python:
    ```python
    import pandas as pd
    url = ""
    df = pd.read_csv(url)
    #Without header:
    df = pd.read_csv(url, header=None)
    ```
    - Putting the data frame into Python
    ```python
    df #Prints entire dataframe
    df.head(n) #Prints first n rows of data frame
    df.tail(n) #Prints last n rows of data frame
    ```
    - Exporting a Pandas data frame to CSV
    ```python
    df.to_csv(path) #Specify path
    ```
    - Basic Insights of Dataset
    ```python
    df.dtypes() #Check data types
    df.describe() #Returns a statistical summary
    df.describe(include="all") #Provides full summary stats
    df.info() #Provides a concise summary of your DataFrame
    ```
    - Accessing Databases with Python
        - 

    