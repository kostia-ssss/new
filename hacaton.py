NPENA = {
    'Коля' : {
        'Посада' : 'Директор',
        'Коефіціент ефективності' : 90.5,
        'Назви останіх трьох проектів' : 'Вічний двигун , машина часу , ракета на марс',
        'вік' : 34
    },
    'Вася' : {
        'Посада' : 'Помічник будівельника',
        'Коефіціент ефективності' : 67.2,
        'Назви останіх трьох проектів' : 'будинок , 3-х поверховий будинок , лікарня',
        'вік' : 20
    },
    'Марк' : {
        'Посада' : 'Електрик',
        'Коефіціент ефективності' : 72.3,
        'Назви останіх трьох проектів' : 'Вуличне освітленя , ліхтар на колесах , гірлянда',
        'вік' : 28
    }
}
print("Тренінги ProTeam")
print("1-надрукувати всі прізвища, 2-надрукувати всі посади")
answer = input("Номер дії (off-вийти)")
while answer != "off":
    if answer == "1":
        for name in NPENA:
            print('-' , name)
    if answer == "2":
        for name in NPENA:
            print('-' , NPENA[name]['Посада'])
    answer = input("Номер дії (off-вийти)")

