from controllers import AuthController
from controllers import MainServiceController

# 필요한 Controller 인스턴스 생성
auth_controller = AuthController()
main_service_controller = MainServiceController()

# 유저 시나리오
login_id = auth_controller.show_login_page()

account = auth_controller.login(login_id)

print(account)
print(type(account))

main_service_controller.start_service(account)