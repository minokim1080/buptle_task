from datetime import datetime

from utils import FileUtils
from utils import SingletonMeta
from exception import LoginIdNotFoundException


class Account:
    account_url = './resource/account_list.json'
    file_utils = FileUtils()
    account_list = file_utils.open_file_as_list(account_url)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.login_id = kwargs['login_id']
        self.role = kwargs['role']

    # 입력받은 login_id 에 해당하는 Account 인스턴스를 만들어서 반환합니다. 없을 경우 LoginIdNotFoundException 예외를 발생시킵니다.
    @staticmethod
    def login(login_id):
        account_list = Account.account_list

        for account in account_list:
            if account.get('login_id') == login_id:
                login_account = Account(**account)

                return login_account

        raise LoginIdNotFoundException('아이디를 찾을 수 없습니다.')

    def get_role(self):
        return self.role


class Restaurant:
    restaurant_url = './resource/restaurant_list.json'
    file_utils = FileUtils()
    restaurant_list = file_utils.open_file_as_list(restaurant_url)

    def __init__(self, id, name, menu_list=None):
        self.id = id
        self.name = name
        self.menu_list = menu_list  # Menu 인스턴스로 이루어진 리스트

    # 모든 식당 정보를 id 값이 오름차순이 되도록 정렬하여 반환합니다.
    @staticmethod
    def find_all_restaurant():
        restaurant_list = Restaurant.restaurant_list

        sorted_list = sorted(restaurant_list, key=lambda x: x['id'])

        return sorted_list

    def show_menus(self):
        pass


class Menu:
    menu_url = './resource/menu_list.json'
    file_utils = FileUtils()
    menu_list = file_utils.open_file_as_list(menu_url)

    def __init__(self, id, name, restaurant_id, price, time):
        self.id = id
        self.name = name
        self.restaurant_id = restaurant_id
        self.price = price
        self.time = time

    # 특정 시간대, 식당의 메뉴들을 모두 반환하는 메소드입니다.
    @staticmethod
    def find_menus_of_restaurant(restaurant_id, time):
        menu_list = Menu.menu_list

        menus_of_restaurant = [menu for menu in menu_list if menu['restaurant_id'] == restaurant_id
                               and menu['time'] == time]

        return menus_of_restaurant


class Mealtime(metaclass=SingletonMeta):
    mealtime_url = './resource/mealtime.json'
    file_utils = FileUtils()
    mealtime = file_utils.open_file_as_list(mealtime_url)

    def __init__(self):
        data = None

    @staticmethod
    def check_mealtime(current_time):
        mealtime = Mealtime.mealtime

        for dict in mealtime:
            dict['start_time'] = datetime.strptime(dict['start_time'], '%H:%M').time()
            dict['end_time'] = datetime.strptime(dict['end_time'], '%H:%M').time()

            if dict.get('name') == '아침':
                morning_start_time = dict['start_time']
                morning_end_time = dict['end_time']

            elif dict.get('name') == '점심':
                lunch_start_time = dict['start_time']
                lunch_end_time = dict['end_time']

            elif dict.get('name') == '저녁':
                dinner_start_time = dict['start_time']
                dinner_end_time = dict['end_time']

        if morning_start_time <= current_time <= morning_end_time:
            return "아침"
        elif lunch_start_time <= current_time <= lunch_end_time:
            return "점심"
        elif dinner_start_time <= current_time <= dinner_end_time:
            return "저녁"
        else:
            print('식사시간이 아닙니다.')
            quit()

    # 특정 시간대의 시간을 변경합니다. 변경하려는 시간은 HH:MM 형태로 입력해야 합니다.
    @staticmethod
    def change_mealtime(name, start_time, end_time):
        mealtime = Mealtime.mealtime
        file_utils = Mealtime.file_utils
        mealtime_url = Mealtime.mealtime_url

        for dict in mealtime:
            if dict['name'] == name:
                dict['start_time'] = start_time
                dict['end_time'] = end_time
                break

        file_utils.save_file(mealtime_url, mealtime)

