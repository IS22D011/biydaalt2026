import re

class UserSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, email, password):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Алдаа: И-мэйл буруу байна"
        if len(password) < 5:
            return "Алдаа: Нууц үг хэт богино"
        if username in self.users:
            return "Алдаа: Хэрэглэгч бүртгэлтэй байна"
        
        self.users[username] = {"email": email, "password": password}
        return "Амжилттай бүртгэгдлээ"

    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False

    # UPDATE: Нууц үг солих
    def update_password(self, username, old_password, new_password):
        if self.login(username, old_password):
            if len(new_password) < 5:
                return "Алдаа: Шинэ нууц үг хэт богино"
            self.users[username]['password'] = new_password
            return "Нууц үг амжилттай солигдлоо"
        return "Алдаа: Хуучин нууц үг буруу"

    # DELETE: Хэрэглэгч устгах
    def delete_account(self, username, password):
        if self.login(username, password):
            del self.users[username]
            return "Бүртгэл амжилттай устлаа"
        return "Алдаа: Нууц үг буруу тул устгах боломжгүй"