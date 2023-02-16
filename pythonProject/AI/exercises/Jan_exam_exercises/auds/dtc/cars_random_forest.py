import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier


def get_data(file):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        data_set = list(csv_reader)
    return data_set


if __name__ == '__main__':
    dataset = get_data('cars.csv')

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

    classifier = RandomForestClassifier(n_estimators=150,criterion='entropy',random_state=0)
    classifier.fit(train_x, train_y)

    counter = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            counter += 1

    print(f"Accuracy: {counter/len(test_set)}")

    feature_imporances = list(classifier.feature_importances_)
    most_important_feature = feature_imporances.index(max(feature_imporances))
    least_important_feature = feature_imporances.index(min(feature_imporances))

    print(f"Feature importances: {feature_imporances}")

    print(f"Most important feature: {most_important_feature}")
    print(f"Least important feature: {least_important_feature}")


    print()

