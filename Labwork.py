import re, math , time


print("Привет,я выполняю Лабороторную работу по Python")
print("Чтобы продолжить введи имя пользователя")
while True:
    username=input("Введите имя пользователя на английском языке: ")

    if re.match(r'^[a-zA-Z0-9]+$', username):
        print("Отлично! Введите пароль чтобы завершить аутентификацию!")
        time.sleep(1.5)     
        Pometka_pass=print('''
        Ученик группы 632 - ПОМНИ!
                           
        Пароль считается надёжным если он содержит:
        1.Не менее 8 символов.                     
        2.Как минимум одну заглавную букву.
        3.Как минимум одну строчную букву.
        4.Как минимум одну цифру.
        5.Как минимум один специальный символ. 
        6.Должен содержать латинские символы.''')
        time.sleep(1.5)
        valid_password = False
        while not valid_password:
         password = input("Введите пароль: ")
         krit1 = len(password) >=8
         krit2 = any(char.isupper()for char in password)
         krit3 = any(char.islower()for char in password)
         krit4 = any(char.isdigit()for char in password)
         spec_simvol = "!@#$%^&*()_"
         krit5 = any(char in spec_simvol for char in password)
         simvol_eng=('^[a-zA-Z]+$')
         krit6 = any(char in simvol_eng for char in password)
         if krit1 and krit2 and krit3 and krit4 and krit5 and krit6:
            valid_password = True
            print("Вы успешно авторизировались,пароль соответствует критериям!")
         else:
            print("Введите пароль соответствующий всем критериям")
            
        time.sleep(1.5)
        print("Ожидайте, идёт обработка данных!")
        time.sleep(1.5)
        number=int(input("Введите число для расчёта факториала:"))
        if number < 0:
            print("Факториал отрицательных чисел не определён.")
        elif number == 0:
            print("Факториал числа 0 равен 1.")
        else:
            factorial =1
            for i in range(1, number + 1):
                factorial *= i
            print (f"Факториал числа {number} равен {factorial}.")
        break
    else:
        print("Извините,но имя пользователя вводится на английском языке. Попробуйте снова")

