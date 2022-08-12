import sys

sys.stdin = open("_모음이보이지않는사람.txt")

n = int(input())

for i in range(1,n+1):
    st = input()
    for j in ['a','e','i','o','u']:
        st = st.replace(j,'')
    print(f'#{i} {st}')
