w = "to be or not to be, that is the question"
w_split = w.split()
dic = {}
for i in w_split:
    i = i.strip(',')
    if i in dic.keys():
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
print(dic)
