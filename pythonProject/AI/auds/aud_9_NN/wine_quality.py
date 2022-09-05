from sklearn.neural_network import MLPClassifier




def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        """
        linija koja ne ni e potrebna
        """
        while True:
            line = f.readline().strip()
            if line == "":
                break
            parts = line.split(";")
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


def divide_sets(dataset):
    bad_classes = [x for x in dataset if x[-1] == 'bad']
    good_classes = [x for x in dataset if x[-1] == 'good']

    train_set = bad_classes[:int(0.7*len(bad_classes))] + good_classes[:int(0.7*len(good_classes))]
    val_set = bad_classes[int(0.7*len(bad_classes)):int(0.8*len(bad_classes))] +\
              good_classes[int(0.7*len(good_classes)):int(0.8*len(good_classes))]
    test_set = bad_classes[int(0.8*len(bad_classes)):] + good_classes[int(0.8*len(good_classes)):]

    return train_set, val_set, test_set




if __name__ == '__main__':
    dataset = read_dataset()
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

    classifier1.fit(train_x,train_y)
    classifier2.fit(train_x,train_y)
    classifier3.fit(train_x,train_y)

    final_classifier = None
    max_acc = 0
    for i, c in enumerate([classifier1, classifier2, classifier2]):
        val_predictions = c.predict(val_x)
        val_acc = 0

        for x,y in zip(val_y,val_predictions):
            if x == y:
                val_acc += 1

        val_acc = val_acc / len(val_y)

        print(f"Klasisfikatorot {i} ima tochnost so validacisko mnozhestvo od {val_acc}")

        if val_acc > max_acc:
            max_acc = val_acc
            final_classifier = c

    acc = 0
    predictions = final_classifier.predict(test_x)

    for x, y in zip(test_y, predictions):
        if x == y:
            acc += 1

    acc = acc / len(test_y)
    print(f'Tochnosta so testirachkoto mnozhestvo e: {acc}')
