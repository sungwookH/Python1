class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))
   
    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit. __init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):
    seize_mode_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 100, 15, 10)
        self.seize_mode = False
    

    def set_seize_mode(self):
        if Tank.seize_mode_developed == False:
            return

        if self.seize_mode == False:
            print("[알림] {} : 시즈모드로 변경완료.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("[알림] {} : 시즈모드 해제완료.".format(self.name))
            self.damage /=2
            self.seize_mode = False




class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)                
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 90, 15, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print("[알림] {} : 클로킹 모드 적용완료.".format(self.name))
            self.clocked = True
        else:
            self.clocked = False


def game_start():
    print("게임이 시작됩니다.")

def gama_over():
    print("gg 게임이 종료되었습니다.")


# 게임시작
game_start()
# 마린 3기 생성
M1 = Marine()
M2 = Marine()
M3 = Marine()
# 탱크 2기 생성
T1 = Tank()
T2 = Tank()
# 레이스 1기 생성
w1 = wraith()
# 유닛 일괄 관리
units = []
units.append(M1)
units.append(M2)
units.append(M3)
units.append(T1)
units.append(T2)
units.append(w1)
# 전군 이동
for unit in units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_mode_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
# 공격 모드 준비(마린 : 스팀팩, 탱크 - 시즈모드, 레이스 - 클로킹)
for unit in units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()

# 전군 공격
for unit in units:
    unit.attack("11시")

# 전군 피해

from random import *

for unit in units:
    unit.damaged(randint(1,45))

gama_over()