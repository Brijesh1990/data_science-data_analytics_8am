# What Is Pandas in Python?

1. Pandas is an open-source Python library used for **data manipulation, data analysis, and data cleaning**.

2. It provides simple and powerful data structures for working with tabular, time-series, and labelled data.

3. Pandas is commonly used in data science, data analytics, machine learning, finance, and scientific computing. It is built on top of NumPy and works well with libraries such as **Matplotlib**, **Seaborn**, and **Scikit-learn**.

## Installation and Import

```bash
pip install pandas
```

```python
import pandas as pd
```

`pd` is the standard alias used for Pandas.

## Main Data Structures

### 1. Series

A `Series` is a one-dimensional labelled array. It can contain numbers, strings, dates, or other Python objects.

```python
marks = pd.Series([85, 90, 78], index=["Asha", "Ravi", "John"])
print(marks)
```

### 2. DataFrame

A `DataFrame` is a two-dimensional labelled table with rows and columns. It is similar to a spreadsheet or a database table.

```python
data = {
	"Name": ["Asha", "Ravi", "John"],
	"Age": [20, 21, 19],
	"Marks": [85, 90, 78],
}

students = pd.DataFrame(data)
print(students)
```

## Characteristics of Pandas

1. **Open source** - Pandas is free to use and has a large developer community.
2. **Python-based** - It integrates naturally with Python syntax and tools.
3. **Powerful data structures** - It provides `Series` and `DataFrame` objects.
4. **Labelled data** - Rows and columns can have meaningful labels instead of only numeric positions.
5. **Handles different data types** - A DataFrame can contain integers, floating-point values, strings, Boolean values, dates, and categorical data in different columns.
6. **Missing-data handling** - It can detect, remove, replace, and interpolate missing values such as `NaN`.
7. **Data cleaning** - It supports removing duplicates, changing data types, renaming columns, and correcting inconsistent data.
8. **Data selection and filtering** - Data can be selected by labels, positions, conditions, or expressions using `.loc`, `.iloc`, and Boolean indexing.
9. **Data alignment** - Pandas automatically aligns data by row and column labels during many operations.
10. **Easy importing and exporting** - It can read and write CSV, Excel, JSON, SQL, HTML, Parquet, and other formats.
11. **Efficient data manipulation** - It supports sorting, grouping, aggregation, transformation, pivoting, reshaping, and ranking.
12. **GroupBy operations** - Data can be divided into groups and summarized using functions such as `sum()`, `mean()`, `count()`, and `max()`.
13. **Combining datasets** - It provides `merge()`, `join()`, and `concat()` for combining tables.
14. **Time-series support** - It supports dates, timestamps, date ranges, resampling, shifting, rolling windows, and time-based indexing.
15. **Vectorized operations** - Operations are applied to complete columns or arrays efficiently without writing many explicit loops.
16. **Descriptive statistics** - Functions such as `mean()`, `median()`, `std()`, `describe()`, and `value_counts()` help summarize data.
17. **Hierarchical indexing** - MultiIndex allows multiple index levels for complex data analysis.
18. **Reshaping support** - Data can be converted between wide and long formats using `pivot()`, `pivot_table()`, `melt()`, and `stack()`.
19. **Categorical data support** - Repeated text values can be stored as categories to improve memory usage and analysis.
20. **Visualization integration** - Pandas provides basic plotting through Matplotlib.
21. **SQL-like functionality** - Filtering, grouping, joining, and aggregation resemble common SQL operations.
22. **Extensible ecosystem** - It works with NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, and database tools.
23. **Interactive use** - It is especially convenient in Jupyter Notebook and other interactive environments.
24. **Memory efficient options** - Appropriate data types, categorical columns, and chunked reading can reduce memory usage.
25. **Programmable and reproducible** - Data preparation steps can be written as Python programs or analysis notebooks.

## Common Pandas Operations

```python
print(students.head())                 # First rows
print(students.shape)                  # Number of rows and columns
print(students.columns)                # Column names
print(students["Marks"])              # Select one column
print(students[students["Marks"] > 80]) # Filter rows

students["Passed"] = students["Marks"] >= 40
students = students.sort_values("Marks", ascending=False)
summary = students.groupby("Passed")["Marks"].mean()
```

## Reading and Writing Files

```python
df = pd.read_csv("students.csv")
df.to_csv("clean_students.csv", index=False)

excel_data = pd.read_excel("students.xlsx")
df.to_json("students.json")
```

## Advantages

- Easy to learn for Python users.
- Reduces the amount of code needed for data analysis.
- Provides many built-in cleaning and analysis functions.
- Works with small and moderately large datasets.
- Integrates with most Python data-science libraries.

## Limitations

- Large datasets may require more memory than available.
- It can be slower than specialized database or distributed-processing systems for very large data.
- Complex operations may create copies of data and increase memory usage.
- It is not a replacement for a database, although it can read from and write to databases.

## Conclusion

Pandas is one of the most important Python libraries for working with structured data. Its labelled tables, data-cleaning tools, filtering, grouping, joining, statistical functions, and file-format support make it a standard tool for data analysis.
