import os
from tkinter import *

klasor="."
answersList=[]
uzantı=".txt"
for a in os.listdir(klasor):
    dosya = os.path.join(klasor,a)
    if os.path.isfile(dosya):
        if uzantı in a:
            print('dosya= ',a)
            answersList.append(a)

size=len(answersList)
for e in range(0,size):
    for d in range(e+1,size):
        top = Tk()
        text = Text(top)
        f1 = open((answersList[e]), "r")
        f2 = open((answersList[d]), "r")
        liste1 = (f1.readlines())
        liste2 = (f2.readlines())
        newlist = []
        text.insert(INSERT, str(e) + " ile " + str(d) + " Benzer satirlar: \n")
        for i in liste1:
            for j in liste2:
                if i == j:
                    text.insert(INSERT, i)
                    newlist.append(i)
        m = len(liste1)
        n = len(newlist)
        text.insert(INSERT, "\n")
        if n <= (m / 6):
            text.insert(INSERT, "%0-%10 benzerdir.")
        if (m / 6) < n <= (m / 5):
            text.insert(INSERT, "%10-%20 benzerdir.")
        if (m / 5) < n <= (m / 4):
            text.insert(INSERT, "%20-%30 benzerdir")
        if (m / 4) < n <= (m / 3):
            text.insert(INSERT, "%30-%40 benzerdir")
        if (m / 3) < n <= (m / 2):
            text.insert(INSERT, "%40-%50 benzerdir")
        if (m / 2) < n <= (m * (4 / 6)):
            text.insert(INSERT, "%50-%70 benzerdir")
        if (m * (4 / 6)) < n <= (m * (5 / 6)):
            text.insert(INSERT, "%70-%90 benzerdir")
        if (m * (5 / 6)) < n <= m:
            text.insert(INSERT, "%90-%100 benzerdir")
        text.pack()
        top.mainloop()