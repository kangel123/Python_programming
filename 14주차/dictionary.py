dic_1 = {}
dic_1["홍길동"] = '010-1234-5678'
dic_1["김강찬"] = '010-1234-5678'
dic_1["이순신"] = '010-1234-5678'
dic_2 = {'홍길동': '010-1234-5678', '김강찬': '010-1234-5678', '이순신': '010-1234-5678'}
print('dic1:', dic_1)
print('dic2:', dic_2)
print(dic_1.keys())
print(dic_1.values())

for key in sorted(dic_1.keys()):
    print(key, dic_1[key])
