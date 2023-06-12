import json
from exception import LoginException

with open('./resource/account_list.json', 'r', encoding='utf-8') as f:
    account_list = json.load(f)


# 로그인
def login(input_login_id: str):

    for account in account_list:
        if account['login_id'] == input_login_id:
            return input_login_id

    raise LoginException  # 아이디가 없을 경우 예외를 던집니다. Django 에서 핸들러로 처리할 것을 가정하고, 여기선 try-except 문을 사용하지 않습니다.
