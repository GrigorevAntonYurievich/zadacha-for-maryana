import re

# Функция для приведения номера телефона к стандартному формату
def normalize_phone(phone):
    # Удаляем все символы, кроме цифр
    phone = re.sub(r'\D', '', phone)
    # Если номер начинается с 8, заменяем на +7
    if phone.startswith('8'):
        phone = '+7' + phone[1:]
    # Если код не указан, считаем, что это 495
    if len(phone) == 7:
        phone = '+7(495)' + phone
    return phone

# Функция для сравнения двух номеров телефона
def compare_phones(phone1, phone2):
    # Нормализуем номера телефонов и выделяем код и номер
    phone1 = normalize_phone(phone1)
    phone2 = normalize_phone(phone2)
    match1 = re.search(r'\((\d{3})\)', phone1)
    code1 = match1.group(1) if match1 else ''
    number1 = re.sub(r'\D', '', phone1)[-7:]
    match2 = re.search(r'\((\d{3})\)', phone2)
    code2 = match2.group(1) if match2 else ''
    number2 = re.sub(r'\D', '', phone2)[-7:]
    # Проверяем совпадение кодов и номеров
    if code1 == code2 and number1 == number2:
        return 'YES'
    else:
        return 'NO'

# Считываем номер, который Вася хочет добавить
new_phone = input().strip()

# Считываем три номера, которые уже есть в адресной книге
phones = [input().strip() for _ in range(3)]

# Проверяем совпадение каждого номера с новым номером
for phone in phones:
    print(compare_phones(new_phone, phone))
