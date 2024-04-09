sum = 0
#숫자가 아닌 다른 문자를 넣었을때 에러를 발생하게 끔
str = input()
for s in str:
    sum += int(s)
print(sum)