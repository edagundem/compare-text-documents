import os
import difflib
file=open('result_list',"w+")
klasor="."
answersList=[]
uzantı=".c"
for a in os.listdir(klasor):
    dosya = os.path.join(klasor,a)
    if os.path.isfile(dosya):
        if uzantı in a:
            print('dosya= ',a)
            answersList.append(a)

size=len(answersList)
for e in range(0 , size):
    file.write("\n****************************** "+ str(e+1)+".dosya ********************************\n\n")
    for d in range(0 , size):
        if e == d:
            continue
        f1 = open((answersList[e]), "r")
        f2 = open((answersList[d]), "r")
        liste1 = (f1.readlines())
        liste2 = (f2.readlines())

        file.write("Dosya " + str(answersList[e]) + " ile " + str(answersList[d]) + " karsilastirildiginda: \n")

        m = len(liste1)
        avg=0
        for i in liste1:
            for j in liste2:
                s = difflib.SequenceMatcher(None, i,j)
                if s.ratio()== 1:
                    avg += 1


        file.write("Benzer satir sayisi: "+ str(avg))
        file.write("\n")
        avg = (avg / m)*1000
        avg= avg//10
        file.write("Benzerlik orani: % "+ str(avg))
        file.write("\n")





















