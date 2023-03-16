# 문자 정렬
x = ['a', 'k', 'c', 'r', 'a', 'b']

for i in range(len(x)):
    for j in range(len(x)):
        if x[i] < x[j]:
            s = x[i]
            x[i] = x[j]
            x[j] = s
print(x)
