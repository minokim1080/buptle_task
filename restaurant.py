import json

from typing import List


with open('./resource/restaurant_list.json', 'r', encoding='utf-8') as f:
    restaurant_list = json.load(f)


def show_restaurant_list():
    restaurant_name_list = []
    for restaurant in restaurant_list:
        restaurant_name_list.append({restaurant['id']: restaurant['name']})

    return restaurant_name_list


def choose_restaurant(input_restaurant_id):
    for restaurant in restaurant_list:
        if restaurant['id'] == input_restaurant_id:
            return input_restaurant_id

    raise FileNotFoundError  # 입력 받은 값에 식당이 없을 경우 예외를 던집니다. Django 에서 핸들러로 처리할 것을 가정하고, 여기선 try-except 문을 사용하지 않습니다.
