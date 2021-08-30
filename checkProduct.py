from list import *
from getData import *



def checkProduct():
    a , b = 0 , 0
    for i in range(len(product)):
        for j in range(len(listNvidia)):
            if listNvidia[j] in product[i+1]['title']:
                print(f"{product[i+1]['title']} found")
                listNvidiaResult[a] = {'title': product[i+1]['title'],'ASIN':product[i+1]['ASIN'],'price':product[i+1]['price']}
                a += 1
        for k in range(len(listAmd)):
            if listAmd[k] in product[i+1]['title']:
                print(f"{product[i+1]['title']} found")
                listAmdResult[b] = {'title': product[i+1]['title'],'ASIN':product[i+1]['ASIN'],'price':product[i+1]['price']}
                b += 1
    print(listNvidiaResult)
    print(listAmdResult)
    for i in range(len(listAmdResult)):
        print(listAmdResult[i])
    for i in range(len(listNvidiaResult)):
        print(listNvidiaResult[i])

