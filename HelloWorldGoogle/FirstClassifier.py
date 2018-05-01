from scipy.spatial import distance

def Distance(z1, z2): 
    return distance.euclidean(z1,z2)

## Based on k Nearest Neighbour algorithm for k = 1
class MyClassifier:
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        pass

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.Closest(row)
            predictions.append(label)
        return predictions    


    def Closest(self, row):
        best_index = 0
        best_dist = Distance(self.X_train[0], row)

        for i in range(len(self.X_train)):
            if Distance(self.X_train[i], row) < best_dist:
                best_dist = Distance(self.X_train[i], row)
                best_index = i

        return self.y_train[best_index]
