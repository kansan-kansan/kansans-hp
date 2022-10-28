"""
from werkzeug.security import generate_password_hash, check_password_hash

# パスワードをハッシュ化
def set_password(password):
    password_hash = generate_password_hash(password)
    print(password_hash)

    # 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
def check__password(pas):
    check_pas = check_password_hash(pas)
    print(check_pas)

print("a" * 100)
set_password("aiueo")
print("b" * 100)
#aiueo = str()
check__password("aiueo")
print("c" * 100)
"""