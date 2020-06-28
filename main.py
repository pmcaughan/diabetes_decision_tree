import pandas as pd
import tree

df = pd.read_csv("diabetes.csv")

# Randomly split 80% of the file into a training set, the 
#  rest into test
train_df = df.sample(frac=0.8,random_state=200)
test_df = df.drop(train_df.index)

decider = tree.Tree()

decider.create(train_df)

num_correct = 0
num_wrong = 0

print(test_df)

for item, row in test_df.iterrows():
    print(" --- ")
    print(row)
    guess = decider.evaluate(row)
    print("I think :", guess)
    print("\t- Real value:", bool(row['Outcome']))
    if(guess == bool(row['Outcome'])):
        num_correct += 1
    else:
        num_wrong += 1
    print("\t- Current Accuracy:", num_correct / (num_correct + num_wrong))

