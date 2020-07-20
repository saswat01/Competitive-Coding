def Way_too_long(s):
    if s and not s.isdigit():

        if len(s)>10:
            a = s[0]
            b = s[-1]
            c = str(len(s) - 2)
            return a+c+b
        else:
            return s
    else:
        return None
r = int(input())

for i in range(r):
    s = input()
    print(Way_too_long(s))
    