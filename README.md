# EXPERIMENT 4 - Data Wrangling and Data Visualization

## I. Intended Learning Outcomes

1. To identify the codes and functions needed in cleaning and visualizing data
2. To be able to apply and use the different codes and functions in creating a Python program that willbe used in data wrangling and data visualization

## II. Materials Used
1. [Boards File](https://bit.ly/ECEBoardExamDataset)
2. Jupyter Notebook
3. ChatGPT

## III. Instructions
1. Write a Python script/code in the Jupyter Notebook to do the given problems.
2. Submit your Jupyter notebook in the dedicated submission bin.

## IV. ECE BOARD EXAM PROBLEM: 
Using data wrangling and data visualization technique with storytelling, analyze the data and present different (i) data frames; and (ii) visuals using the dataset given.

**Part 1:**
Create the following data frames based on the format provided:
1. Filename: Instru = [“Name”, “GEAS”, “Electronics >70”]; where track is constant as Instrumentation and hometown Luzon
2. Filename: Mindy = [ “Name”, “Track”, “Electronics”, “Average >=55”]; where hometown is constant as Mindanao and gender Female

**Part 2:**
Create a visualization that shows how the different features contributes to average grade. Does chosen track in college, gender, or hometown contributes to a higher average score?

## IV. Solutions
Set up the libraries for numerical computing, data manipulation, and mathematical operations.
``` js
import pandas as pd
```
Load the corresponding .xlsx file into a data frame named 'boards'
```js
boards = pd.read_excel("board2.xlsx")
boards
```
> [!NOTE]
> The boards file must be on the same folder as the notebook

### ***Part 1***
> **1. Filename: Instru = [“Name”, “GEAS”, “Electronics >70”]; where track is constant as Instrumentation and hometown Luzon**

```js
Instru = boards.loc[(boards['Hometown'] == 'Luzon') & (boards['Track'] == 'Instrumentation') & (boards['Electronics'] > 70), ['Name','GEAS','Electronics']]
Instru
```
**Explanation**

_`boards['Hometown'] == 'Luzon` : filters rows where the Hometown column has the value 'Luzon'._

_`boards['Track'] == 'Instrumentation'` : filters the rows to include only those where the Track column has the value 'Instrumentation'_

_`boards['Track'] == 'Instrumentation'` : includes rows where the Electronics score is greater than 70._

> **2. Filename: Mindy = [ “Name”, “Track”, “Electronics”, “Average >=55”]; where hometown is constant as Mindanao and gender Female**

```js
boards['Average'] = round(boards[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1),2)
Mindy = boards.loc[(boards['Hometown'] == 'Mindanao') & (boards['Gender'] == 'Female') & (boards['Average'] >= 55), ['Name','Track','Electronics', 'Average']]
Mindy
```
**Explanation**

_`boards[['Math', 'Electronics', 'GEAS', 'Communication']]` : Selects the columns Math, Electronics, GEAS, and Communication from the boards DataFrame_

_`.mean(axis=1)` : Computes the mean (average) across these columns for each row (student)_

_`round(..., 2)` : Rounds the computed average to two decimal places._

_`boards['Average'] = ...` : Creates a new column named Average in the boards DataFrame to store these rounded average scores_


### ***Part 2***
> **Create a visualization that shows how the different features contributes to average grade. Does chosen track in college, gender, or hometown contributes to a higher average score?**

Importing plt for graphs
   ```js
   import matplotlib.pyplot as plt
   ```

   ```js
   plt.figure(figsize=(5, 2))
   plt.bar(boards['Hometown'],boards['Average'])
   ```
**Explanation**

  _`plt.figure()` : Initializes a new figure for plotting._
  
  _`figsize=(5, 2)` : Sets the size of the figure to 5 inches wide and 2 inches tall_

 _`plt.bar()` : Creates a bar plot._

 _`boards['Hometown']` : Specifies the categorical data for the x-axis_

  _`boards['Average']` : Specifies the heights of the bars, which correspond to the average scores for each hometown_


```js
plt.figure(figsize=(5,1))
plt.bar(boards['Gender'],boards['Average'])
```
**Explanation**

 _`plt.figure()` : Initializes a new figure for plotting._
  
  _`figsize=(5, 2)` : Sets the size of the figure to 5 inches wide and 2 inches tall_

 _`plt.bar()` : Creates a bar plot._

 _`boards['Gender']` : Specifies the categorical data for the x-axis_

  _`boards['Average']` : Specifies the heights of the bars, which correspond to the average scores for each gender_


```js
plt.figure(figsize=(5,2))
plt.bar(boards['Track'],boards['Average'])
```
**Explanation**

_`plt.figure()` : Initializes a new figure for plotting._
  
  _`figsize=(5, 2)` : Sets the size of the figure to 5 inches wide and 2 inches tall_

 _`plt.bar()` : Creates a bar plot._

 _`boards['Track']` : Specifies the categorical data for the x-axis_

  _`boards['Average']` : Specifies the heights of the bars, which correspond to the average scores for each track

## V. Other Informations
Author: Daphne P. Robleado

Section: 2ECE-A

## VI. See Version History
* 4 Readme file completed
* 3 Uploaded Final Notebook and .py files
* 2 Uploaded Notebook draft
* 1 Repository has been established
