1. Стек: Python3.10, FastApi, Postgres
2. В папке создать файл .env:
    - `POSTGRES_DB=` Имя db
    - `POSTGRES_USER=` Имя
    - `POSTGRES_PASSWORD=` Пароль

3. `sudo docker-compose up -d`
4. `pip install -r requirements.txt`
5. ``
6. `python -m uvicorn raiders.main:app --reload --port 8000`



