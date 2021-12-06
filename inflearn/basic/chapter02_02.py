# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x,y,z)

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Object Referances
# 이러한 절차로 실행이 된다는 ..?
# 변수의 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300) # 변수로 할당하지 않고
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n
print(m, n )# 파이썬에서는 콤마 뒤에는 띄어쓰기하는 것을 권장함
print("고유값:", id(m), id(n))
print(type(n), type(m))

print()
print(n, m)
print()
m = 400

# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655

print("### 고유값 확인")
print(id(m))
print(id(n))
# 둘은 서로 다르다.
print(id(m) == id(n))
print()

n = 800 # 같은 값을 할당하면 아이디값이 똑같음
print(id(m) == id(n))
print()

m = 800
n = 800
z = 800
i = 800
print(id(m) == id(n) == id(z) == id(i))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : nuber_of_college_graguates -> 변수

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 숫자로 시작은 불가능
# ex) 1 = 1, 1_num = 1
# 예약어는 변수명으로 불가능(python reserved words)
# ex) for = 3
