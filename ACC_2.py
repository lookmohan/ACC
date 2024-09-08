def breakword(s,dic):
    for i in range(1,len(s)+1):
        if s[:i] in dic:
            if i==len(s):
                return 1
            if breakword(s[i:],dic):
                return 1
    return 0
n1=6
s1="ilike"
dic={'i','like','sam','sung','samsung','mobile'}
print(breakword(s1,dic))
