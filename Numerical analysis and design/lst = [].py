lst = []
lst1 = []
sz= 0 
n = int(input())
for i in range(0,n):
    put = input()
    lst.append(put)
    if put  not in lst1:
        lst1.append(put)
        sz+=1
print(sz)
for occ in lst1:
    print(lst.count(occ),end = ' ')
lst = []
lst1 = []
sz= 0 
n = int(input())
for i in range(0,n):
    put = input()
    lst.append(put)
    if put  not in lst1:
        lst1.append(put)
        sz+=1
print(sz)
for occ in lst1:
    print(lst.count(occ),end = ' ')










