
import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


def read_file(file):
    with open(file) as f:
        csv_reader = csv.reader(f,delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset


if __name__ == '__main__':
    dataset = read_file('cars.csv')
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

    classifier = CategoricalNB()

    classifier.fit(train_x, train_y)

    counter = 0
    for i in range(len(test_x)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            counter += 1

    accuracy = counter / len(test_set)

    print(f"Accuracy: {accuracy}")


    entry = [i for i in input().split(" ")]
    encoded_entry = encoder.transform([entry])

    predicted_entry_class = classifier.predict(encoded_entry)[0]
    print(f"Predicted entry class: {predicted_entry_class}")
