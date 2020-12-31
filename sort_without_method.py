
l = [5,3,6,4,2]


for i in range(len(l)):
    # print(i)
    for j in range(i,len(l)):
        # print(l[i])
        # print(l[j])
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(l)






