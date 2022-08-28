def InsertSort(l):
    for i in range(1, len(l)):
        t = l[i]
        j = i
        while j > 0 and l[j - 1] > t:
            l[j] = l[j - 1]
            j -= 1
        l[j] = t
    print(l)


l = [49, 38, 65, 97, 76, 13, 27, 49]
InsertSort(l)