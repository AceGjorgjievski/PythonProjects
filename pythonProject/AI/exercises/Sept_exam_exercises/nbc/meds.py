import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB





def read_data(file):
    with open(file) as f:
        reader = csv.reader(f,delimiter=',')
        dataset = list(reader)[1:]
    return dataset



if __name__ == '__main__':
    dataset = read_data('medical_data.csv')
    print(dataset)

    encoder = OrdinalEncoder()

    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(len(dataset) * 0.7)]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)


    test_set = dataset[int(len(dataset)*0.7):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()

    classifier.fit(train_x,train_y)

    accuracy = 0



    for i in range(len(test_x)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    print(f"Accuracy: {accuracy/len(test_set)}")


    entry = [int(el) for el in input().split(" ")]
    entry_x = encoder.transform(entry)

    predicted_entry = classifier.predict([entry_x])[0]
    print(predicted_entry)





