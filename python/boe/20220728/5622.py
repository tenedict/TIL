n = input()
n = n.lower()
time = 0
for i in n:
    if i == 'a' or i =='b' or i =='c':
        time += 3
    elif i == 'd' or i =='e' or i =='f':
        time += 4
    elif i == 'g' or i =='h' or i =='i':
        time += 5
    elif i == 'j' or i =='k' or i =='l':
        time += 6
    elif i == 'm' or i =='n' or i =='o':
        time += 7
    elif i == 'p' or i =='q' or i =='r'or i == 's':
        time += 8
    elif i == 'v' or i =='t' or i =='u':
        time += 9
    elif i == 'y' or i =='w' or i =='x' or i =='z' :
        time += 10
print(time)   