class FrenchPackage:
    def detail(self):
        print("프랑스 감성 여행 패키지 [현금 특가 100만원]")

def paris():
    print("파리로 떠나요")

if __name__ == "__main__":
    print("French 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할때만 실행되요")
    trip_ = FrenchPackage()
    trip_.detail()
else:
    print("French 외부에서 모듈 호출")