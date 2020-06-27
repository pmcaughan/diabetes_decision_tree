import node 
import pandas as pd

class Tree:
    def __init__(self, root=node.Node(), max_depth=9, min_impurity=0.0):
        self.max_depth = max_depth
        self.root=root
        self.min_impurity = min_impurity

    def create(self, df):
        print("Starting Tree Creation")
        self.root.recursive_create(df,self.max_depth, self.min_impurity)
        print("Creation Complete")

    def evaluate(self, series):
        return self.root.recursive_evaluate(series)



