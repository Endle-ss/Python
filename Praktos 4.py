import sqlite3
from hashlib import sha256

class ClothingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('clothing_store.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.current_user = None

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users (id),
                FOREIGN KEY (product_id) REFERENCES Products (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users (id),
                FOREIGN KEY (product_id) REFERENCES Products (id)
            )
        ''')

        self.conn.commit()

    def register_user(self, username, password):
        hashed_password = self._hash_password(password)
        query = "INSERT INTO Users (username, password) VALUES (?, ?)"
        values = (username, hashed_password)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Пользователь успешно зарегистрирован.")
        except sqlite3.IntegrityError:
            print("Ошибка: Пользователь с таким именем уже существует.")

    def login_user(self, username, password):
        hashed_password = self._hash_password(password)
        query = "SELECT * FROM Users WHERE username=? AND password=?"
        values = (username, hashed_password)
        self.cursor.execute(query, values)
        user_data = self.cursor.fetchone()
        if user_data:
            self.current_user = User(user_data[0], user_data[1])
            print("Вход выполнен успешно.")
        else:
            print("Неверное имя пользователя или пароль.")

    def add_product(self, name, price):
        query = "INSERT INTO Products (name, price) VALUES (?, ?)"
        values = (name, price)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Продукт успешно добавлен.")
        except:
            print("Ошибка при добавлении продукта.")

    def display_products(self):
        query = "SELECT * FROM Products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()
        print("Продукты:")
        for product in products:
            print(f"{product[0]}. {product[1]} - ${product[2]}")

    def add_to_cart(self, product_id, quantity):
        if self.current_user:
            query = "INSERT INTO Cart (user_id, product_id, quantity) VALUES (?, ?, ?)"
            values = (self.current_user.id, product_id, quantity)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("Продукт добавлен в корзину.")
            except:
                print("Ошибка при добавлении продукта в корзину.")
        else:
            print("Пожалуйста, выполните вход.")
    def display_cart(self):
        if self.current_user:
            query = "SELECT Cart.id, Products.name, Cart.quantity FROM Cart JOIN Products ON Cart.product_id = Products.id WHERE user_id=?"
            values = (self.current_user.id,)
            self.cursor.execute(query, values)
            cart_items = self.cursor.fetchall()
            if cart_items:
                print("Корзина покупок:")
                for item in cart_items:
                    print(f"{item[0]}. {item[1]} - Количество: {item[2]}")

                print("\nДополнительные опции:")
                print("1. Удалить товар из корзины")
                print("2. Изменить количество товара в корзине")

                choice = input("Введите номер дополнительной опции: ")
                if choice == '1':
                    product_id_to_remove = int(input("Введите ID товара для удаления из корзины: "))
                    self.remove_from_cart(product_id_to_remove)
                elif choice == '2':
                    product_id_to_update = int(input("Введите ID товара для изменения количества: "))
                    new_quantity = int(input("Введите новое количество: "))
                    self.update_cart_quantity(product_id_to_update, new_quantity)
                else:
                    print("Неверный выбор дополнительной опции.")
            else:
                print("Корзина покупок пуста.")
        else:
            print("Пожалуйста, выполните вход.")
    def remove_from_cart(self, product_id):
        if self.current_user:
            query = "DELETE FROM Cart WHERE user_id=? AND product_id=?"
            values = (self.current_user.id, product_id)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("Продукт успешно удален из корзины.")
            except:
                print("Ошибка при удалении продукта из корзины.")
        else:
            print("Пожалуйста, выполните вход.")

    def update_cart_quantity(self, product_id, new_quantity):
        if self.current_user:
            query = "UPDATE Cart SET quantity=? WHERE user_id=? AND product_id=?"
            values = (new_quantity, self.current_user.id, product_id)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("Количество продукта в корзине успешно обновлено.")
            except:
                print("Ошибка при обновлении количества продукта в корзине.")
        else:
            print("Пожалуйста, выполните вход.")
    def checkout(self):
        if self.current_user:
            query = "SELECT * FROM Cart WHERE user_id=?"
            values = (self.current_user.id,)
            self.cursor.execute(query, values)
            cart_items = self.cursor.fetchall()
            if cart_items:
                for item in cart_items:
                    order_query = "INSERT INTO Orders (user_id, product_id, quantity) VALUES (?, ?, ?)"
                    order_values = (item[1], item[2], item[3])
                    self.cursor.execute(order_query, order_values)

                clear_cart_query = "DELETE FROM Cart WHERE user_id=?"
                self.cursor.execute(clear_cart_query, values)
                self.conn.commit()
                print("Оплата прошла успешно. Заказ размещен.")
            else:
                print("Корзина покупок пуста. Добавьте продукты перед оформлением заказа.")
        else:
            print("Пожалуйста, выполните вход.")

    def remove_from_cart(self, product_id):
        if self.current_user:
            query = "DELETE FROM Cart WHERE user_id=? AND product_id=?"
            values = (self.current_user.id, product_id)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("Продукт успешно удален из корзины.")
            except:
                print("Ошибка при удалении продукта из корзины.")
        else:
            print("Пожалуйста, выполните вход.")

    def update_cart_quantity(self, product_id, new_quantity):
        if self.current_user:
            query = "UPDATE Cart SET quantity=? WHERE user_id=? AND product_id=?"
            values = (new_quantity, self.current_user.id, product_id)
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                print("Количество продукта в корзине успешно обновлено.")
            except:
                print("Ошибка при обновлении количества продукта в корзине.")
        else:
            print("Пожалуйста, выполните вход.")
    def _hash_password(self, password):
        return sha256(password.encode()).hexdigest()

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

clothing_system = ClothingSystem()

while True:
    print("\n1. Регистрация")
    print("2. Вход")
    print("3. Добавить продукт")
    print("4. Показать продукты")
    print("5. Добавить в корзину")
    print("6. Показать корзину")
    print("7. Оформить заказ и оплатить")
    print("8. Выход")

    choice = input("Введите ваш выбор: ")

    if choice == '1':
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        clothing_system.register_user(username, password)

    elif choice == '2':
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        clothing_system.login_user(username, password)

    elif choice == '3':
        if clothing_system.current_user:
            name = input("Введите название продукта: ")
            price = float(input("Введите цену продукта: "))
            clothing_system.add_product(name, price)
        else:
            print("Пожалуйста, выполните вход.")

    elif choice == '4':
        clothing_system.display_products()

    elif choice == '5':
        if clothing_system.current_user:
            clothing_system.display_products()
            product_id = int(input("Введите ID продукта для добавления в корзину: "))
            quantity = int(input("Введите количество: "))
            clothing_system.add_to_cart(product_id, quantity)
        else:
            print("Пожалуйста, выполните вход.")

    elif choice == '6':
        clothing_system.display_cart()

    elif choice == '7':
        clothing_system.checkout()

    elif choice == '8':
        break

    else:
        print("Неверный выбор. Пожалуйста, повторите попытку.")
