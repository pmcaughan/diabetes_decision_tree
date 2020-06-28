# Decision Tree Diabetes Predictor
Predictor for whether or not a person has diabetes given a handful of diagnostic measures using ![Decision Tree Learning ](https://en.wikipedia.org/wiki/Decision_tree_learning)

Written in python and made using the ![Pandas Data Analysis API](https://pandas.pydata.org/)

## About

I made this as a personal project during the 2020 COVID Pandemic in my quest to learn and implement various styles of machine learning in place of a lost internship.

This uses ![this publically available dataset of Pima Indian women](https://www.kaggle.com/uciml/pima-indians-diabetes-database) to create and test a decision tree.

When randomly splitting 80% of the database to train and 20% to test, it had an accuracy of 65%

## Future

There are many ways to potentially improve the accuracy of this.
Right now the only criteria used to split the dataset at each node is the median of each given potential variable.
By adding more potential criteria it can be made more accurate. 
Additionally, more could be done to clean up the data before creating the tree, right now its just being fed right in while missing variables and outliers could be accounted for.
