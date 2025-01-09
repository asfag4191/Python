menu=['🍔 Cheeseburger',
      '🍟 Fries',
      '🥤 Soda',
      '🍦 Ice Cream',
      '🍪 Cookie']


def welcome():
    print('Velkommen til resturanten, menyen er:\n')
    for i in range(1,len(menu)+1):
        print(f'Press {i} for å bestille: {menu[i-1]}')

def get_item(order):
    if order==1:
            print('Takk for bestilling!')
    elif order==2:
        print('Takk for bestilling!')
    elif order==3:
        print('Takk for bestilling!')
    elif order==4:
        print('Takk for bestilling!')
    elif order==5:
        print('Takk for bestilling!')
    else:
         print('Det har vi ikke på menyen')

if __name__ == '__main__':
    welcome=welcome()
    order=int(input('hva vil du bestille? '))
    order=get_item(order)

