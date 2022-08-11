li = []
co = False
for i in range(1,6):
    n = input()
    if 'FBI' in n:
        print(i)
        co = True
if co == False:
    print('HE GOT AWAY!')

