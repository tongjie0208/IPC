import codecs

f = codecs.open('log_tp8k_64_new.txt', mode='r', encoding='utf-8')  
line = f.readline()   
list1 = []
while line:
    a = line.split()
    b = a[4:5]  
    list1.append(b)  
    line = f.readline()
f.close()


for i in list1:
    s = ''.join(i)
    print(s)


"""
for i in list1:
    s = ''.join(i)
    s = s.split(".")
    print(''.join(s[0:1]))
"""