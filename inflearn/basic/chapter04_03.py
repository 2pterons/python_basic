# Chapter04-3
# 파이썬 반복문

# while 실습
# 파이썬에서는 if, for, while 이 3개의 구문을 합쳐서
# 모든 프로그램의 입/출력을 제어할 수 있는 "흐름 제어문" 이라고 한다.

# while 기본 사용법
# 표현식
# while <expr>:
#   <statement(s)>
# while문은 if문과 비슷하 조건이 만족하는 동안 계속 반복하고 조건에 만족하지 않으면 그 때 wile문을 ㅃㅏ져나간다.

# 예제 1
n = 5
while n > 0:
    n = n-1 # 조건이 없으면 무한반복에 빠진다.
    print(n)

# while True:
#    print(n) # 무한 반복
#    n = - 1

# 예제 2
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop()) # pop()과 같은 함수를 이용해서 종료할 수 있는 코드를 완성
    #또는 print(a.pop(-1))

# if 중첩
# 에제 3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')
print()

# 예제 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')
print()

# 예제 5
i = 1
while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1
print()

# while - else 구문
# 예제 6
n = 10
while n > 5:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')
print()

n = 10
while n > 6:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')
print()

# 예제 7
print('예제7')
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0
while i < len(a):
    if a[i] == s:
        break
    print('found :', a[i])
    i += 1
else:
    print(s, "not found in list")
print()

# 예제 8
a = ['foo', 'bar', 'baz', 'qux']
while True:
    if not a: #True가 아니면 break
        break
    print('예제8', a.pop())
print()

# Break, Couninue
# While-Else 구문
# 무한 반복 구문
# 기본 패턴 실습
