import time

def gettime():
    now = time.localtime()
    return now

def gettime2():
    now = time.localtime()
    return (now.tm_hour, now.tm_min)

result = gettime2()
print("{}시 {} 분".format(result[0],result[1]))