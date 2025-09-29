#chapter02_02_pracitce 8 (2025_09_22)
"""fomat함수를 사용한 포매팅"""

"""숫자 바로 대입하기"""
s="I administered the drug {0} times.".format(5)
print(s)

"""문자열 바로 대입하기"""
s="I administered the drug {0} times.".format("five")
print(s)

"""숫자값을 가진 변수로 대입하기"""
number=5
s="I administered the drug {0} times.".format(number)
print(s)

"""2개 이상의 값 넣기 """
number=5
day="three"
s="I administered the drug {0} times over {1} days.".format(number,day)
print(s)

"""이름으로 넣기 """
s="I administered the drug {number} times over {day} days.".format(number=5,day=3)
print(s)

"""인덱스와 이름을 혼용해서  넣기 """
s="I administered the drug {0} times over {day} days.".format(5,day=3)
print(s)

"""왼쪽 정렬"""
s="{0:<10}".format("biology")
print(s)

"""오른쪽 정렬"""
s="{0:>10}".format("biology")
print(s)

"""가운데  정렬"""
s="{0:^10}".format("biology")
print(s)

"""공백 채우기"""
s="{0:=^10}".format("biology")
print(s)
s="{0:*^10}".format("biology")
print(s)

"""소수점 표현하기"""
number=3.141592
s="{0:0.5f}".format(number)
print(s)

s="{0:10.5f}".format(number)
print(s)

"""{또는} 문자 표현하기"""
s="{{or}}".format()
print(s)

s="{0}".format("{or}")
print(s)
