import requests

# подставить токен без верного URL
TOKEN = "?"
BASE_URL = "VVV" #НЕВЕРНЫЙ URL

# 1. Создаем проект "Деревня котов"
create_response = requests.post(
    f"{BASE_URL}/projects",
    json={"title": "Деревня котов"},
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
)

# Проверяем успешность создания
if create_response.status_code == 200:
    project_id = create_response.json()["id"]
    print(f"Проект создан успешно. ID: {project_id}")

    # 2. Получаем проект по ID
    get_response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )

    # Проверяем успешность получения
    if get_response.status_code == 200:
        print("Данные проекта:", get_response.json())
    else:
        print(f"Ошибка получения проекта: {get_response.status_code}")
else:
    print(f"Ошибка создания проекта: {create_response.status_code}")