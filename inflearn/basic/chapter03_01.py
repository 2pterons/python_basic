# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스) # 순서가 있다.
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
#float = 10.0 # 컴퓨터에서는 10 != 10.0
float_v = 10.0
#int = 7
int_v = 7
list = [str1, str2]
print(list)
dict = {
    "name":"Machine Learning",
    "version":2.0
}

tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) , x ** y -> 2 **3
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777779999999999999999999999999997777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산실습
i1 = 39
i2 = 939
big_int1 = 77777777777777779999999999999999998432138743
big_int2 = 735138731344356135046840684684068406846804854
f1 = 1.234
f2 = 3.939

# +
print(">>>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# 정수와 실수의 연산은 자동으로 실수형으로 형변환
print(3 + 1.0) # = 4.0

# *
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

# 형 변환 실습 (중요★)
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, Flase : 0
print(int(False))
print(complex(3))
print(complex('3')) # 문자형을 숫자형으로 바꾼다음에 실행되는 것을 확인할 수 있다.
print(complex(False))
print(complex(True))

# 수치 연산 함수
print(abs(-7)) #절대값 반환
x, y = divmod(100, 8) #100을 8로 나눤 다음 몫과 나머지를 각각 변수에 할당
# 많이 사용됨
print(x, y)
print(pow(5, 3), 5 ** 3) #제곱

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)
