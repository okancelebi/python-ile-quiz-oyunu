quiz = {
    "Soru 1": {
        "Soru": "Fransa'nin başkenti neresidir?",
        "Cevap": "Paris"
    },
    "Soru 2": {
        "Soru": "Almanya'nin başkenti neresidir?",
        "Cevap": "Berlin"
    },
    "Soru 3": {
        "Soru": "İtalya'nin başkenti neresidir?",
        "Cevap": "Roma"
    },
    "Soru 4": {
        "Soru": "İspanya'nin başkenti neresidir?",
        "Cevap": "Madrid"
    },
    "Soru 5": {
        "Soru": "Türkiye'nin Başkenti neresidir?",
        "Cevap": "Ankara"
    },
}

score = 0

for key, value in quiz.items():
    print(value['Soru'])
    answer = input("Cevap? ")

    if answer.lower() == value['Cevap'].lower():
        print('Doğru!')
        score = score+1
        print("Skorun : " + str(score))

    else:
        print("Yanliş!")
        print("Cevap :" + value['Cevap'])
        print("Skorun :" + str(score))