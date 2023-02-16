import csv

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def get_data(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f,delimiter=';')
        dataset = list(csv_reader)[1:]
    final_data = []
    for t in dataset:
        last_ind = len(t)-1
        row = [float(t[i]) for i in range(len(t)) if i != last_ind]
        row.append(t[last_ind])
        final_data.append(row)

    return final_data

def divide_data(dataset):
    good_classes = [row for row in dataset if row[-1] == 'good']
    bad_classes = [row for row in dataset if row[-1] == 'bad']

    train_set = good_classes[:int(0.7*len(good_classes))] + bad_classes[:int(0.7*len(bad_classes))]
    val_set = good_classes[int(0.7*len(good_classes)):int(0.8*len(good_classes))] + \
              bad_classes[int(0.7 * len(bad_classes)):int(0.8* len(bad_classes))]
    test_set = good_classes[int(0.8*len(good_classes)):] + bad_classes[int(0.8*len(bad_classes)):]

    return train_set, val_set, test_set

if __name__ == '__main__':
    dataset = get_data('winequality.csv')

    train_set, val_set, test_set = divide_data(dataset)

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]


    classifier = MLPClassifier(10,activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10,activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10,activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    scaler = StandardScaler()
    scaler.fit(train_x)
    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)

    classifier.fit(train_x, train_y)
    classifier2.fit(scaler.transform(train_x), train_y)
    classifier3.fit(scaler2.transform(train_x), train_y)

    acc = 0
    predictions = classifier.predict(val_x)
    for true, pred in zip(val_y, predictions):
        if true == pred:
            acc += 1
    acc = acc / len(predictions)

    acc2 = 0
    predictions2 = classifier2.predict(scaler.transform(val_x))
    for true, pred in zip(val_y, predictions2):
        if true == pred:
            acc2 += 1
    acc2 = acc2 / len(predictions2)

    acc3 = 0
    predictions3 = classifier3.predict(scaler2.transform(val_x))
    for true, pred in zip(val_y, predictions3):
        if true == pred:
            acc3 += 1
    acc3 = acc3 / len(predictions3)

    print(f"Bez normalizacija imame tochnost: {acc}")
    print(f"So stander scaler normalizacija imame tochnost: {acc2}")
    print(f"So min-max scaler imame tochnost: {acc3}")


    tp, tn, fp, fn = 0,0,0,0

    final_predictions = classifier2.predict(scaler.transform(test_x))

    for true, pred in zip(test_y, final_predictions):
        if true == 'good':
            if pred == true:
                tp += 1
            else:
                fn += 1
        else:
            if pred == true:
                tn += 1
            else:
                fp += 1

    accuracy = (tp+tp)/(tp+tn+fn+fp)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


