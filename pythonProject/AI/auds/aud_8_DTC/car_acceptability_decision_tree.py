import csv

from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

"""
Decision Tree Classifier
"""

def read_data(data):
    with open(data) as doc:
        csv_reader = csv.reader(doc,delimiter=',')
        data_set = list(csv_reader)[1:]
    return data_set


if __name__ == '__main__':
    dataset = read_data('cars.csv')

    encoder = OrdinalEncoder()

    encoder.fit([x[:-1] for x in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [x[:-1] for x in train_set]
    train_y = [y[-1] for y in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [x[:-1] for x in test_set]
    test_y = [y[-1] for y in test_set]
    test_x = encoder.transform(test_x)


    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

    """
    criterion => spored koj kriterium sakame da se pravi podelba na atributite vo drvoto.
    predefirano se koristi Gini index, a se koristi i entropy;
    
    random_state => sekogash kje bideme sigurni deka kje dobieme ista podelba i isti
    rezultati so drvoto na odluka.
    """

    classifier.fit(train_x, train_y)

    print(f"Depth: {classifier.get_depth()}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1


    print(f"Accuracy: {accuracy / len(test_set)}")

    feature_importances = list(classifier.feature_importances_)
    print(f"Feature importances: {feature_importances}")

    """
    koja karakteristika vlijalela najmnogu/najmalku vo procesot na treniranje
    (najvazhna, najmalku vazhna)
    """

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f"Most important feature: {most_important_feature}")
    least_important_feature = feature_importances.index(min(feature_importances))
    print(f"Least important feature: {least_important_feature}")



    train_x_2 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x_2.append(row)

    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(row)

    train_x_3 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        train_x_3.append(row)

    test_x_3 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        test_x_3.append(row)


    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x_2,train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x_3,train_y)


    print(f"Depth (without most important feature): {classifier2.get_depth()}")
    print(f"Number of leaves (without most important feature): {classifier2.get_n_leaves()}")

    """
    ima povekje listovi kaj classifier2.get_n_leaves() bidejkji e otstraneta najvazhnata karakteristika
    i mnogu potesko kje nauchi da gi klasificira tie primeroci
    
    """

    print(f"Depth (without least important feature): {classifier3.get_depth()}")
    print(f"Number of leaves (without least important feature): {classifier3.get_n_leaves()}")

    accuracy_2 = 0
    for i in range(len(test_x_2)):
        predicted_class_2 = classifier2.predict([test_x_2[i]])[0]
        true_class_2 = test_y[i]
        if predicted_class_2 == true_class_2:
            accuracy_2 += 1

    print(f"Accuracy 2: {accuracy_2/len(test_x_2)}")

    accuracy_3 = 0
    for i in range(len(test_x_3)):
        predicted_class_3 = classifier3.predict([test_x_3[i]])[0]
        true_class_3 = test_y[i]
        if predicted_class_3 == true_class_3:
            accuracy_3 += 1

    print(f"Accuracy 3: {accuracy_3 / len(test_x_3)}")

    print()

