gender = {
    'female': 'Дорогая',
    'male': 'Дорогой'
}

people = [
    ["Лучик", "Иван", 78, 'male'],
    ["Иванова", "Тамара", -35, 'female'],
    ["Рамашкин", "Сергей", 95, 'male'],
]
doljniki = str()
for lastName,name,balance,pol in people:
    if balance < 0:

        dolg = f"""{gender[pol]} {lastName} {name} задолженость ваше лицевого счета
состовляет {balance} рублей"""
        doljniki = f"""{doljniki} {lastName} {name} долг {balance} |"""

        print(dolg)
    else:
        text = f"""{gender[pol]} {lastName} {name} баланс вашего лицевого счета
состовляет {balance} рублей"""
        print(text)

print('Doljniki',doljniki)