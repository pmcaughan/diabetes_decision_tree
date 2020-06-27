
#Whenever you split, left is yes and right is no


"""
Calculates the gini impurity of a dataframe, which is the percentage of the outcome
column that is not the majority outcome. for example, a dataframe which has 25 1's in 
the outcome and 75 0's would have an impurity of 0.25

Args:
   df: a pandas dataframe with a binary Outcome column
Returns:
    the proportion of the minority element in the dataframe between 0 and 0.5
    0 means the outcome is only 1's or only 0's, 0.5 means they are equally mixed
"""
def impurity(df):
    size = len(df)
    if(size == 0):
        return 0
    num_positive = len(df[df['Outcome'] == 1]);
    num_negative = len(df[df['Outcome'] == 0]);
    return 1 - ((num_positive/size)**2) - ((num_negative/size)**2)

def condition_impurity(df, lam):
    left_df = df[lam(df)]
    left_gini = impurity(left_df)
    right_df = df[lam(df) == False]
    right_gini = impurity(right_df)
    weighted_average = (len(left_df)/len(df))*left_gini
    weighted_average += (len(right_df)/len(df))*right_gini
    return weighted_average

"""
Calculates the gini gain of a certain decider
The higher the gini gain of a lamba expression, the better it is at splitting the data

Args:
    df: the data frame to be split by the divider
    lam: a lambda expression that returns a boolean value to split the data 

Returns:
    the gini gain
"""
def gini_gain(df, lam):
    root_gini = impurity(df)
    left_df = df[lam(df)]
    left_gini = impurity(left_df)
    right_df = df[lam(df) == False]
    right_gini = impurity(right_df)
    return (root_gini - ((len(left_df)/len(df)) * left_gini) + ((len(right_df)/len(df)) * right_gini))
