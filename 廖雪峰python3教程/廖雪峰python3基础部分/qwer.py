from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    s1=[]
    s2=[]
    for i in range(len(s)-1):
        if s[i]=='.':
            a = i #找到小数点的位置
            for i in range(a): #将小数点前数按顺序找出
                s1.append(s[i])
            for i in range(1,len(s)-a): #将小数点后数按倒叙找出
                s2.append(s[-i])
            s2.append('0') #补0
    def char2num(y):
        return DIGITS[y]
    def f1(x,y):
        return x*10+y
    def f2(x,y):
        return x/10+y
    return reduce(f2,map(char2num,s2))+reduce(f1,map(char2num,s1))
# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
x = str2float('123.456')
print(x)
if abs(str2float('123.456') - 123.456 ) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')