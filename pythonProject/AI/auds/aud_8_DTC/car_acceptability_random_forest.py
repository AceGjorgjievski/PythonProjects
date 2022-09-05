import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder


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

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [x[:-1] for x in test_set]
    test_y = [y[-1] for y in test_set]
    test_x = encoder.transform(test_x)

    classifier = RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=0)
    classifier.fit(train_x, train_y)

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
    koja karakteristika vijalela najmnogu/najmalku vo procesot na treniranje
    (najvazhna, najmalku vazhna)
    """

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f"Most important feature: {most_important_feature}")
    least_important_feature = feature_importances.index(min(feature_importances))
    print(f"Least important feature: {least_important_feature}")