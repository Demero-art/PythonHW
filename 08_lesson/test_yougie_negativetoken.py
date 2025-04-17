import requests

# ПОДСТАВИТЬ ДАННЫЕ В URL
TOKEN = "NO TOKEN"
BASE_URL = "?"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

new_project = {
    "title": "Деревня гусей"
}

response = requests.post(f"{BASE_URL}/projects", json=new_project, headers=headers)

if response.status_code == 200:
    print("Проект создан успешно")
else:
    print("Ошибка создания проекта")