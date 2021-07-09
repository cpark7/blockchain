song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when ther wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""
alpha = dict()

for c in song:
    if not c.isalpha():
        continue
    c = c.lower()
    if c not in alpha:
        alpha[c] = 1
    else:
        alpha[c]+=1
print(alpha)

#수업때 말한거
keys = alpha.keys()
keyslist = sorted(keys)

for key in keyslist:
    print("{}:{}".format(key,alpha[key]))#강사님은 alpha.get(key)로했엉.
# 내가한거
alpha = sorted(alpha.items(),key = lambda x:x[0])
print(alpha)
