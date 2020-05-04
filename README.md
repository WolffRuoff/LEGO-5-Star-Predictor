# The Lego Rating Predictor #

## Introduction ##
When most people think of Denmark, one of the first things to pop into their minds is LEGO. LEGO, a Danish company founded in 1932, is now the largest toy company in the world with an annual revenue of $2.1 billion USD. As two students who were studying in Denmark, we thought it would be appropriate to base our data analysis project on one of the cornerstones of the Country we had the honor to stay in.

We decided to explore what makes LEGO so popular. Specifically, we were curious what aspects of a LEGO set yield the best ratings on a 5.0 scale. We found two datasets on Kaggle.com that had valuable information about the LEGO inventory. The first, found [here](https://www.kaggle.com/rtatman/lego-database), was filled with useful information, from different colored bricks to the different set and theme names. All the CSVs that linked together to via different ids, as you can see below.

![Set1](./Images/Set1.png)

The second dataset, found [here](https://www.kaggle.com/mterzolo/lego-sets), had other numerical information like the list price, piece count and 5.0-star rating of each product. The CSV also had columns for set name and theme name, allowing us to link the two datasets together as a Pandas dataframe. We then used Pandas, MatPlotLib, and SKLearn to create graphs and a Gaussian Naive Bays classifier from our data.

## Graphs


#### Graph 1: Frequency of the Star Ratings
![Graph 1](./Images/Graph1.png)

#### Graph 2: Review Difficulty vs. Average Star Ratings
![Graph 2](./Images/Graph2.png)

For this graph we decided to see how the review difficulty of a LEGO set influences its overall star rating. To properly illustrate this, we decided to create a box and whisker plot because it not only shows the median and quartiles, but it also shows if there are any outliers.

#### Graph 3: List Price Vs. Star Rating
![Graph 3](./Images/Graph3.png)
![Graph 3.5](./Images/Graph3_5.png)

#### Graph 4:
![Graph 4](./Images/Graph4.png)
![Graph 4.5](./Images/Graph4_5.png)

## Machine Learning


![Machine Learning Results](./Images/MLResults.png)


## Conclusion
