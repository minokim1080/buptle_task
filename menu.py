import json


with open('./resource/menu_list.json', 'r', encoding='utf-8') as f:
    menu_list = json.load(f)


def show_menus(restaurant_id):
    result = []
    for menu in menu_list:
        result.append((menu['id'], menu['name'], menu['price']))

    return result


def choose_menu(menu_id, price):
    print(str(price) + "원이 결제되었습니다")
