# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """ How are you? """
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print('I\'m Boy')
print('a \t b')
print('a \"\" b')

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""

escape_str1 = "Do yo have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 출력
# 역슬레시를 있는 그대로 raw로 표시할 수 있다.
raw_s1 = r'D:\python\test'
print(raw_s1)

### 멀티라인 입력
multi_str =\
'''
문자열\n
멀티라인 입력
테스트
'''
print(multi_str)

### 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) #해당 변수 안에 해당 문자가 들어있는 지
print('n' in str_o1)
print('P' not in str_o2)
print('p' not in str_o2)

### 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

# Capitalize : 첫글자를 대문자로 바꿔준다.
print("Capitalize: ", str_o1.capitalize())

# endswith : 끝부분에 어떤 문자로 끝나는지 체크
print("endswith?: ", str_o2.endswith('!'))

# replace : 해당 문자를 찾아서 원하는 문자로 변경
print("replace: ", str_o1.replace('thon','Good'))

imsi = 'Python'
print("sorted: ", sorted(str_o1))
print("sorted: ", sorted(imsi))
# sorted : 대문자가 가장먼저 정렬되고 그 다음 알파벳 순서로 정렬

# split :
print("split: ", str_o4.split(' '))

### 반복 시퀀스
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 가 있으면 반복할 수 있다.

# 출력
for i in im_str:
    print(i)


###슬라이싱(중요★)
str_sl = "Nice Python"
print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3]) # 0부터 2까지 0 1 2
print(str_sl[5:11])
print(str_sl[5:])
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_sl[:10]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[::2])
print(str_sl[::-1])


### 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) # 변수에 담긴 아스키 코드를 확인
print(ord('z')) # 문자열의 아스키 코드를 확인
print(chr(122)) # 아스키 코드 번호로 문자를 확인
