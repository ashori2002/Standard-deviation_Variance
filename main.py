import math
myList = [10,12,13,15,18,20,25,26,32]

average = (sum(myList)/len(myList))
print(f"Avrage : {average}")
newList = []
for i in myList:
    if(i>average):
        newList.append((i - average)**2)
    elif(i<average):
        newList.append((average - i)**2)
    elif(i==average):
        newList.append(0)
    else:
        print("ERROR")

variance = sum(newList)/5
print(f"Variance : {variance}")

standardDeviation = math.sqrt(variance)
print(f"Standard Deviation : {standardDeviation}")

period = {min : average - standardDeviation , max : average + standardDeviation}
print(f"Period : min = {period[max]} max = {period[max]}")
