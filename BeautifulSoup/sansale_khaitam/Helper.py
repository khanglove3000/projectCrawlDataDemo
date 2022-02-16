from fileinput import filename
from Target import Target

def getTargetFromFile(fileName):
    targetFile = open(fileName, "r", encoding='utf8')
    lines = targetFile.readlines()
    targetFile.close()

    targets = []
    n = len(lines)
    print("n = " + str(n))
    i = 0
    while i < n:
        newTarget = Target(lines[i].strip(), lines[i+1].strip())
        print(newTarget.info())
        targets.append(newTarget)
        i = i + 2
    return targets


def converToPrice(strPrice):
	strPrice = strPrice.replace('.', '')
	strPrice = strPrice.replace('đ', '')
	return int(strPrice)