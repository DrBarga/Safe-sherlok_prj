import time
from ip_adress import get_ip_info
from phonenum import phonenum, lookup_phone_number
from nick import osint

print('''
Sherlok
Load...''')

while True:
    print('''
    Information of IP adress    -[1]
    Information of nick name    -[2]
    Information of phonenumbers -[3]
    exit                        -[4]''')
    inf = input('enter selection:')

    if inf == '1':
        print()
        ip_adress = input('Enter IP adress:')
        print('Wait...')
        print(get_ip_info(ip_adress))



    elif inf == '2':
        print()
        nick = input('select nick:')
        print('Wait...')
        print(osint(nick))

    elif inf == '3':
        print()
        num = input('select number:')
        print('Wait...')
        print(phonenum(num))
        print(lookup_phone_number(num))

    elif inf == '4':
        print('exitin...')
        time.sleep(1)
        break