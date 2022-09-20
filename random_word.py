import random as r


def main():
    while True:
        print('Давай сыграем в угадайку!')
        word_list = [   'верблюд', 'кошка', 'собака', 'женщина', 'деньги', 'машина', 'проблема', 
                    'решение', 'история', 'власть', 'тысяча',
                    'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 
                    'развитие', 'процесс', 'условие', 'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 
                    'действие', 'государство', 'любовь', 'взгляд', 'общество', 'деятельность', 'организация', 'президент', 
                    'комната', 'порядок', 'момент', 'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 
                    'смерть', 'программа', 'задача', 'предприятие', 'разговор', 'правительство', 'производство', 'информация', 
                    'положение', 'интерес', 'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 
                    'материал', 'неделя', 'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 
                    'документ', 'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
                    'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
                    'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
                    'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 
                ]
        word = get_word(word_list)
        #print(word)
        #count = 6
        #state = display_hangman(count)
        #print('Ваше состояние:', state)
        main_game = play_game(word)
        if main_game:
            print('Поздравляю, вы победили!!!\nЗагаданное слово', word)
        else:
            print('К сожалению вы проиграли, загаданное слово:', word)
        game = input('Хотите еще сыграть? д - да, н - нет ').upper()
        if game != 'д'.upper():
            print('Хорошего дня!')
            break


def get_word(words):
    """return random words from list"""
    result = r.choice(words)
    return result.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def input_parametre():
    text = input('Введите букву или слово: ').upper()
    while not text.isalpha():
        text = input('Введите букву или слово: ').upper()
    return text


def play_game(text):
    star = '*'
    word = list('*' * len(text))
    flag = True 
    guess_letters = []
    guess_words = []
    count = 6
    print('Ваше состояние', display_hangman(count))
    while star in word and count > 0:
        print('Слово:', ''.join(word))
        char = input_parametre()
        if char in text:
            if len(char) == 1:
                if char in guess_letters:
                    print('Вы уже называли эту букву.')
                    continue
                else:
                    print('Эта буква есть в загаданном слове.')
                    guess_letters.append(char)
                    idx = [i for i, j in enumerate(text) if j == char]
                    for i in range(len(idx)):
                        word[idx[i]] = char
            elif len(char) > 1:
                if char in guess_words:
                    print('Вы уже угадывали это слово.')
                    continue
                elif char == text:
                    #print('Поздравляю, вы угадали!!!')
                    guess_words.append(char)
                    break
                else: 
                    count -= 1
                    print('Это неверный ответ, ваше состояние', display_hangman(count))
                    guess_words.append(char)       
        else:
            if char in guess_letters or char in guess_words:
                print('Вы уже пробовали эту букву или слово...')
            else:
                count -= 1
                if len(char) == 1:
                    print('К сожалению, такой буквы нету')
                    guess_letters.append(char)
                elif len(char) > 1:
                    guess_words.append(char)
                    print('К сожалению, ответ неверный')
                print('Ваше состояние:', display_hangman(count))

    if count == 0:
        flag = False
    return flag
main()           
        


