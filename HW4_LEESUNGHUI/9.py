d = [
    {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone': '555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone': '555-3141', 'email':''},
    {'name':'LJ', 'phone': '555-2718', 'email':'lj@mail.net'},
]


print("전화번호가 8로 끝나는 사용자 이름")
for person in d:
    if person['phone'].endswith('8'):
        print(person['name'])

print("이메일이 없는 사용자 이름")
for person in d:
    if not person['email']:
        print(person['name'])

user_name = input("입력: ")
for person in d:
    if person['name'] == user_name:
        print(f"전화번호: {person['phone']}, 이메일: {person['email'] if person['email'] else '이메일 없음'}")
        break
else:
    print("해당 없음")
