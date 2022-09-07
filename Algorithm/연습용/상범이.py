import readline

from sys import stdin, stdout #(입출력 가속)

list = []

count = int(input())
for i in range(count):
    i = int(input())
    list.append(i)

def Open(list):
    for n in list:
        list2 = [j for j in range(1, int(n)+1)]
        for i in range(2, int(n)+1):
            for j in range(1, int(n)+1):
                if i*j > int(n):
                    break
                elif i*j in list2:
                    list2.remove(i*j)
                else:
                    list2.append(i*j)
        print(len(list2))

Open(list)


