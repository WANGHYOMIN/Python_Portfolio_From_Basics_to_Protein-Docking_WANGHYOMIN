#chapter02_02_practice 9 (2025_09_22)
"""f 문자열 포매팅"""
name="hyomin"
age=23

s=f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(s)

s=f'나는 내년이면 {age+1}살이 된다.'
print(s)

d={'name':'hyomin','age':23}
s=f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
print(s)

s=f'{"hi":<10}'
print(s)

s=f'{"hi":>10}'
print(s)

s=f'{"hi":^10}'
print(s)

s=f'{"hi":=^10}'
print(s)

s=f'{"hi":!^10}'
print(s)

number=3.141592
s=f'{number:0.2f}'
print(s)

s=f'{number:10.2f}'
print(s)

s=f'{{or}}'
print(s)
