# -*- coding: utf-8 -*-
"""pengolahan data

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o5cfFm-lEQLTdZMdb4q7jfRWsJ_ODtkI
"""

import pandas as pd
import matplotlib.pyplot as plt

#==============Ngoding jangan lupa kopinyaa===========

#PROGRAM PENGELOLAHAN DATA
#PERHITUNGAN
#1.mean
#2.modus
#3.median
#4.quartil 1
#5.quartil 3
#6.varian
#PENYAJIAN
#1.grafik matplotlib

data = pd.read_excel ("/content/drive/My Drive/Colab Notebooks/Survery difilter.xlsx")
print(data)

data.sort_values(by=['masukan'])

data.masukan.median().plot()

#PERHITUNGAN
#1.mean
#2.modus
#3.median
#4.quartil 1
#5.quartil 3
#6.varian

import pandas as pd
import matplotlib.pyplot as plt

def mean(A):
    total = 0
    for num in A:
        total = total + num
    return total/len(A)

def median(A):
    if len(A)%2 !=0:
      median = A[int(len(A)/2)]
    else:
      median = A[int(len(A)/2)-1] + A[(len(A)/2)]
      median = median/2
    return median

def modus(A):
    counter = 0
    num = A[0]

    for i in A:
        frekuensi = A.count(i)
        if(frekuensi > counter):
            counter = frekuensi
            num = i
        if len(set(A)) == len(A):
          return "modus tidak ditemukan"
    return num

data = pd.read_excel ("/content/drive/My Drive/Colab Notebooks/Survery difilter.xlsx")
masukan = data['masukan']


rata2 = mean(masukan)
tengah = median(masukan)


print(f"Nilai mean adalah: {rata2}")
print(f"Nilai median adalah: {tengah}")

"""# New Section"""