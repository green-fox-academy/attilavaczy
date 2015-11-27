v = [1, 2, 3]
out = 0

if len(v) == 1:
    out = 1
elif len(v) == 2:
    out = 2
elif len(v) > 2:
    out = 10
else:
    out = -1

print(out)

#ver

if len(v) == 0:
    out = -1
elif len(v) == 1:
    out = 1
elif len(v) == 2:
    out = 2
else:
    out = 10

print(out)
