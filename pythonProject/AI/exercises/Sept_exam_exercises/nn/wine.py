import csv
from sklearn.neural_network import MLPClassifier


def read_data(file):
    with open(file) as f:
        _ = f.readline()
        data = []
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(";")
            data.append(list(map(float, parts[:-1])) + parts[-1:])
    return data


def divide_sets(dataset):
    good_classes = [x for x in dataset if x[-1] == 'good']
    bad_classes = [x for x in dataset if x[-1] == 'bad']

    train_set = good_classes[:int(len(good_classes) * 0.7)] + bad_classes[:int(len(bad_classes) * 0.7)]
    val_set = good_classes[int(len(good_classes) * 0.7):int(len(good_classes) * 0.8)] + \
              bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)]
    test_set = good_classes[int(len(good_classes) * 0.8):] + bad_classes[int(len(bad_classes) * 0.8):]

    return train_set, val_set, test_set


if __name__ == '__main__':
    dataset = read_data('winequality.csv')

    train_set, val_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]

    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]

    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    classifier1 = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier1.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)


    class_list = [classifier1, classifier2, classifier3]

    max_acc = 0
    final_classifier = None
    for i, c in enumerate(class_list):
        val_predict = c.predict(val_x)
        val_acc = 0
        for x, y in zip(val_y, val_predict):
            if x == y:
                val_acc += 1

        print(f"Klasifikatorot {i+1} ima tochnost : {val_acc/len(val_y)}")
        if val_acc > max_acc:
            max_acc = val_acc
            final_classifier = c


    final_predictions = final_classifier.predict(test_x)

    final_acc = 0
    for x,y in zip(test_y, final_predictions):
        if x == y:
            final_acc += 1

    print(f"Accuracy: {final_acc/len(test_y)}")




