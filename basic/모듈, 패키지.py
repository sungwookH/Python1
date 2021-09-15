# 모듈 (미리 만들어 놓은 .py파일) =================================================================

import theater_module                   # theater_module 에 정의되어 있는 함수 사용
theater_module.price(3)
theater_module.morning_price(4)
theater_module.army_price(3)

import theater_module as mv             # 모듈 theater_module를 mv 로 축약해서 사용
mv.price(3)
mv.morning_price(4)
mv.army_price(3)

from theater_module import *            # from 모듈 import *  -  모듈 입력 필요없이 해당 모듈의 함수 즉시 사용
price(3)
morning_price(4)
army_price(3)

from theater_module import price, morning_price      # from 모듈 import any   -  모듈의 함수 중 일부만 불러옴
price(2)
morning_price(3)
# army_price(5) is not defined

from theater_module import army_price as apri        # from 모듈 import any as any  -  모듈의 함수 중 일부만 불러와서 축약사용
apri(2)

### import 모듈 or from 모듈 import 를 사용할 때, 모듈 파일에 있는 실행 문장이 자동 실행, 출력됨 따라서, 모듈 파일에 함수가 아닌
# 자동 실행 문장 중 출력을 원치 않는 부분은 if __name__ == "__main__": 처리해야함
# 다시 말해 위 메소드를 적어 놓은 모듈에서 위 메소드 이후 내용은 해당 모듈을 직접 실행시에만 출력

# 가져오려는 모듈 파일이 현재 실행하려는 파일과 다른 폴더 에 있는 경우
# import sys
# sys.path.append("가져오려는 모듈 파일이 있는 폴더 경로") 로 경로를 추가해야함
import sys
sys.path.append("c:\\Users\\sunguk\\Desktop\\python workspace\\travel")
import USA
trip = USA.UsaPackage()
trip.detail()

# 패키지 (모듈을 여러개 모아놓은 것)====================================================== 패키지 = 폴더
# 패키지 폴더 travel 에서 파일 __init__ 은 패키지 관련 설정하는 곳
import travel.USA                       # import 폴더.모듈    # import 폴더.모듈.클래스 는 불가능 
trip = travel.USA.UsaPackage()
trip.detail()

from travel.French import FrenchPackage  # from 폴더.모듈 import 클래스 / 클래스 가져오기
trip2 = FrenchPackage()
trip2.detail()

from travel.French import paris          # from 폴더.모듈 import 함수 / 함수 가져오기
paris()

from travel import French                # from 폴더 import 모듈 / 모듈 가져오기
trip3 = French.FrenchPackage()
trip3.detail()

# __all__  :  폴더에 모든 걸 가져오기 / 폴더의 파일(모듈) - __init__.py에서
# 내보낼 것 정하기 : __all__ = ["French", "USA"] ==================================
from travel import *
trip_all = French.FrenchPackage()
trip_all.detail()

# 패키지, 모듈 위치 ======================================================

from travel import French
import inspect
print(inspect.getfile(French))
print(inspect.getfile(inspect))


# pip install ======================================================

# Pypi 에서 패키지 다운로드
# 버전 업데이트 : pip install --upgrade 패키지이름
# 패키지 삭제 : pip uninstall 패키지 이름