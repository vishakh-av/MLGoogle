# Orange vs Apple
from sklearn import tree
import sys
features = [[140,1], [130,1], [150,1], [170,1]] 
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[150, 0]]))

def main():
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))