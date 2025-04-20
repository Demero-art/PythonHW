import requests

# Данные
TOKEN = "lu3Of0JexlVF9gX0aX0-dTJ1PTedVeCyUgO6mSKNCl-bgUvmkUk5Lo0UdpnftO7n"
BASE_URL = "https://ru.yougile.com/api-v2"


def test_create_and_rename_project():
    # 1. Создаём проект
    create_resp = requests.post(
        f"{BASE_URL}/projects",
        json={"title": "Деревня котов"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )
    # Проверка создания
    assert create_resp.status_code == 201

    # 2. Получаем ID проекта
    PROJECT_ID = create_resp.json()["id"]

    # 3. Переименовываем проект
    rename_resp = requests.put(
        f"{BASE_URL}/projects/{PROJECT_ID}",
        json={"title": "Город енотов"},
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )
    # Проверка переименования
    assert rename_resp.status_code == 201
