from flask import Flask, request, render_template
import os

app = Flask(__name__)


def user_information(): #유저의 정보를 불러 들여옴
    return_inf = {}

    with open("user_inf.txt", "r", encoding="utf-8") as f:
        userInformation = f.read().strip().split('\n')

    for i in range(len(userInformation)):
        temp = userInformation[i].split('-(please)-')
        return_inf[temp[0]] = temp[1]

    return return_inf
        
def text_inf(num): #채팅 개수를 불러들여옴. num개 만큼 받아들임
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
        for i in range(num, 1, -1):
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


@app.route("/")
def home():
    return render_template('index.html', status = "logout" )


@app.route("/login", methods=['POST'])
def login():
    user_id = str(request.form['hakbun'])
    user_password = str(request.form['pa'])
    
    information = user_information()

    if information[user_id] == user_password:
        return render_template('index.html',
                               textInf = text_inf(10),
                               status = 'login',
                               ha = user_id,
                               nikname = "익명"
                               )

    return render_template('index.html',
                            status = 'logout')

@app.route("/playchat", methods=['POST'])
def chat():
    if request.form['user_nik'] == '':

        if text_chek(request.form['user_hak']) != request.form['user_text'] and request.form['user_text'] != '':
            text_plus(request.form['user_hak'], "익명", request.form['user_text'])

        return render_template('index.html',
                                textInf = text_inf(10),
                                status = 'login',
                                ha = request.form['user_hak'],
                                nikname = "익명"
                                )
    else:

        if text_chek(request.form['user_hak']) != request.form['user_text'] and request.form['user_text'] != '':
            text_plus(request.form['user_hak'], request.form['user_nik'], request.form['user_text'])

        return render_template('index.html',
                                textInf = text_inf(10),
                                status = 'login',
                                ha = request.form['user_hak'],
                                nikname = request.form['user_nik']
                                )
    
# @app.route("/getchat")
# def get_chat():
#     return text_inf(13) #소리없는 아우성



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

