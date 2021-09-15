def price(person):
    print("{}명 가격은 {}원입니다.".format(person, person*10000))

def morning_price(person):
    print("{}명 조조할인 가격은 {}원입니다.".format(person, person*6000))

def army_price(person):
    print("{}명 군인 가격은 {}원입니다.".format(person, person*5000))

if __name__ == "__main__":
    army_price(5)