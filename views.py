import re

from utils import SingletonMeta
from exception import InvalidInputNumException


class AuthView(metaclass=SingletonMeta):
    def __init__(self):
        self.data = None

    # 로그인 페이지에 필요한 내용을 보여주고, id를 입력받습니다. 결과값으로 입력받은 id를 반환합니다.
    def show_login_view(self):
        print('--------식권대장---------\n')
        input_login_id = input('로그인이 필요한 서비스입니다. 아이디를 입력해주세요. : ')

        return input_login_id


class MainServiceView(metaclass=SingletonMeta):
    def __init__(self):
        self.data = None

    # 식당 목록을 보여주고, 사용자가 선택한 식당 번호를 입력 받습니다. 결과 값으로 해당 식당 번호를 반환합니다.
    def show_restaurant_view(self, restaurant_list):
        message = '\n0. 종료'
        restaurant_id_list = [restaurant['id'] for restaurant in restaurant_list]

        for restaurant in restaurant_list:
            restaurant_id = restaurant.get('id')
            restaurant_name = restaurant.get('name')
            message = message + '\n{restaurant_id}.{restaurant_name}'.format(restaurant_id=restaurant_id,
                                                                             restaurant_name=restaurant_name)

        input_num = int(input('원하시는 가게의 번호를 입력해주세요. 아래는 가게 목록입니다.' + message + '\n\n 번호 입력 : '))

        if input_num == 0:
            print('서비스를 종료합니다.')
            quit()

        if input_num not in restaurant_id_list:
            print('존재하지 않는 번호입니다. 다시 입력해주세요\n')
            raise InvalidInputNumException('')

        return input_num

    # 매개 변수로 받은 메뉴 목록을 보여주고, 결제를 진행합니다.
    def show_menu_view(self, menu_list):
        message = '\n0. 종료'
        menu_id_price_list = [{'id': menu['id'], 'price': menu['price']} for menu in menu_list]

        for menu in menu_list:
            menu_id = menu.get('id')
            menu_name = menu.get('name')
            menu_price = menu.get('price')

            message = message + '\n{menu_id}.{menu_name} \n 가격 : {menu_price}'.format(menu_id=menu_id,
                                                                                      menu_name=menu_name,
                                                                                      menu_price=menu_price)

        input_num = int(input('원하시는 메뉴의 번호를 입력해주세요. 아래는 메뉴 목록입니다.' + message + '\n\n 번호 입력 : '))

        for dict in menu_id_price_list:
            if input_num == 0:
                print('서비스를 종료합니다.')
                quit()

            if dict['id'] == input_num:
                price = dict['price']
                print("{price}원이 결제되었습니다.".format(price=price))
                quit()

        print('존재하지 않는 번호입니다. 다시 입력해주세요\n')
        raise InvalidInputNumException('')

    def show_admin_view(self):
        input_num = int(input('원하시는 작업의 번호를 입력해주세요. 아래는 작업 목록입니다.\n'
                              '0.종료\n'
                              '1.일반 주문\n'
                              '2.식사 시간 변경'))

        if input_num == 0:
            print('서비스를 종료합니다.')
            quit()

        if input_num == 1 or input_num == 2:
            return input_num

        print('존재하지 않는 번호입니다. 다시 입력해주세요\n')
        raise InvalidInputNumException('')

    def show_change_mealtime_view(self):
        input_detail = input('변경하려는 시간을 입력해주세요. 입력 양식은 다음과 같습니다.\n'
                             '아침/점심/저녁 여부, 시작 시간, 종료 시간\n'
                             '아침, 점심, 저녁은 각각 1,2,3으로 표현합니다.\n'
                             '아침 시간을 8시에서 13시로 바꾸려면 아래와 같이 입력하면 됩니다.\n'
                             'ex) 1, 08:00, 13:00\n\n'
                             '입력하기 : ')

        input_detail = re.sub(r'\s', '', input_detail)  # 공백 없애기

        # '1,08:00,13:00' 형태 확인하는 정규식. 앞 부분은 00~23, 뒷 부분은 00~59만 입력할 수 있다.
        pattern = r'^[1-3],(?:[01][0-9]|2[0-3]):[0-5][0-9],(?:[01][0-9]|2[0-3]):[0-5][0-9]$'
