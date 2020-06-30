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

### Data Wrangling
- Missing Values
    - Drop the variable or drop the entry
    ```python
    dataframes.dropna()#axis=0 for entire row drop/axis=1 for entire column drop
    df.dropna(subset=['price'], axis=0, impace=True)#inplace True modifies the ata
    ```
    - Replace it with an average or frequency
    ```python
    dataframe.replace(missing_value, new_value)
    ```
- Data Formatting
    - Converting data types
    ```python
    df['price'] = df['price'].astype('int')
    ```
- Data Normalization
    - Simple Feature scaling: old/max = new
    ```python
    df['price'] = df['price']/df[['price'].max()
    ```
    - Min-Max: (old-min)/(max-min)
    ```python
    df['price'] = (df['price']-df['price'].min())/(df[['price'].max()-df['price'].min())
    ```
    - Z-score: (old-average)/(standard deviation)
    ```python
    df['price'] = (df['price']-df['price'].mean())/df[['price'].std()
    ```
 - Binning
    ```python
    bins = np.linspace(min(df['price'], max(df['price']), 4)
    group_names = ['Low', 'Medium', 'High']
    df['price-binned'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)
    ```
- Categorical -> Quantitative
    - Assign 0 or 1 (One-hot encoding)
    ```python
    pd.get_dummies(df['fuel'])
    ```
    
### Exploratory Data Analysis
- Descriptive Statistics
    - Summarize categorical data by using: `value_counts()`
    - Box Plot: `sns.boxplot(x='drive-wheels', y='price', data=df)`
    - Scatter Plot: `plt.scatter(x,y)` using matplotlib
- GroupBy
    - `dataframe.Groupby()`
    - Pandas method `pivot()` makes table look like excel sheet
    - Heat-map `plt.pcolor(df_pivot, cmap='RdBu') plt.colorbar()`
- ANOVA
    - Finding correlation between different groups of a categorical variable
    - F-test score: variation between sample group means divided by variation within sample group
    - P-value: confidence degree
    ```python
    df_anova = df[['make', 'price']]
    grouped_anova = df_anova.groupyby(['make'])
    stats.f_oneway() #From sci-kit
    ```
- Correlation
    - Measures to what extent different variables are interdependent
    - Use `sns.regplot()`
    - Positive/Negative linear relationship
- Correlation - Statistics
    - Pearson Correlation
        - Correlation coefficient
            - Close +1: Large positive relationship
            - Close to -1: Large negative relationship
            - Close to 0: No relationship
        - P-value
            - < 0.001: strong certainty in result
            - < 0.05: moderate
            - < 0.1: weak
            - Greater 0.1: none
        - `pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])`
