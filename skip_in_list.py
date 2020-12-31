l = ['jay','umang','manthan','','anuj',None,'dabhi',None,'','','sohan',None]
a = []
for i in l:
    if i == '' or i == None:
        continue
    else:
        a.append(i[0])
print(a)

# # Print List element
# l = [['jay','16ce34','Computer'],['rumit','16ce44','computer'],['parth','16ce15',['automobile']]]
# f = l[2][2][0]
# print(f)
