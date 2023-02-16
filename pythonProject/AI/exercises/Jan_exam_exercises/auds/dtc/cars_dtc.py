import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier



def read_data(file):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        dataset = list(csv_reader)
    return dataset

if __name__ == '__main__':
    dataset = read_data('cars.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])


    train_set = dataset[:int(0.7*len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(train_x, train_y)


    counter = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            counter += 1

    print(f"Accuracy: {counter/len(test_set)}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")
    print(f"Depth: {classifier.get_depth()}")




    feature_importances = list(classifier.feature_importances_)
    most_important_feature = feature_importances.index(max(list(classifier.feature_importances_)))
    least_important_feature = feature_importances.index(min(list(classifier.feature_importances_)))

    print(f"Feature imporantances: {feature_importances}")
    print(f"Most important feature: {most_important_feature}")
    print(f"Least important feature: {least_important_feature}")



    train_x_2 = []
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x_2.append(row)

    test_x_2 = []
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(row)

    train_x_3 = []
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        train_x_3.append(row)

    test_x_3 = []
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        test_x_3.append(row)


    classifier2 = DecisionTreeClassifier(criterion='entropy',random_state=0)
    classifier2.fit(train_x_2, train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x_3, train_y)


    feature_importances_2 = list(classifier2.feature_importances_)
    most_important_feature_2 = feature_importances_2.index(max(feature_importances_2))
    least_important_feature_2 = feature_importances_2.index(min(feature_importances_2))

    feature_importances_3 = list(classifier3.feature_importances_)
    most_important_feature_3 = feature_importances_3.index(max(feature_importances_3))
    least_important_feature_3 = feature_importances_3.index(min(feature_importances_3))

    counter2 = 0
    for i in range(len(test_x_2)):
        predicted_class = classifier2.predict([test_x_2[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            counter2 += 1

    print(f"Accuracy2 (without most important feature): {counter2/len(test_x_2)}")

    counter3 = 0
    for i in range(len(test_x_3)):
        predicted_class = classifier3.predict([test_x_3[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            counter3 += 1

    print(f"Accuracy2 (without least important feature): {counter3/len(test_x_3)}")


    print(f"Depth 2 (without most important feature): {classifier2.get_depth()}")
    print(f"Number of leaves 2 (without most important feature): {classifier2.get_n_leaves()}")


    print(f"Depth 3 (without most important feature): {classifier3.get_depth()}")
    print(f"Number of leaves 3 (without most important feature): {classifier3.get_n_leaves()}")


    print()
