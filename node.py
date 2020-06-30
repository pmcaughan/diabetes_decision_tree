import gini

def find_attribute(df):
    # max_gain = float("-inf")
    min_impurity = float("inf")
    for column in df:
        if(column == 'Outcome'):
            continue
        condition = lambda x: x[column] > df[column].median()
        cond_imp = gini.condition_impurity(df,condition)
        # gain = gini.gini_gain(df,condition)
        if(cond_imp <= min_impurity):
            min_impurity = cond_imp
            best_name = column
            # max_gain = gain
    return best_name

class Node:
    def __init__(self, condition=None, left=None, right=None, attribute=None, outcome=None):
        #Condition is a lambda expression to split the data
        self.condition = condition
        self.left = left
        self.right = right
        self.outcome = outcome

    def recursive_create(self, df, height, min_impurity=0):
        num_positive = len(df[df['Outcome'] == 1])
        num_negative = len(df[df['Outcome'] == 0])
        if(num_positive > num_negative):
            self.outcome = True
        else:
            self.outcome = False
        # if(height == 0 or gini.impurity(df) <= min_impurity):
            # self.left = None
            # self.right = None
        #     self.condition = lambda x: True
        #     return
        print("Creating Node")
        print("\tInput df size =", len(df))
        print("\tInput Impurity =", gini.impurity(df))
        print("\tNode Height =", height)
        print("\tInput df =", self.outcome)
        # import pdb; pdb.set_trace()
        self.attribute = find_attribute(df)
        self.condition = lambda x: x[self.attribute] > df[self.attribute].median()
        left_df = df[self.condition(df)]
        right_df = df[self.condition(df) == False]
        print("\tAttribute =",self.attribute)
        print("Node Created.")
        print()

        if(height == 0 or gini.impurity(df) <= min_impurity):
            self.left = None
            self.right = None
            return

        if((len(left_df) == 0) or (gini.impurity(left_df) == 0)):
            self.left = None
        else:
            self.left = Node()
            self.left.recursive_create(left_df,height-1, min_impurity)
        if((len(right_df) == 0) or (gini.impurity(right_df) == 0)):
            self.right = None
        else:
            self.right = Node()
            self.right.recursive_create(right_df,height-1, min_impurity)

    
    def recursive_evaluate(self, series):
        if(self.condition(series)):
            if(self.left == None):
                return self.outcome
            else:
                return self.left.recursive_evaluate(series)
        else:
            if(self.right == None):
                return self.outcome
            else:
                return self.right.recursive_evaluate(series)


