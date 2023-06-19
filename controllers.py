import datetime

from utils import SingletonMeta
from views import AuthView
from views import MainServiceView
from models import Account
from models import Restaurant
from models import Menu
from models import Mealtime
from exception import LoginIdNotFoundException


class AuthController(metaclass=SingletonMeta):
    auth_view = AuthView()

    def __init__(self):
        self.data = None

    # 로그인 페이지를 보여주는 메소드입니다. 결과값으로 로그인 페이지에서 입력받은 id를 반환합니다.
    def show_login_page(self):
        auth_view = self.auth_view
        login_id = auth_view.show_login_view()

        return login_id

    # 로그인을 진행하는 메소드입니다. id의 유효성을 검증하고 로그인을 진행합니다. 결과값으로 로그인 된 account 인스턴스를 반환합니다.
    def login(self, login_id):
        try:
            self._validate_login_id(login_id)
            account = Account.login(login_id)

            return account

        except LoginIdNotFoundException as e:
            print(e)
            print('아이디가 존재하지 않습니다.')

    # 로그인 시 아이디의 유효성을 검증하는 메소드입니다. 본 클래스 내부에서만 사용합니다.
    def _validate_login_id(self, login_id):
        try:
            if login_id is None or '':
                raise TypeError

        except TypeError as e:
            print(e)
            print('아이디가 입력되지 않았습니다.')


class MainServiceController(metaclass=SingletonMeta):
    main_service_view = MainServiceView()

    def __init__(self):
        self.data = None

    # 메인 서비스를 시작하는 메소드입니다. 관리자, 사용자 여부에 따라 다른 로직을 제공합니다.
    def start_service(self, account):
        role = account.get_role()

        if role == 0:
            self._start_restaurant_service()

        if role == 1:
            Mealtime.change_mealtime()

    # 식당 서비스를 시작하는 메소드입니다. 본 클래스 내부에서만 사용합니다.
    def _start_restaurant_service(self):
        restaurant_list = Restaurant.find_all_restaurant()
        main_service_view = MainServiceController.main_service_view

        input_restaurant_id = main_service_view.show_restaurant_view(restaurant_list)

        self._show_menus(input_restaurant_id)

    # 메뉴를 보여주고 선택 및 결제하는 메소드입니다. 본 클래스 내부에서만 사용합니다.
    def _show_menus(self, restaurant_id):
        main_service_view = MainServiceController.main_service_view
        current_time = datetime.datetime.now()
        time = Mealtime.check_mealtime(current_time)  # 아침, 점심, 저녁 중 해당되는 시간 할당

        menu_list = Menu.find_menus_of_restaurant(restaurant_id, time)

        main_service_view.show_menu_view(menu_list)

