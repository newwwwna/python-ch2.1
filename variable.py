#variable
import keyword

#변수 이름은 문자, 숫자, _ 로 구성됨.
friend=1
a=10
my_name='김유나'
myName='김유나'
_yourName='둘리'
member1='도우넛'
long_string="""
"""

#에러
#friend$=1
#a!=10
#@myName='김유나'
# 숫자는 앞에 올 수 없음
#1abc=10
# 예약어는 변수 이름으로 사용할 수 없음
#def =10

print(keyword.kwlist)
print(len(keyword.kwlist))

#한글 이름의 변수도 가능
가격1=2000
print(가격1)
가격2=500
print(가격1-가격2)