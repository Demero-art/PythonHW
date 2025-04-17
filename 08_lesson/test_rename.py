import requests

# ПОДСТАВИТЬ ДАННЫЕ
TOKEN = "?"
BASE_URL = "?"

# Создание проекта (добавьте в начало)
create_resp = requests.post(
    f"{BASE_URL}/projects",
    json={"title": "Деревня котов"},
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
)
PROJECT_ID = create_resp.json()["id"]  # Получаем ID нового проекта

# Простое переименование проекта
response = requests.put(
    f"{BASE_URL}/projects/{PROJECT_ID}",
    json={"title": "Город енотов"},
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
)
# Выводим результат
print("Статус переименования:", response.status_code)
print("Ответ сервера:", response.text)