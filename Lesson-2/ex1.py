mathq = [1, 31, 63, 12, 83, 90, 12, 27, 19, 31]
mode = max(mathq)
mean = sum(mathq) / len(mathq)
print("Mode:", mode)
print("Mean:", mean)
mathq.sort()
if (len(mathq) % 2 == 1):
    mid = len(mathq) // 2
    median = mathq(mid)
else:
    mid = len(mathq) // 2 - 1
    median = mathq[mid] + mathq[mid + 1]
    median = median / 2
    
print("Median:", median)

mathq1 = mathq[0]
mods = []
max = 0

for i in range(len(mathq)):
    count = 1
    for j in range(i, len(mathq)):
        if mathq[j] == mathq[i]:
            count = count + 1
    if (max < count): max = count
    
print(max)