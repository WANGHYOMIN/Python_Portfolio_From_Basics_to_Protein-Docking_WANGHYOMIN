#chapter02_02_practice 6 (2025_09_22)
"""문자열 포매팅 하기"""

"""숫자 바로 대입"""
s="I administered the drug %d times." %5
print(s)

"""문자열 바로 대입"""
s="I administered the drug %s times." %"five"
print(s)

"""숫자 값을 나타내는 변수로 대입"""
number=5
s="I administered the drug %d times." %number
print(s)

"""2개 이상의 값 넣기"""
number=5
day="three"
s="I administered the drug %d times over %s days." %(number,day)
print(s)

"""포매팅 연산자 %d와 %를 같이 쓰기"""
s="The mortality rate is %d%%"%76
print(s)
