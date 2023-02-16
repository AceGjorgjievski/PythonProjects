import csv

from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import GaussianNB



def read_data(file):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',')
        dataset = list(csv_reader)[1:]
    dataset_v2 = []

    for row in dataset:
        row_v2 = [int(el) for el in row]
        dataset_v2.append(row_v2)
    return dataset_v2

if __name__ == '__main__':
    dataset = read_data('medical_data.csv')

    train_set = dataset[:int(0.7*len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    counter = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            counter += 1

    accuracy = counter / len(test_set)

    print(f"Accuracy: {accuracy}")

    entry = [int(i) for i in input().split(" ")]
    predicted_entry_class = classifier.predict([entry])[0]
    print(f'Predicted entry class: {predicted_entry_class}')

    entry_proba = classifier.predict_proba([entry])
    print(f"Predicted entry probability: {entry_proba}")



