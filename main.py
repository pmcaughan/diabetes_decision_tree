import pandas as pd
import tree

df = pd.read_csv("diabetes.csv")

# Randomly split 80% of the file into a training set, the 
#  rest into test
train_df = df.sample(frac=0.8,random_state=200)
test_df = df.drop(train_df.index)

decider = tree.Tree(max_depth = 10)

decider.create(train_df)

num_correct = 0
num_wrong = 0
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

test_len = len(test_df)
current = 1
for item, row in test_df.iterrows():
    print(" --- ")
    print("Item",current,"/", test_len)
    current += 1
    # print(row)
    guess = decider.evaluate(row)
    print("I think :", guess)
    print("\t- Real value:", bool(row['Outcome']))
    if(guess == bool(row['Outcome'])):
        num_correct += 1
        if(guess == True):
            true_positives += 1
        else:
            true_negatives += 1
    else:
        num_wrong += 1
        if(guess == True):
            false_positives += 1
        else:
            false_negatives += 1
    print("\t- Current Accuracy:", num_correct / (num_correct + num_wrong))

print("Completed.")
print("\tCorrect Guesses:", num_correct)
print("\tPrecision:", true_positives / (true_positives + false_positives))
print("\tRecall:", true_positives / (true_positives + false_negatives))
print("\tFalse Positives:", false_positives)
print("\tFalse Negatives:", false_negatives)
print("\tTrue Positives:", true_positives)
print("\tTrue Negatives:", true_negatives)

