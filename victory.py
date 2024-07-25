# - количество правильных ответов
# - количество ошибок
# - процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
# - процент неправильных ответов
# После вывода информации программа спрашивает
#
# пользователя хочет ли он начать игру сначала, если да - то повторяем все сначала, если ответ нет - выходим из программы

# исходные данные
Date_Pushkin = '1799'
Date_Groznij = '1530'
Date_Chehov = '1860'
Date_Pasternak = '1890'
Date_Bianki = '1894'

answer_true = 0  # кол-во правильных ответов
percent_true = 0.0  # кол-во правильных ответов в %
answer = ''  # здесь храним данные по ответам

player_want = 1  # пожелание играть 1= хотим,0 - не хотим
while player_want != '0':
    answer = input("введите дату рождения А.С. Пушкина ")
    if answer == Date_Pushkin:
        answer_true += 1

    answer = input("введите дату рождения Ивана Грозного ")
    if answer == Date_Groznij:
        answer_true += 1

    answer = input("введите дату рождения Чехова ")
    if answer == Date_Chehov:
        answer_true += 1

    answer = input("введите дату рождения Пастернака ")
    if answer == Date_Pasternak:
        answer_true += 1

    answer = input("введите дату рождения Бианки ")
    if answer == Date_Bianki:
        answer_true += 1

    print('кол-во верных ответов = ', answer_true)
    print('кол-во верных ответов в % = ', answer_true * 100 / 5)
    print('кол-во Не верных ответов = ', 5 - answer_true)
    print('кол-во Не верных ответов в % = ', 100 - answer_true * 100 / 5)
    answer_true=0 # обнуляем

    player_want = input("Повторим викторину ? (1/0) ")
