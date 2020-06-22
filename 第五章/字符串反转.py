def rsv(s):
    if s == '':
        return s
    else:
        return (rsv(s[1:])+s[0])
s='abc'
rsv(s)
print(s)
