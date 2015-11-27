z = 4
text = 'Gold'
i = 0
while i < z:
    print(text)
    i += 1


#ver
for i in range(0, z):
    print(text)

#ver3
for t in [text] * 4:
    print(t)
