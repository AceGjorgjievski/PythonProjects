import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier


def get_data(file):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        dataset = list(csv_reader)[1:]
        return dataset


if __name__ == '__main__':
    dataset = get_data('cars.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(len(dataset)*0.7)]
    train_x = [row[:-1]for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(len(dataset)*0.7):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)


    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

    classifier.fit(train_x, train_y)

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    print(f"Accuracy: {accuracy/len(test_set)}")
    print(f"Depth: {classifier.get_depth()}")
    print(f"Number leaves: {classifier.get_n_leaves()}")

    temp = list(classifier.feature_importances_)

    most_important_features = temp.index(max(temp))
    least_important_features = temp.index(min(temp))


    print(f"Most important feature: {most_important_features}")
    print(f"Least important feature: {least_important_features}")

    # ----  -   -----       ------                  ----#
    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    train_x2 = []
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != most_important_features]
        train_x2.append(row)

    test_x2 = []
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_features]
        test_x2.append(row)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)

    train_x3 = []
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != least_important_features]
        train_x3.append(row)

    test_x3 = []
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != least_important_features]
        test_x3.append(row)


    classifier2.fit(train_x2, train_y)
    classifier3.fit(train_x3, train_y)


    accuracy2 = 0
    for i in range(len(test_x2)):
        predicted_class2 = classifier2.predict([test_x2[i]])[0]
        true_class2 = test_y[i]

        if predicted_class2 == true_class2:
            accuracy2 += 1

    accuracy3 = 0
    for i in range(len(test_x3)):
        predicted_class3 = classifier3.predict([test_x3[i]])[0]
        true_class3 = test_y[i]
        if predicted_class3 == true_class3:
            accuracy3 += 1

    print(f"Accuracy (without most important feature): {accuracy2/len(test_x2)}")
    print(f"Accuracy (without least important feature): {accuracy3/len(test_x3)}")

    print(f"Depth 2(without most important feature) {classifier2.get_depth()}")
    print(f"Depth 3(without most important feature) {classifier3.get_depth()}")

    print(f"Leaves 2 (without most important feature) {classifier2.get_n_leaves()}")
    print(f"Leaves 3 (without most important feature) {classifier3.get_n_leaves()}")





    print()


