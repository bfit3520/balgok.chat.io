import random as r

def ma(t, n):
    reT = str(t)

    while len(reT) < n:
        reT = '0' + reT
    
    return reT

def mix_password():
    with open("user_inf.txt", "w", encoding="utf-8") as f:
        for i in range(1, 28 + 1):
            f.write("308" + ma(i, 2) + "-(please)-" + ma(r.randrange(1, 1000), 4 ) + '\n')

def user_information(): #유저의 정보를 불러 들여옴
    return_inf = {}

    with open("user_inf.txt", "r", encoding="utf-8") as f:
        userInformation = f.read().strip().split('\n')

    for i in range(len(userInformation)):
        temp = userInformation[i].split('-(please)-')
        return_inf[temp[0]] = temp[1]

    return return_inf

def change_password(user_id, password):
    new_inf = ""
    
    with open("user_inf.txt", "r", encoding="utf-8") as f:
        userInformation = f.read().strip().split('\n')

    for i in range(len(userInformation)):
        if userInformation[i][:5] == str(user_id):
            temp = userInformation[i][:-4] + str(password)
            userInformation[i] = temp
    
    for i in userInformation:
        new_inf += i + "\n"
    
    with open("user_inf.txt", "w", encoding="utf-8") as f:
        f.write(new_inf)

def text_inf(num): #채팅 개수를 불러들여옴. 최근 50개
    return_text = ''

    with open("text_log.txt", "r", encoding="utf-8") as f:
        temp = f.read().strip().split('\n')

    for i in range(len(temp)):
        temp[i] = temp[i].split('-(구분자)-')[1:]
        temp[i] = temp[i][0] + ': ' + temp[i][1]

    if len(temp) <= num:
        for i in range(len(temp) - 1):
            return_text += temp[i] + "<br>"
        return_text += temp[-1]
    else:
        for i in range(num, 2, -1):
            return_text += temp[-i] + "<br>"
        return_text += temp[-1]
    
    return return_text

def text_plus(user_id, user_name, text): #채팅을 추가함
    with open("text_log.txt", "a", encoding="utf-8") as f:
        f.write(user_id + '-(구분자)-' + user_name + '-(구분자)-' + text + '\n')

def text_chek(user_id):
    with open("text_log.txt", "r", encoding="utf-8") as f:
        temp = f.read().strip().split('\n')
    
    for i in range(len(temp)):
        temp[i] = temp[i].split('-(구분자)-')

    for i in range(1, len(temp) + 1):
        if temp[-i][0] == str(user_id):
            return temp[-i][2]
    
    return "none-text"


while 1:
    a = input("> ").split("/")
    change_password(a[0], a[1])