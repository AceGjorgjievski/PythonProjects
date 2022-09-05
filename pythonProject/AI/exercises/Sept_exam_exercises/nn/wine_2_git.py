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

def divide_set(dataset):
    good = [x for x in dataset if x[-1] == 'good']
    bad = [x for x in dataset if x[-1] == 'bad']

    train_set = good[:int(len(good)*0.7)] + bad[:int(len(bad)*0.7)]
    val_set = good[int(len(good)*0.7):int(len(good)*0.8)] + bad[int(len(bad)*0.7):int(len(bad)*0.8)]
    test_set = good[int(len(good)*0.8):] + bad[int(len(bad)*0.8):]

    return train_set, val_set, test_set

if __name__ == '__main__':
    dataset = read_data('winequality.csv')

    train_set, val_set, test_set = divide_set(dataset)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]

    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]

    test_x = [x[:-1]for x in test_set]
    test_y = [x[-1]for x in test_set]

    classifier1 = MLPClassifier(5,learning_rate_init=0.001,max_iter=500,activation='relu', random_state=0)
    classifier2 = MLPClassifier(10,learning_rate_init=0.001,max_iter=500,activation='relu', random_state=0)
    classifier3 = MLPClassifier(100,learning_rate_init=0.001,max_iter=500,activation='relu', random_state=0)

    classes = [classifier1, classifier2, classifier3]

    classifier1.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)


    max_acc = 0
    final_classificator = None
    for i, v in enumerate(classes):
        predictions = v.predict(val_x)
        true = val_y
        acc = 0

        for x,y in zip(true, predictions):
            if x == y:
                acc+=1

        print(f"Klasifikatorot {i+1} ima tochnost {acc/len(val_y)}")
        if acc > max_acc:
            max_acc = acc
            final_classificator = v

    final_predictions = final_classificator.predict(test_x)
    final_acc = 0

    for x,y in zip(test_y, final_predictions):
        if x == y:
            final_acc += 1

    print(f"Finall Accuracy: {final_acc/len(test_y)}")




