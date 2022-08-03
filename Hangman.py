import random
word_list = ['труп', 'кофе', 'попугай', 'оружие', 'футболка', 'мотоцикл', 'компютер', 'желтый', 'фонарь', 'полицейский', 'стрижка', 'монета', 'шаурма', 'вода', 'счастье', 'погода', 'президент', 'стул', 'время', 'любовь']
def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()
def display_hangman(tries):
    stages = ['''--------
|      |
|      0
|     \\|/
|      |
|     / \\
-''',
'''--------
|      |
|      0
|     \\|/
|      |
|     /
-''',
'''--------
|      |
|      0
|     \\|/
|      |
|
-''',
'''--------
|      |
|      0
|     \\|
|      |
|
-''',
'''--------
|      |
|      0
|      |
|      |
|
-''',
'''--------
|      |
|      0
|
|
|''',
'''--------
|      |
|
|
|
|
-''']
    return stages[tries]
def is_valid_lvsw(lvsw):
    while not(lvsw.isdigit()):
        lvsw = input('Выберите либо [1], либо [2]')
    else:
        while lvsw != '1' and lvsw != '2':
            lvsw = input('Камон чувак, ты настолько тупой, что даже не можешь нажать 1 или 2 и потом Enter')
        else:
            return int(lvsw)
def is_valid_letter(tries_letter):
    while not(tries_letter.isalpha()) or len(tries_letter) > 1:
        tries_letter = input('Хватит тупить и введи уже по нормальному букву')
    else:
        return tries_letter.upper()
def is_valid_word(tries_word, word):
    while not(tries_word.isalpha()) or len(tries_word) != len(word):
        tries_word = input('Хватит тупить и введи уже по нормальному слово')
    else:
        return tries_word.upper()
def is_valid_bc(bc):
    while not(bc.isalpha()):
        bc = input('[да] или [нет]')
    else:
        while bc != 'да' and bc != 'нет':
            bc = input('[да] или [нет]')
        else:
            return bc.lower()
def play(word):
    word_completion = [' - '] * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(*word_completion)
    print('Перед вами пердставлена длина загаданного слова и состояние виселицы. Когда все попытки угдадать слова закончаться то человек будет повешен. Попытайтесь угадать ради вашего же блага')
    while tries != 0 and ''.join(word_completion) != word:
        lvsw = input('Вы хотите сказать букву или все слово целиком? Введите [1] или [2]')
        lvsw = is_valid_lvsw(lvsw)
        if lvsw == 1:
            tries_letter = input('Введите букву')
            tries_letter = is_valid_letter(tries_letter)
            if not(tries_letter in word):
                if not(tries_letter in guessed_letters):
                    tries -= 1
                    guessed_letters.append(tries_letter)
                    print(display_hangman(tries))
                else:
                    print('Вы ввели уже не правильно названную ранее букву. Потыайтесь снова')
            elif tries_letter in word:
                if not(tries_letter in guessed_letters):
                    guessed_letters.append(tries_letter)
                    for i in range(len(word)):
                        if word[i] == tries_letter:
                            word_completion[i] = tries_letter
                    print(*word_completion)
                else:
                    print('Вы ввели уже правильно названную ранее букву. Попытайтесь снова')
        if lvsw == 2:
            tries_word = input('Введите слово')
            tries_word = is_valid_word(tries_word, word)
            if tries_word != word:
                if not(tries_word in guessed_words):
                    tries -= 1
                    guessed_words.append(tries_word)
                    print(display_hangman(tries))
                else:
                    print('Вы ввели уже не правильно названное ранее слово. Попытайтесь снова')
            elif tries_word == word:
                word_completion = tries_word
                print(word_completion)
    else:
        if ''.join(word_completion) == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
        else:
            print('Загаданное слово: ' + word)
while True:
    play(get_word(word_list))
    bc = input('Желаете ли вы продолжить игру? [да] или [нет]').lower()
    bc = is_valid_bc(bc)
    if bc == 'нет':
        break
