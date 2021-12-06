# 주석을 통해 무엇을 공부하는지 잘 정리하는 습관을 기르자

# CHanpter02-1
# 피이썬 완전 기초
# print 사용법
# 참조 : https://wwww.python-course.eu/python3_formatted_output.python3_formatted_output

# 기본 출력
print('Python Start!')
print("Python Start!")
print()
print()
print('''Python Start!''')
print("""Python Start!""")

print()

# separater 옵션
print('P', 'Y', 'T', 'H', 'O', 'N')
# 이렇게 분리 되어있는 것을 sep라는 옵션?을 넣어서 사용
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
# 결과 : P,Y,T,H,O,N
print('010','7777','1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end='')
print('!')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
# 해당 내용을 내가 지정한 파일에 쓰는것 (참고로 위는 틀린 것)
# 즉, 외부에 특정한 파일로 쓸 것이라는 의미
# sys.stdout은 아래 콘솔을 말한다.
print()

# format 사용(d, s, f)
# d: 정수
# s: 문자열
# f: 실수
print("### format 사용")
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))

# %s
print('%10s' % ('nice')) #총 자리수 10개중에 나머지에 해당 문자를 처리.
print('%10s' % ('nice111'))
print('{:>10}'.format('nice')) #
print()

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
print()

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
print()

print('{:_>10}'.format('nice'))
print()

print('{:*<10}'.format('nice'))
print('{:^>10}'.format('nice'))
print('{:^10}'.format('nice')) # 중앙정렬
print()

print('%5s' % ('nice'))
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) #공간이 다섯개이기 때문에 짤림
print()

print("### 주어진 공간안에 결과값")
print('{:10.5}'.format('pythonstudy')) # 10개의 주어진 공간안에 결과값은 5개만 나온다.
print('%10.5s' % ('pythonstudy'))

# %d
print("### 정수")
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print()

print('%4d' % (42))
print('%4d' % (421341234))
print('{:4d}'.format(42)) #정수일 때는 format함수에서 d를 붙여줘야한다.
print('{:4d}'.format(426516468468))
print()

# %f
print('### 실수')
print('%f' % (3.1434343434343434))
print('%1.8f' % (3.1434343434343434))
# 앞이 정수부 뒤가 소수부
# 따라서 앞에는 1개 뒤에는 8개가 출력됨
print('{:f}'.format(3.1434343434343434))
print('{:1.8f}'.format(3.1434343434343434))
print()

print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
