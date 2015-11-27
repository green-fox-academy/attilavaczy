x = 8
time = 120
out = ''

if x % 4 == 0 and time < 200:
    out = 'check'
elif time >= 200:
    out = 'Time out'
else:
    out = 'Run Forest Run!'

print(out)

#ver2

maxtime = 200

if x % 4 == 0 and time < maxtime:
    out = 'check'
elif time >= maxtime:
    out = 'Time out'
else:
    out = 'Run Forest Run!'

print(out)
