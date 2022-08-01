t = int(input())
for _ in range(t):
    st = []
    s = input()
    co = True

    for ch in s:
        if ch == '(':
            st.append('(')
        if ch == ')':
            if st:
                st.pop()
            elif not st:
                co = False
                break
    if not st and co:
        print('YES')
    elif st or not co:
        print('NO')