import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder


def read_file(file):
    with open(file) as doc:
        dataset = list(csv.reader(doc,delimiter=','))[1:]
    dataset_v2 = []

    for row in dataset:
        row_v2 = [int(el) for el in row]
        dataset_v2.append(row_v2)
    return dataset_v2


if __name__ == '__main__':
    dataset = read_file('medical_data.csv')

    """
    koga koristime Gausov NB klasifikator ne e potrebno da koristime ordinal encoder,
    samiot model kje znae da go napravi toa; znae kako da se spravi so neprekinati vrednosti
    
    kje gi iskoristime tie podatooci i kje gi pratime na GaussianNB classifikator
    
    """


    train_set = dataset[:int(0.7*len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    accuracy = 0
    classifier = GaussianNB()
    classifier.fit(train_x, train_y)


    for i in range(len(test_set)):
        predicted = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted == true_class:
            accuracy += 1


    print(accuracy/len(test_set))

    entry = [int(el) for el in input().split(" ")]


    """
    koga prakjame neshto na f-jata predict(), taa ochekuva
    lista od listi, a nie bidejkji prakjame samo eden primerok, 
    treba da se predade kako posebna lista .predict([entry])
    """
    predicted_class = classifier.predict([entry])[0]
    print(predicted_class)


    """
    vrakja verojatnosti za klasnite tipovi (vo sluchajov bidejkj imame 2 (0 i 1), kje
    vrati dve verojatnosti). I onaa vrednost koja shto e povisoka toa e taa vrednost
    koja shto kje ja dobieme kako predviduvanje so ovoj model
    
    verojatnosti za predviduvanja za sekoja od klasite za daden zapis <- predict.proba()
    """
    print(classifier.predict_proba([entry]))
