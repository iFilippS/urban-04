
# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен
# подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
#     Функция count_calls подсчитывающая вызовы остальных функций.
#     Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в
#       верхнем регистре, строку в нижнем регистре.
#     Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится
#       в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
#     Создать переменную calls = 0 вне функций.
#     Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться
#       в остальных двух функциях.
#     Создать функцию string_info с параметром string и реализовать логику работы по описанию.
#     Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
#     Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
#     Вывести значение переменной calls на экран(в консоль).


calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(imp_str):
    count_calls()

    # Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в
    # верхнем регистре, строку в нижнем регистре.

    imp_str_len = len(imp_str)
    imp_str_Upp = imp_str.upper()
    imp_str_low = imp_str.lower()
    return (imp_str_len, imp_str_Upp, imp_str_low)


def is_contains(imp_str, imp_list):
    count_calls()

    # Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится
    # в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

    bool_imp_list = [imp_str.lower() == item.lower() for item in imp_list]

    return any(bool_imp_list)


print(string_info('Привет, Мир!!!'))
print(is_contains('222U', ['1', '2222u', '4'])) # 222U not 2222u
print(string_info('Hello, World!!!'))
print(is_contains('URBAN', ['UrlaN', 'Urbann', 'Urba'])) # Urbann not URBAN
print()

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print()
print(calls)
