import json


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# 파일 읽기, 쓰기, 저장과 관련된 메소드를 제공하는 클래스입니다.
class FileUtils(metaclass=SingletonMeta):

    def __init__(self):
        self.data = None

    # 필드로 받아온 파일을 열어 리스트로 반환합니다.
    def open_file_as_list(self, url):
        result = []

        try:
            with open(url, 'r', encoding='utf-8') as f:
                result = json.load(f)

                return result

        except FileNotFoundError as e:
            print(e)
            print('파일이 존재하지 않거나 경로가 올바르지 않습니다.')

        except IOError as e:
            print(e)
            print('파일이 손상되었거나, 파일에 대한 접근 권한이 없습니다.')

        except TypeError as e:
            print(e)
            print('결과값이 리스트가 아닙니다. 현재 결과 타입은 ' + type(json.load(f)) + ' 입니다.')

        except Exception as e:
            print(e)
