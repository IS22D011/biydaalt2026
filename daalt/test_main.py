import pytest
from main import UserSystem

@pytest.fixture
def system():
    s = UserSystem()
    s.register("testuser", "test@mail.com", "password123")
    return s

# UPDATE Тест
def test_update_password_success(system):
    result = system.update_password("testuser", "password123", "newpass123")
    assert result == "Нууц үг амжилттай солигдлоо"
    assert system.login("testuser", "newpass123") == True

def test_update_password_wrong_old(system):
    result = system.update_password("testuser", "wrongold", "newpass123")
    assert result == "Алдаа: Хуучин нууц үг буруу"

# DELETE Тест
def test_delete_account_success(system):
    result = system.delete_account("testuser", "password123")
    assert result == "Бүртгэл амжилттай устлаа"
    assert "testuser" not in system.users

def test_delete_account_fail(system):
    result = system.delete_account("testuser", "wrongpass")
    assert result == "Алдаа: Нууц үг буруу тул устгах боломжгүй"