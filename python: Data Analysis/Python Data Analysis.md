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

### Model Development
- Linear and Multiple Regression
    - Linear:
    ```python
    from sklearn.linear_model import LinearRegression
    lm = LinearRegression()
    x = df[['highway-mpg']]
    y = df['price']
    lm.fit(x,y)
    y_hat = lm.predict(x)
    ```
    - Multiple: multiple independent variables
    ```python
    z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
    lm.fit(z, df['price'])
    y_hat = lm.predict(x)
    ```
- Model Eval using Visualization
    - Regression Plot:
    ```python
    import seaborn as sns
    sns.regplot(x='', y='', data=df)
    plt.ylim(0,)
    ```
    - Residual Plot
    ```python
    import seaborn as sns
    sns.residplot(df['highway-mpg'], df['price'])
    ```
    - Distribution Plot:
    ```python
    import seaborn as sns
    ax1 = sns.distplot()
    sns.distplot(y_hat,...)
    ```
- Polynomial Regression and Pipelines
    - Quadratic
    - Cubic
    ```python
    f = np.polyfit(x,y,3)
    p = np.polyd(f) #print(p) for printing model equation
    #Poly with multi-variate
    from sklearn.preprocessing import PolynomialFeatures
    pr = PolynomialFeatures(degree=2, include_bias=False)
    ```
    - Higher order
    - Pre-processing: normalize each feature simultaneously
    ```python
    from sklearn.preprocessing import StandardScaler
    SCALE = StandardScaler()
    SCALE.fit(x_data[['horsepower', 'highway-mpg']])
    x_scale = SCALE.transform()
    - Pipelines: used to normalize then transform 
- Measures for In-Sample Evaluation
    - Mean-Squared Error(MSE)
    - R^2 Error (Coefficient of Determination)
- Prediction and Decision Making
    - Determining a Good Model Fit
        - Do the predicted values make sense
        - Visualization
        - Numerical measures for evaluation
        - Comparing Models

### Model Evaluation and Refinement
- Split dataset into test data and train data
    - Usually 80 train and 20 test
    ```python
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=0) #testSize is percentage for testing, randomState is number generator used for random sampling
    ```
    - Cross Validation
        - Most common out-of-sample evaluation metrics
        - More effective use of data
        - Divide the data into equal groups and use one group as test and other groups as traning
    ```python
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(linearModel, x_data, y_data, cv=3) #cv is the number of partitions
    ```
    - Retusn the preduction that was obtained for each element when it was in the test set
    ```python
    y_hat = cross_val_predict(linearModel2e, x_data, y_data, cv=3)
    ```
- Overfitting, Underfitting and Model Seletion
    - Polynomial order should minimize test or Error MSE
- Ridge Regression
    - Prevents overfitting
    - 𝛼 prevents overfitting and decreases the large magnitude of coefficients
        - 0, 0.001 0.01, 0.01, 1, 10
    ```python
    from sklearn.linear_model import Ridge
    RidgeModel = Ridge(alpha=0.1)
    RidgeModel.fit(X,y)
    y_hat = RidgeModel.predict(X)
    ```
- Grid Search
    - Hyperparameters
    - Automatically iterates over hyperparameters using corss-validation
    - Finds which parameters produce the best scores
    ```python
    from sklearn.linear_model import Ridge
    from sklearn.model_selection import GridSearchCV

    parameters1 = [{'alpha':[0.001, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]}]
    RR = Ridge()
    Grid1 = GridSearchCV(RR, parameters1, cv=4)
    Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)
    Grid1.best_estimator_

    socres = Grid1.cv_results_
    scores['mean_test_score']

    #Find best model by seeing normalize hyperparameter test scores
    parameters = [{'alpha':[1, 10, 100, 1000], 'normalize':[True, False]}]
    ```
