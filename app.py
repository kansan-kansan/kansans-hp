#https://flask.palletsprojects.com/en/2.0.x/quickstart/
from flask import Flask,Response
from flask import render_template
import time

app = Flask(__name__, static_folder='./templates')#アプリのインスタンス化


@app.route("/") #URLを作っているイメージ
def hello():  #関数名はなんでも良い
    with open("./log.txt", "a",encoding='utf-8') as txt:
        now = time.ctime()
        cnvtime = time.strptime(now)
        txt.write("\n\nhello.html>>")
        txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))
    return render_template('hello.html')
    #city左側はhello.html内の変数

@app.route("/deliverables")
def deliverables():
    with open("./log.txt", "a",encoding='utf-8') as txt:
        now = time.ctime()
        cnvtime = time.strptime(now)
        txt.write("\n\ndeliverables.html>>")
        txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))
    return render_template('deliverables.html')

@app.route("/hello")
def hello_():
    with open("./log.txt", "a",encoding='utf-8') as txt:
        now = time.ctime()
        cnvtime = time.strptime(now)
        txt.write("\n\nhello.html>>")
        txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))
    return render_template('hello.html')

@app.route("/photo")#写真
def photo():
    with open("./log.txt", "a",encoding='utf-8') as txt:
        now = time.ctime()
        cnvtime = time.strptime(now)
        txt.write("\n\nphoto.html>>")
        txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))
    return render_template('photo.html')

@app.route("/questionnaire")#アンケート画面
def questionnaire():
    with open("./log.txt", "a",encoding='utf-8') as txt:
        now = time.ctime()
        cnvtime = time.strptime(now)
        txt.write("\n\nquestionnaire.html>>")
        txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))
    return render_template('questionnaire.html')


@app.route("/login",methods=['GET', 'POST'])
def login():
    with open("./log.txt", "a",encoding='utf-8') as txt:
        now = time.ctime()
        cnvtime = time.strptime(now)
        txt.write("\n\nlogin.html>>")
        txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))    
    ####Flashの挿入?(間違っている or 値が入っていない)
    """
    Flash https://qiita.com/kotmats/items/fcff19ae5ea309d9fee9
    #if reqest.method == "POST":     #値が入れば 
        username = request.form.get('username')     #
        password = request.form.get('password')     #
        enter_user_hash = check_user_hash(userid)     #ユーザーをハッシュ化
        enter_pas_hash = check_password_hash(password)  #pasをハッシュ化
        if enter_user_hash == db.pyのuser''  and enter_pas_hash'== db.pyのpas'':
            ####成功した場合
            return render_template('management.html')

        else:       #user,pasは入れたが、違った場合
            flash("ユーザー名または、パスワードが違います。")

    #else       #入力していないなら
        #flash("ユーザー名または、パスワードが違います。")
    #    return render_template('login.html')
    #322d353ad59f8a760ad94cee8bb01c26f994ebd1cd1dbbf68fe3c80018706095
    """
    return render_template('login.html')

"""
##ログイン後
@app.route("/management")
def management():
        return render_template('management.html')

"""

if __name__=="__main__":
    app.run(debug=True)