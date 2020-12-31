print("Open a Txt. File And Count Words , latters , line.")

with open('demo.txt','r') as f:
    letters = 0
    line = 0
    word = 0
    for i in f:
        s = i.split(' ')
        l =len("".join(s))
        w = len(s)
        l1 = len(i.split('.'))
        letters = letters + l
        word = word + w
        line = line + l1
    print("letters",letters)
    print("line",line)
    print("word",word)
    f.close()
