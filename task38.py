'''Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных'''

path = 'task38.txt'
data = open(path, 'r+')
print('Телефонный справочник')
for line in data:
    print(line)
newone = str(input("Введитие нового абонента\n"))
write_string = '\n'+newone
data.writelines(write_string)
data.close()

path = 'task38.txt'
print('Обновленный телефонный справочник')
data = open(path, 'r')
for line in data:
    print(line)
data.close()