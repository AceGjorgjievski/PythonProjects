import csv
from sklearn.neural_network import MLPClassifier


def get_data(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=';')
        dataset = list(csv_reader)[1:]
    final_data = []
    for t in dataset:
        row = [float(t[i]) for i in range(len(t)) if i != len(t) - 1]
        class_attr = t[-1]
        row.append(class_attr)
        final_data.append(row)

    return final_data


def divide_data(dataset):
    good_classes = [row for row in dataset if row[-1] == 'good']
    bad_classes = [row for row in dataset if row[-1] == 'bad']

    train_set = good_classes[:int(0.7 * len(good_classes))] + bad_classes[:int(0.7 * len(bad_classes))]
    valid_set = good_classes[int(0.7 * len(good_classes)):int(0.8 * len(good_classes))] + \
                bad_classes[int(0.7 * len(bad_classes)):int(0.8 * len(bad_classes))]
    test_set = good_classes[int(0.8 * len(good_classes)):] + bad_classes[int(0.8 * len(bad_classes)):]

    return train_set, test_set, valid_set


if __name__ == '__main__':
    dataset = get_data('winequality.csv')

    train_set, test_set, valid_set = divide_data(dataset)

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_x = [row[:-1] for row in valid_set]
    val_y = [row[-1] for row in valid_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)

    final_classifier = None
    max_accuracy = 0
    for i, c in enumerate([classifier, classifier2, classifier3]):
        counter = 0
        predictions = c.predict(val_x)
        for pred, true in zip(predictions, val_y):
            if pred == true:
                counter += 1

        accuracy = counter / len(val_x)
        print(f"Klasifikator {i} ima tochnost: {accuracy}")

        if accuracy > max_accuracy:
            max_accuracy = accuracy
            final_classifier = c

    acc = 0
    final_predictions = final_classifier.predict(test_x)
    for pred, true in zip(final_predictions, test_y):
        if pred == true:
            acc += 1

    acc = acc / len(test_x)

    print(f"Tochnosta vrz testirachkoto mnozhestvo e: {acc}")
