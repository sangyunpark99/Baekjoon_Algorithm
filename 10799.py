s = list(input())
st = []

ans = 0

for i in range(len(s)):
    if s[i] == '(':
        st.append('(')
    else:
        if s[i-1] == '(':
            st.pop()
            ans += len(st)
        else:
            ans += 1
            st.pop()

print(ans)