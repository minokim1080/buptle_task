import account
import restaurant
import menu


def main():

    # 첫 화면 및 아이디 입력
    print('---------식권 대장--------\n')
    input_login_id = input('아이디를 입력해주세요. : ')
    account.login(input_login_id)

    # 식당 목록 보여주기
    restaurant_name_list = restaurant.show_restaurant_list()
    print(restaurant_name_list)

    # 식당 선택
    input_restaurant_id = input('식당을 선택해주세요. : ')
    restaurant_id = restaurant.choose_restaurant(input_restaurant_id)

    # 메뉴 보여주기
    selected_menu_list = menu.show_menus(restaurant_id)
    print(selected_menu_list)

    # 메뉴 선택 및 결제
    input_menu_id = input('메뉴를 선택해주세요. : ')
    menu.choose_menu(input_menu_id)


if __name__ == '__main__':
    main()

