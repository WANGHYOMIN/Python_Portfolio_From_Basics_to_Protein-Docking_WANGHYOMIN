#chapter02_02_practice 11 (2025_09_29)
""" 문자열 관련 함수들 """

""" count-문자 개수 세기 """
s="biology"
print(s.count('o'))

""" find-위치 알려주기1 """
s="Medicine is the best choice"
print(s.find('b'))

""" index-위치 알려주기2"""
s="Medicine is the best choice"
print(s.index('b'))

""" join-문자열 삽입 """
s='abcd'
print(",".join(s))

""" upper-소문자를 대문자로 바꾸기 """
s="hi"
print(s.upper())

""" lower-대문자를 소문자로 바꾸기 """
s="HI"
print(s.lower())

""" lstrip-왼쪽 공백 지우기 """
s=" hi "
print(s.lstrip())

""" rstrip-오른쪽 공백 지우기 """
s=" hi "
print(s.rstrip())

""" strip-양쪽 공백 지우기 """
s=" hi "
print(s.strip())

""" replace-문자열 바꾸기 """
s="Medicine is the best choice"
print(s.replace("Medicine","Therapeutics"))

""" split-문자열 나누기 """
s="Medicine is the best choice"
print(s.split())

s="Medicine:is:the:best:choice"
print(s.split(":"))



