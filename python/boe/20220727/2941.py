list_ = ['c=','c-','dz=','d-','lj','nj','s=','z=']

n = input()
for i in list_:
    n = n.replace(i,"_")
    

print(len(n))