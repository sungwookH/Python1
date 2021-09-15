# 예외처리 (try: → 오류가 발생할 수 있는 구문) =============

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))         # ValueError: invalid literal for int() with base 10: '삼'
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했습니다.")
    print(err)

try:
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
except Exception as err:                                       # Exception 모든 에러를 뜻함
    print(err)
else:
    print(num1 + num2)                                     # 에러가 아니면 하위 구문 실행


# 에러 발생시키기
try:
    print("한 자리 수 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    elif num2 == 0:
        raise ZeroDivisionError
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError:
    print("올바른 숫자를 입력해주세요")


# 사용자 정의 에러

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "[에러코드001]" + self.msg

try:
    print("한 자리 수 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력 값 : {}, {}".format(num1, num2))
    elif num2 == 0:
        raise ZeroDivisionError
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except BigNumberError as err:
    print("한 자리 수만 입력하세요.")
    print(err)
finally:                                                  # finally - 실행 오류 여부에 관계없이 finally 내부 구문 실행
    print("계산기를 이용해 주셔서 감사합니다.")

# 퀴즈 9

# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#     출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#     치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#     출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):
    pass

chicken = 10
waiting_no = 1
while chicken >= 0:
    try:
        print("주문가능한 치킨 : {}".format(chicken))
        order = int(input("주문하실 치킨 수량을 입력해주세요 : "))
        if 0 < order <= chicken:
            print("대기번호 : [{}]\t 주문해주셔서 감사합니다.".format(waiting_no))
            chicken -= order
            waiting_no += 1
        elif order > chicken:
            print("주문가능한 치킨을 초과했습니다. 다시 주문해주세요")
        elif order <= 0:
            raise ValueError
        if chicken == 0:
            raise SoldOutError
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    except ValueError:
        print("잘못된 값을 입력하였습니다.")