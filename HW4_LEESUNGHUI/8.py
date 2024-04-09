days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}

user_input = input("월을 입력:")

for month, day in days.items():
    if user_input.title() in [month, month[:3]]:
        print(f"{month}는 {day}일.")
        break
else:
    print("없음")


print("알파벳 순서로 모든 월 출력:")
for month in sorted(days.keys()):
    print(month)

print("일수가 31인 모든 월 출력:")
for month, day in days.items():
    if day == 31:
        print(month)

print("월의 일수를 기준으로 오름차순으로 쌍 출력:")
for month in sorted(days.items(), key=lambda x: x[1]):
    print(month)
