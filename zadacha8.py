def format_phone_number(phone):
    phone = ''.join(filter(str.isdigit, phone))
    
    if phone.startswith('8'):
        phone = '495' + phone[1:]
    
    elif phone.startswith('+7'):
        phone = '495' + phone[2:]
    
    return phone

vasya_phone = format_phone_number(input())
phone_book = [format_phone_number(input()) for _ in range(4)]

for number in phone_book:
    if number == vasya_phone:
        print("YES")
    else:
        print("NO")
