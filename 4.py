import sys

mas1 = []
for x in sys.stdin.readlines():
    if x != "\n" and x != "\t":
        mas1.append(x)
mas = []
for x in mas1[0].split():
    mas.append(x)
ch = 1
while ch:
    ch = 0
    for x in mas1[1:]:
        s = x.split("=")
        r = s[0].split()
        r1 = s[1].split()
        if len(r) == 2:
            flag = True
            for z in r:
                if z not in mas:
                    flag = False
            if flag:
                for y in r1:
                    if y not in mas:
                        mas.append(y)
                        ch = 1
        else:
            if r[0] in mas:
                for z in r1:
                    if z not in mas:
                        mas.append(z)
                        ch = 1
mas.sort()
print(*mas)







