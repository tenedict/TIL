a , b, c = map(int,input().split())
if a+b+c >= 100:
    print('OK')
else:
    g = (min(a,b,c))
    if g == a:
        print('Soongsil')
    if g == b:
        print('Korea')
    if g == c :
        print('Hanyang')