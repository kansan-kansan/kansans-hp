#https://flask.palletsprojects.com/en/2.0.x/quickstart/
from flask import Flask,Response
from flask import render_template
app = Flask(__name__, static_folder='./templates')#アプリのインスタンス化

@app.route("/") #URLを作っているイメージ
def hello():  #関数名はなんでも良い
    return render_template('hello.html')
    #city左側はhello.html内の変数

@app.route("/deliverables")
def deliverables():
    return render_template('deliverables.html')

@app.route("/hello")
def hello_():
    return render_template('hello.html')

@app.route("/photo")#写真
def photo():
    return render_template('photo.html')

@app.route("/questionnaire")#アンケート画面
def questionnaire():
    return render_template('questionnaire.html')


@app.route("/login",methods=['GET', 'POST'])
def authorized():
    """
    #if reqest.method == "POST":     値が入れば 
    
    #else
    #    return render_template('authorized.html')
    #322d353ad59f8a760ad94cee8bb01c26f994ebd1cd1dbbf68fe3c80018706095
    """
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)