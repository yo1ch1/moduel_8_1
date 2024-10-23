
def add_everything_up(a, b):
    try:
        result = a + b
        return round(result, 3)
    except TypeError:
        result = str(a) + str(b)
        return result
    finally:
        print('Несмотря на ошибку программа завершила свою работу')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
