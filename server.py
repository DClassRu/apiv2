from flask import Flask, request, jsonify
import pymysql
import random
import string

app = Flask(__name__)

# Подключение к базе данных
db = pymysql.connect(host="localhost", user="dclass_api", password="password", database="dclass-main")
cursor = db.cursor()

# Функция для генерации случайного id
def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Эндпоинт для добавления нового пользователя
@app.route('/add', methods=['POST'])
def add_user():
    try:
        data = request.json
        first_name = data['first_name']
        name = data['name']
        cl = data['cl']
        email = data['email']
        role = data['role']
        password = data['password']
        
        # Генерация случайного id
        user_id = generate_random_id()

        # Выполнение SQL-запроса для добавления нового пользователя
        sql = f"INSERT INTO users (id, first_name, name, cl, role, email, password, dcoin, edu_login, edu_pass, notification) VALUES " \
              f"('{user_id}', '{first_name}', '{name}', '{cl}', '{role}', '{email}', '{password}', 0, NULL, NULL, NULL)"
        cursor.execute(sql)
        db.commit()

        return jsonify({"message": "User added successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт для обновления данных об образовании пользователя
@app.route('/add_edu_data', methods=['POST'])
def add_edu_data():
    try:
        data = request.json
        edu_login = data['edu_login']
        edu_pass = data['edu_pass']
        user_id = data['id']

        # Выполнение SQL-запроса для обновления данных об образовании пользователя
        sql = f"UPDATE users SET edu_login = '{edu_login}', edu_pass = '{edu_pass}' WHERE id = '{user_id}'"
        cursor.execute(sql)
        db.commit()

        return jsonify({"message": "Educational data added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт для увеличения dcoin пользователя
@app.route('/dcoin', methods=['POST'])
def update_dcoin():
    try:
        data = request.json
        user_id = data['id']
        dcoin_sum = data['sum']

        # Выполнение SQL-запроса для увеличения dcoin пользователя
        sql = f"UPDATE users SET dcoin = dcoin + {dcoin_sum} WHERE id = '{user_id}'"
        cursor.execute(sql)
        db.commit()

        return jsonify({"message": "dcoin updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт для обновления уведомления пользователя
@app.route('/notification', methods=['POST'])
def update_notification():
    try:
        data = request.json
        user_id = data['id']
        notification_text = data['text']

        # Выполнение SQL-запроса для обновления уведомления пользователя
        sql = f"UPDATE users SET notification = '{notification_text}' WHERE id = '{user_id}'"
        cursor.execute(sql)
        db.commit()

        return jsonify({"message": "Notification updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
