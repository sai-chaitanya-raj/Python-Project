n = int(input("Enter number of strings you want to input: "))
strarray , wordsarray = [] , []
for x in range(n):
    strarray.append(input("Enter a string: "))
print(strarray)
for str in strarray:
    wordsarray.append(str.split(" "))
# print(wordsarray)
for i in range(len(wordsarray)):
    accr = ""
    for word in wordsarray[i]:
        accr = accr + word[0] + " "
    print(accr.upper() + "\n")












