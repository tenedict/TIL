n = input()

for i in n:
    if i == 'C' or i == 'A' or i == 'M' or i == 'B' or i == 'R' or i == 'I' or i == 'D' or i == 'G' or i == 'E':
        n = n.replace(i,'')
print(n)