
# Завдання 1 (Температура)

temperatures = [2, 5, 4, 6, 7, 3, 1]

avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)
diff = max_temp - min_temp

print("=== Температура ===")
print("Середнє:", avg_temp)
print("Максимум:", max_temp)
print("Мінімум:", min_temp)
print("Різниця:", diff)


# Завдання 2 (Витрати)

expenses = [1200, 1500, 800, 600, 1000, 400, 900]

total = sum(expenses)
avg = total / len(expenses)
max_val = max(expenses)
min_val = min(expenses)
days_over_1000 = len([x for x in expenses if x > 1000])

print("\n=== Витрати ===")
print("Сума:", total)
print("Середнє:", round(avg, 2))
print("Максимум:", max_val)
print("Мінімум:", min_val)
print("Днів > 1000:", days_over_1000)


# Завдання 3 (Голоси)

from collections import Counter

votes = ["apple", "banana", "apple", "orange", "banana", "apple", "apple", "apple", "orange"]

counter = Counter(votes)
leader = counter.most_common(1)[0]
top3 = counter.most_common(3)

print("\n=== Голоси ===")
for fruit, count in counter.items():
    print(f"{fruit}: {count}")

print("Лідер:", leader)
print("Топ-3:", top3)


# Завдання 4 (Оцінки)

math = [80, 92, 75, 60, 88]
physics = [70, 65, 90, 85, 78]
english = [95, 100, 85, 90, 87]

def stats(subject):
    return sum(subject)/len(subject), min(subject), max(subject)

math_stats = stats(math)
physics_stats = stats(physics)
english_stats = stats(english)

subjects = {
    "math": math_stats[0],
    "physics": physics_stats[0],
    "english": english_stats[0]
}

best_subject = max(subjects, key=subjects.get)

print("\n=== Оцінки ===")
print("Math:", math_stats)
print("Physics:", physics_stats)
print("English:", english_stats)
print("Кращий предмет:", best_subject)