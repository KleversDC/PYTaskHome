
# # Завдання 1 (Температура)

# temperatures = [2, 5, 4, 6, 7, 3, 1]

# avg_temp = sum(temperatures) / len(temperatures)
# max_temp = max(temperatures)
# min_temp = min(temperatures)
# diff = max_temp - min_temp

# print("=== Температура ===")
# print("Середнє:", avg_temp)
# print("Максимум:", max_temp)
# print("Мінімум:", min_temp)
# print("Різниця:", diff)


# # Завдання 2 (Витрати)

# expenses = [1200, 1500, 800, 600, 1000, 400, 900]

# total = sum(expenses)
# avg = total / len(expenses)
# max_val = max(expenses)
# min_val = min(expenses)
# days_over_1000 = len([x for x in expenses if x > 1000])

# print("\n=== Витрати ===")
# print("Сума:", total)
# print("Середнє:", round(avg, 2))
# print("Максимум:", max_val)
# print("Мінімум:", min_val)
# print("Днів > 1000:", days_over_1000)


# # Завдання 3 (Голоси)

# from collections import Counter

# votes = ["apple", "banana", "apple", "orange", "banana", "apple", "apple", "apple", "orange"]

# counter = Counter(votes)
# leader = counter.most_common(1)[0]
# top3 = counter.most_common(3)

# print("\n=== Голоси ===")
# for fruit, count in counter.items():
#     print(f"{fruit}: {count}")

# print("Лідер:", leader)
# print("Топ-3:", top3)


# # Завдання 4 (Оцінки)

# math = [80, 92, 75, 60, 88]
# physics = [70, 65, 90, 85, 78]
# english = [95, 100, 85, 90, 87]

# def stats(subject):
#     return sum(subject)/len(subject), min(subject), max(subject)

# math_stats = stats(math)
# physics_stats = stats(physics)
# english_stats = stats(english)

# subjects = {
#     "math": math_stats[0],
#     "physics": physics_stats[0],
#     "english": english_stats[0]
# }

# best_subject = max(subjects, key=subjects.get)

# print("\n=== Оцінки ===")
# print("Math:", math_stats)
# print("Physics:", physics_stats)
# print("English:", english_stats)
# print("Кращий предмет:", best_subject)

# import random

# # Завдання 1

# print("\n=== Завдання 1 ===")

# arr = [random.randint(0, 50) for _ in range(20)]
# print("Масив:", arr)

# threshold = int(input("Введи порогове число: "))

# count = len([x for x in arr if x > threshold])
# print("Кількість елементів > порогу:", count)

# max_val = max(arr)
# index = arr.index(max_val)
# print("Максимум:", max_val)
# print("Позиція:", index)

# sorted_arr = sorted(arr, reverse=True)
# print("Відсортований:", sorted_arr)


# # Завдання 2

# print("\n=== Завдання 2 ===")

# low = int(input("Нижня межа: "))
# high = int(input("Верхня межа: "))

# matrix = [[random.randint(low, high) for _ in range(5)] for _ in range(5)]

# print("Матриця:")
# for row in matrix:
#     print(row)

# diag = [matrix[i][i] for i in range(5)]
# print("Головна діагональ:", diag)
# print("Сума діагоналі:", sum(diag))

# for i in range(5):
#     for j in range(5):
#         if j > i:
#             matrix[i][j] = 0

# print("Після обнулення:")
# for row in matrix:
#     print(row)


# # Завдання 3

# print("\n=== Завдання 3 ===")

# start = int(input("Початок діапазону: "))
# end = int(input("Кінець діапазону: "))

# seq = list(range(start, end + 1))

# seq = seq[:30]

# matrix = [seq[i:i+5] for i in range(0, 30, 5)]

# print("Матриця 6x5:")
# for row in matrix:
#     print(row)

# row_sums = [sum(row) for row in matrix]
# print("Суми рядків:", row_sums)

# col_max = [max(matrix[i][j] for i in range(6)) for j in range(5)]
# print("Максимуми стовпців:", col_max)


# # Завдання 4

# print("\n=== Завдання 4 ===")

# low = int(input("Нижня межа: "))
# high = int(input("Верхня межа: "))

# arr = [random.randint(low, high) for _ in range(15)]
# print("Масив:", arr)

# negatives = [x for x in arr if x < 0]
# print("Від'ємні:", negatives)

# modified = [x if x >= 0 else 0 for x in arr]
# print("Замінений масив:", modified)

# zero_count = modified.count(0)
# print("Кількість нулів:", zero_count)


# # Завдання 5

# print("\n=== Завдання 5 ===")

# n = int(input("Довжина масивів: "))

# a = [random.randint(0, 10) for _ in range(n)]
# b = [random.randint(10, 20) for _ in range(n)]

# print("Масив A:", a)
# print("Масив B:", b)

# combined = a + b
# print("Об'єднаний:", combined)

# sum_arr = [a[i] + b[i] for i in range(n)]
# diff_arr = [a[i] - b[i] for i in range(n)]

# print("Сума:", sum_arr)
# print("Різниця:", diff_arr)


# # Завдання 6

# print("\n=== Завдання 6 ===")

# rows = int(input("К-сть рядків: "))
# cols = int(input("К-сть стовпців: "))

# matrix = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]

# print("Матриця:")
# for row in matrix:
#     print(row)

# new_rows = int(input("Нові рядки: "))
# new_cols = int(input("Нові стовпці: "))

# flat = [x for row in matrix for x in row]

# new_matrix = [flat[i:i+new_cols] for i in range(0, len(flat), new_cols)]

# print("Нова матриця:")
# for row in new_matrix:
#     print(row)

# row_min = [min(row) for row in new_matrix]
# row_max = [max(row) for row in new_matrix]

# print("Мінімуми:", row_min)
# print("Максимуми:", row_max)

# total_sum = sum(flat)
# print("Загальна сума:", total_sum)

# import pandas as pd

# print("\n=== ЗАВДАННЯ 1: КНИГИ ===")

# books = pd.DataFrame({
#     "Назва": ["Книга A", "Книга B", "Книга C", "Книга D", "Книга E", "Книга F"],
#     "Автор": ["Автор 1", "Автор 2", "Автор 3", "Автор 4", "Автор 5", "Автор 6"],
#     "Рік": [2010, 2018, 2020, 2016, 2012, 2023],
#     "Ціна": [100, 250, 300, 150, 90, 400]
# })

# print("Весь DataFrame:")
# print(books)

# print("\nСередня ціна:", books["Ціна"].mean())

# print("\nПісля 2015:")
# print(books[books["Рік"] > 2015])

# print("\nСортування за ціною:")
# print(books.sort_values("Ціна"))


# print("\n=== ЗАВДАННЯ 2: ЗАМОВЛЕННЯ ===")

# orders = pd.read_csv("orders.csv")

# print("Перші 10 рядків:")
# print(orders.head(10))

# print("\nКількість замовлень:")
# print(orders["Клієнт"].value_counts())

# print("\nМаксимальна сума:", orders["Сума"].max())
# print("Мінімальна сума:", orders["Сума"].min())
# print("Загальна сума:", orders["Сума"].sum())


# print("\n=== ЗАВДАННЯ 3: ПРОДУКТИ ===")

# food = pd.DataFrame({
#     "Продукт": ["М'ясо", "Рис", "Яблуко", "Банан", "Хліб", "Сир", "Молоко", "Гречка", "Курка", "Картопля"],
#     "Категорія": ["Білки", "Вуглеводи", "Фрукти", "Фрукти", "Вуглеводи", "Жири", "Жири", "Вуглеводи", "Білки", "Вуглеводи"],
#     "Калорії": [250, 350, 80, 90, 270, 400, 150, 320, 280, 200],
#     "Білки": [20, 7, 0, 1, 6, 25, 3, 12, 22, 2]
# })

# print("Весь DataFrame:")
# print(food)

# print("\nКалорії > 300:")
# print(food[food["Калорії"] > 300])

# print("\nСередні білки по категоріях:")
# print(food.groupby("Категорія")["Білки"].mean())

# print("\nСортування:")
# print(food.sort_values("Калорії", ascending=False))


# # ЗАВДАННЯ 4 — СПІВРОБІТНИКИ

# print("\n=== ЗАВДАННЯ 4: СПІВРОБІТНИКИ ===")

# workers = pd.DataFrame({
#     "Ім'я": ["Аня", "Іван", "Петро", "Оля", "Денис", "Марія", "Сергій", "Ліза"],
#     "Проект": ["A", "A", "B", "B", "C", "C", "A", "B"],
#     "Години": [10, 20, 15, 25, 30, 5, 12, 18]
# })

# print("Вихідний DataFrame:")
# print(workers)

# print("\nГодини по співробітниках:")
# print(workers.groupby("Ім'я")["Години"].sum())

# print("\nГодини по проектах:")
# print(workers.groupby("Проект")["Години"].sum())

# print("\nНайбільше годин витратив:")
# print(workers.groupby("Ім'я")["Години"].sum().idxmax())


# # ЗАВДАННЯ 5 — КВИТКИ

# print("\n=== ЗАВДАННЯ 5: КВИТКИ ===")

# tickets = pd.DataFrame({
#     "Фільм": ["A", "A", "B", "B", "C", "C", "A", "B", "C", "A", "B", "C"],
#     "Місто": ["Київ", "Львів", "Київ", "Львів", "Київ", "Львів", "Київ", "Львів", "Київ", "Львів", "Київ", "Львів"],
#     "Квитки": [100, 120, 90, 80, 150, 60, 200, 110, 130, 140, 95, 70]
# })

# print("Весь DataFrame:")
# print(tickets)

# print("\nКвитки по фільмах:")
# print(tickets.groupby("Фільм")["Квитки"].sum())

# print("\nКвитки по містах:")
# print(tickets.groupby("Місто")["Квитки"].sum())

# print("\nНайпопулярніший фільм:")
# print(tickets.groupby("Фільм")["Квитки"].sum().idxmax())


# # ЗАВДАННЯ 6 — JOIN

# print("\n=== ЗАВДАННЯ 6: JOIN ===")

# clients = pd.DataFrame({
#     "ID": [1, 2, 3, 4, 5],
#     "Ім'я": ["Іван", "Петро", "Оля", "Марія", "Денис"],
#     "Місто": ["Київ", "Львів", "Харків", "Одеса", "Дніпро"]
# })

# orders2 = pd.DataFrame({
#     "ID клієнта": [1, 2, 1, 3, 4],
#     "Замовлення": ["A", "B", "C", "D", "E"],
#     "Вартість": [100, 200, 150, 300, 250]
# })

# print("Клієнти:")
# print(clients)

# print("\nЗамовлення:")
# print(orders2)

# merged = clients.merge(orders2, left_on="ID", right_on="ID клієнта")

# print("\nОб'єднаний DataFrame:")
# print(merged)

# print("\nСума по клієнтах:")
# print(merged.groupby("Ім'я")["Вартість"].sum())

# import matplotlib.pyplot as plt
# import numpy as np
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# plan = [100, 120, 130, 140, 150, 160]
# fact = [90, 110, 120, 135, 155, 170]

# plt.plot(months, plan, label="План")
# plt.plot(months, fact, label="Факт")

# plt.title("Продажі: План vs Факт")
# plt.xlabel("Місяці")
# plt.ylabel("Продажі")
# plt.legend()

# plt.show()

# ages = np.random.randint(18, 70, 100)

# plt.hist(ages, bins=10, color="skyblue")

# plt.axvline(np.mean(ages), color="red", label="Середнє")

# plt.title("Розподіл віку")
# plt.xlabel("Вік")
# plt.ylabel("Кількість")
# plt.legend()

# plt.show()

# g1 = np.random.randint(50, 100, 30)
# g2 = np.random.randint(40, 90, 30)
# g3 = np.random.randint(60, 100, 30)

# plt.boxplot([g1, g2, g3], labels=["Група 1", "Група 2", "Група 3"])

# plt.title("Порівняння оцінок")
# plt.show()

# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# temp = [20, 22, 21, 19, 23, 24, 22]
# humidity = [60, 65, 63, 70, 68, 66, 64]

# plt.plot(days, temp, label="Температура")
# plt.plot(days, humidity, label="Вологість")

# plt.xticks(rotation=45)

# plt.title("Погода за тиждень")
# plt.legend()
# plt.show()

# hours = list(range(24))
# load = [30, 25, 20, 22, 18, 15, 20, 30, 50, 60, 70, 80,
#         90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35]

# plt.plot(hours, load, color="green")
# plt.fill_between(hours, load, alpha=0.3)

# plt.title("Навантаження сервера")
# plt.xlabel("Години")
# plt.ylabel("Load")
# plt.grid()

# plt.show()

# x = np.arange(1, 11)

# conv = np.random.rand(10)
# ret = np.random.rand(10)
# avg_check = np.random.rand(10)
# orders = np.random.rand(10)

# fig, axs = plt.subplots(2, 2, figsize=(10,8))

# axs[0,0].plot(x, conv)
# axs[0,0].set_title("Конверсія")

# axs[0,1].plot(x, ret)
# axs[0,1].set_title("Утримання")

# axs[1,0].plot(x, avg_check)
# axs[1,0].set_title("Середній чек")

# axs[1,1].plot(x, orders)
# axs[1,1].set_title("Замовлення")

# plt.suptitle("Метрики продукту")

# plt.show()

# Поліноміальна регресія та регуляризація

# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score

# data = fetch_california_housing(as_frame=True)

# X = data.data[['MedInc']]
# y = data.target

# poly = PolynomialFeatures(degree=2, include_bias=False)
# X_poly = poly.fit_transform(X)

# X_train, X_test, y_train, y_test = train_test_split(
#     X_poly, y, test_size=0.2, random_state=42
# )

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# r2 = r2_score(y_test, y_pred)

# print("R² на тестовій вибірці:", r2)





# data = fetch_california_housing(as_frame=True)

# X = data.data[['MedInc']]
# y = data.target

# results = []

# for degree in [1, 2, 3]:

#     poly = PolynomialFeatures(degree=degree, include_bias=False)
#     X_poly = poly.fit_transform(X)

#     X_train, X_test, y_train, y_test = train_test_split(
#         X_poly, y, test_size=0.2, random_state=42
#     )

#     model = LinearRegression()
#     model.fit(X_train, y_train)

#     y_train_pred = model.predict(X_train)
#     y_test_pred = model.predict(X_test)

#     train_r2 = r2_score(y_train, y_train_pred)
#     test_r2 = r2_score(y_test, y_test_pred)

#     results.append([degree, train_r2, test_r2])

# results_df = pd.DataFrame(
#     results,
#     columns=['Ступінь полінома', 'R² train', 'R² test']
# )

# print(results_df)






# data = fetch_california_housing(as_frame=True)

# features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms']

# X = data.data[features]
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# lr_model = LinearRegression()
# lr_model.fit(X_train, y_train)

# lr_pred = lr_model.predict(X_test)
# lr_r2 = r2_score(y_test, lr_pred)

# lasso_model = Lasso(alpha=0.1)
# lasso_model.fit(X_train, y_train)

# lasso_pred = lasso_model.predict(X_test)
# lasso_r2 = r2_score(y_test, lasso_pred)

# zero_coef = sum(lasso_model.coef_ == 0)

# print("LinearRegression R²:", lr_r2)
# print("Lasso R²:", lasso_r2)

# print("\nКоефіцієнти LinearRegression:")
# print(lr_model.coef_)

# print("\nКоефіцієнти Lasso:")
# print(lasso_model.coef_)

# print("\nКількість нульових коефіцієнтів у Lasso:", zero_coef)






# data = fetch_california_housing(as_frame=True)

# features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms']

# X = data.data[features]
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# lr_model = LinearRegression()
# lr_model.fit(X_train, y_train)

# lr_pred = lr_model.predict(X_test)
# lr_r2 = r2_score(y_test, lr_pred)

# ridge_model = Ridge(alpha=1.0)
# ridge_model.fit(X_train, y_train)

# ridge_pred = ridge_model.predict(X_test)
# ridge_r2 = r2_score(y_test, ridge_pred)

# lr_nonzero = np.sum(lr_model.coef_ != 0)
# ridge_nonzero = np.sum(ridge_model.coef_ != 0)

# results = pd.DataFrame({
#     'Модель': ['LinearRegression', 'Ridge(alpha=1.0)'],
#     'Тест R²': [lr_r2, ridge_r2],
#     'Кількість ненульових коеф.': [lr_nonzero, ridge_nonzero]
# })

# print(results)









# Дерева рішень, ансамблі та класифікація
# import numpy as np
# import pandas as pd

# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split

# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor

# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import (
#     r2_score,
#     confusion_matrix,
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score
# )

# from xgboost import XGBRegressor




# housing = fetch_california_housing(as_frame=True)

# X = housing.data[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms']]
# y = housing.target



# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42
# )

# tree_model = DecisionTreeRegressor(
#     max_depth=4,
#     random_state=42
# )

# tree_model.fit(X_train, y_train)

# y_pred_tree = tree_model.predict(X_test)

# r2_tree = r2_score(y_test, y_pred_tree)

# print("=== Завдання 1 ===")
# print(f"R² для Decision Tree: {r2_tree:.4f}")



# forest_model = RandomForestRegressor(
#     n_estimators=100,
#     random_state=42
# )

# forest_model.fit(X_train, y_train)

# y_pred_forest = forest_model.predict(X_test)

# r2_forest = r2_score(y_test, y_pred_forest)

# results_task2 = pd.DataFrame({
#     'Модель': ['Decision Tree', 'Random Forest'],
#     'R²': [r2_tree, r2_forest]
# })

# print("\n=== Завдання 2 ===")
# print(results_task2)



# xgb_model = XGBRegressor(
#     n_estimators=200,
#     learning_rate=0.1,
#     max_depth=5,
#     random_state=42
# )

# xgb_model.fit(X_train, y_train)

# y_pred_xgb = xgb_model.predict(X_test)

# r2_xgb = r2_score(y_test, y_pred_xgb)

# results_task3 = pd.DataFrame({
#     'Модель': ['Random Forest', 'XGBoost'],
#     'R²': [r2_forest, r2_xgb]
# })

# print("\n=== Завдання 3 ===")
# print(results_task3)


# median_price = np.median(y)

# y_class = (y > median_price).astype(int)

# X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
#     X,
#     y_class,
#     test_size=0.2,
#     random_state=42
# )

# log_model = LogisticRegression(max_iter=1000)

# log_model.fit(X_train_cls, y_train_cls)

# y_pred_cls = log_model.predict(X_test_cls)

# cm = confusion_matrix(y_test_cls, y_pred_cls)

# accuracy = accuracy_score(y_test_cls, y_pred_cls)
# precision = precision_score(y_test_cls, y_pred_cls)
# recall = recall_score(y_test_cls, y_pred_cls)
# f1 = f1_score(y_test_cls, y_pred_cls)

# print("\n=== Завдання 4 ===")

# print("\nConfusion Matrix:")
# print(cm)

# print(f"\nAccuracy : {accuracy:.4f}")
# print(f"Precision: {precision:.4f}")
# print(f"Recall   : {recall:.4f}")
# print(f"F1-score : {f1:.4f}")






# # Базова регресія
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.datasets import load_diabetes
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import (
#     mean_absolute_error,
#     mean_squared_error,
#     r2_score
# )



# diabetes = load_diabetes()

# X = diabetes.data[:, 2]

# X = X.reshape(-1, 1)

# y = diabetes.target



# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# model = LinearRegression()

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("=== Завдання 1 ===")
# print("\nПерші 10 реальних та передбачених значень:\n")

# results = pd.DataFrame({
#     'Реальні значення': y_test[:10],
#     'Передбачення': y_pred[:10]
# })

# print(results)



# plt.figure(figsize=(8, 5))

# plt.scatter(X_test, y_test, color='blue', label='Реальні дані')

# plt.plot(X_test, y_pred, color='red', linewidth=2,
#          label='Лінія регресії')

# plt.xlabel('BMI')
# plt.ylabel('Цільова змінна')
# plt.title('Лінійна регресія для датасету Diabetes')

# plt.legend()
# plt.grid(True)

# plt.show()



# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# metrics_table = pd.DataFrame({
#     'Метрика': ['MAE', 'MSE', 'R²'],
#     'Значення': [mae, mse, r2]
# })

# print("\n=== Завдання 3 ===")
# print(metrics_table)

# X_train_gd = X_train.flatten()
# X_test_gd = X_test.flatten()


# def gradient_descent(X, y, lr=0.1, epochs=1000):

#     w = 0
#     b = 0

#     n = len(X)

#     for i in range(epochs):

#         y_pred = w * X + b

#         error = y_pred - y

#         dw = (2/n) * np.sum(error * X)
#         db = (2/n) * np.sum(error)

#         w = w - lr * dw
#         b = b - lr * db

#     return w, b


# w, b = gradient_descent(X_train_gd, y_train)

# y_pred_gd = w * X_test_gd + b

# mae_gd = mean_absolute_error(y_test, y_pred_gd)

# mae_sklearn = mean_absolute_error(y_test, y_pred)

# print("\n=== Завдання 4 ===")

# print(f"\nКоефіцієнт w: {w:.4f}")
# print(f"Коефіцієнт b: {b:.4f}")

# comparison = pd.DataFrame({
#     'Модель': ['Gradient Descent', 'LinearRegression'],
#     'MAE': [mae_gd, mae_sklearn]
# })

# print("\nПорівняння моделей:")
# print(comparison)








# Побудова багатошарового персептрона (MLP)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import torch
import torch.nn as nn
import torch.optim as optim


data = load_breast_cancer()

X = data.data
y = data.target

df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y

print("Перші 5 рядків:")
print(df.head())


print("\n=== Баланс класів ===")
print(df['target'].value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)

y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)


input_size = X_train.shape[1]

model = nn.Sequential(
    nn.Linear(input_size, 16),
    nn.ReLU(),

    nn.Linear(16, 8),
    nn.ReLU(),

    nn.Linear(8, 1),
    nn.Sigmoid()
)

print("\n=== Архітектура моделі ===")
print(model)


criterion = nn.BCELoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 30

loss_history = []
accuracy_history = []

for epoch in range(epochs):

    model.train()

    outputs = model(X_train_tensor)

    loss = criterion(outputs, y_train_tensor)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    predicted = (outputs >= 0.5).float()

    accuracy = (
        predicted.eq(y_train_tensor)
        .sum()
        .item()
        / y_train_tensor.shape[0]
    )

    loss_history.append(loss.item())
    accuracy_history.append(accuracy)

    print(
        f"Epoch [{epoch+1}/{epochs}] | "
        f"Loss: {loss.item():.4f} | "
        f"Accuracy: {accuracy:.4f}"
    )



model.eval()

with torch.no_grad():

    test_outputs = model(X_test_tensor)

    test_loss = criterion(
        test_outputs,
        y_test_tensor
    )

    test_predicted = (test_outputs >= 0.5).float()

    test_accuracy = accuracy_score(
        y_test,
        test_predicted.numpy()
    )

print("\n=== ПІДСУМКОВІ МЕТРИКИ ===")

results = pd.DataFrame({
    'Метрика': ['Loss', 'Accuracy'],
    'Значення': [
        test_loss.item(),
        test_accuracy
    ]
})

print(results)



plt.figure(figsize=(8, 5))

plt.plot(
    range(1, epochs + 1),
    loss_history,
    color='red',
    label='Loss'
)

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss during training')

plt.legend()
plt.grid(True)

plt.savefig('loss_healthrisk_mlp.png')

plt.show()



plt.figure(figsize=(8, 5))

plt.plot(
    range(1, epochs + 1),
    accuracy_history,
    color='blue',
    label='Accuracy'
)

plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy during training')

plt.legend()
plt.grid(True)

plt.savefig('accuracy_healthrisk_mlp.png')

plt.show()

