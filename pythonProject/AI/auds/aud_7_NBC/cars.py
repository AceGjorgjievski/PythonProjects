import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

"""
naive bayes classifier

"""

def file_reader(file):
    with open(file) as doc:
        csv_reader = csv.reader(doc,delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset


if __name__ == '__main__':
    dataset = file_reader('cars.csv')

    encoder = OrdinalEncoder()# gi mapira site kategoriski atributi vo numerichki vrednosti

    encoder.fit([row[:-1] for row in dataset])# gi davame karakteristikite bidejkji sakame da gi mapirame samo niv
    # od koi podatoci treba da go nauchi toa mapiranje (site karakteristiki, osven poslednata kolona koja shto e klasa)

    """
    go delime podatochnoto mnozhestvo na dve pod-mnozhestva
    """
    #prvite procenti se zemaat za teniranje (vo sluchajov prvite 70%)
    train_set = dataset[:int(0.7*len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x) # da se napravi transformacija od soodvetna karakteristika vo celobrojna vrednost i
    # da se iskoristi encoderot shto vekje e istreniran, vekje znae kako da go pravi toa mapiranje


    """
    kaj encoder.fit() ima funkcii koi shto kje nauchat deka treba da se mapira; 
    gi naogja site vrednosti koi shto se unikatni [pr -> small,medium,big i sega small neka e 0, medium e 1, big e 2 itn.. nekoj rechnik
    koj shto sekoja vrednost 'small' kje ja mapira vo vrednost '0']
    potoa koga kje povikame encoder.transform() se koristat tie rechnici i se zamenuvaat tie vrednosti predadeni kako vlez
    
    train_x = encoder.transform(train_x)
    
    ako sme pratile nekoja vrednost koja predtoa ne ja 'videle' (ne sme ja predale kaj fit za da nauchi), togash kje ima 
    greshka kaj transform
    
    kaj encoderot gi davame samo karakteristikite, a klasata ja koristime kako takva
    
    
    pravime model koj shto kje ja predviduva klasata; spored nekoi karakteristiki (atributi) da ni dade na izlez klasa
    pr. za nekoj avtomobil ima 2 sedishta, brz e , dupnata guma i slichno -> na izlez kje ni dade kako unacceptable(ili pak na izlez kje 
    ima da/ne) i slichni primeri.. dali ima korona => pokachena temp, kashla, glavobolki itn.. -> na izlez kje dade spored dadeni karakteristiki
    soodvetna klasa da/ne ili ima/nema korona
    
    za daden vlez -> daj ni izlez (vo koja klasa kje pripagja primerok koj shto kje go predademe kako vlez)
    
    kako vo fajlot car.csv
    
    """


    # potoa poslednite procenti se zemaat za testiranje (vo sluchajov 30%)
    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x) # isto kako pogore objasneto

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y) # pravime treniranje samo so podmnozhestvoto za treniranje
    # kje se presmetaat frekvenciite spored Baesovata teorema i potoa koga kje povikame funkcija
    # 'predict()' toj model kje ni kazhe ovoj primerok kje pripagja vo nekoja konkretna klasa


    accuracy = 0
    for i in range(len(test_set)):
        predict_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predict_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)
    print(f"Accuracy: {accuracy}")

    entry = [el for el in input().split(" ")]

    encoded_entry = encoder.transform([entry])

    predicted_class = classifier.predict(encoded_entry)[0]

    print(predicted_class)


