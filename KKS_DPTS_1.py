DPTS_1 = {
    "10NDF54CF001": ["F исх/в на ОВ ДПТС ,т/ч", True, True],  # 9
    "10NDF54CP001": ["P исх/в на ОВ ДПТС ,МПа",True,True],  # 8
    "10NDF54CT001": ["T исх/в на ОВ ДПТС ,°С",True,True],  # 7

    "10NDF64CF001": ["F исх/в на ДПТС ,т/ч",True,True],  # 5
    "10NDF64CP001": ["P исх/в после ПИВ ,МПа",True,True],  # 4
    "10NDF64CT001": ["T исх/в на ДПТС ,°С",True,True],  # 6

    "10NDJ21CF001": ["F на подаче воды от дренажного бака в ДПТС ,т/ч",True,True],  # 12
    "10NDJ21CP001": ["P на подаче воды от дренажного бака в ДПТС ,МПа",True,True],  # 10
    "10NDJ21CT001": ["T на подаче воды от дренажного бака в ДПТС ,°С",True,True],  # 11

    "F1CALCULATEDDPTS1": ["F на подводе исх/в к колонкам ДПТС №1 ,т/ч",True,False],  # рассчётное
    "10NDF91CP001_00CJK01_00CJL01": ["P в паровом простанстве ДПТС №1 дубл. от шк. 00CJK01 ,кПа",True,False],  # 19
    "10NDF70CT001": ["T на подводе исх/в к колонкам ДПТС №1 ,°С",True,False],  # 17

    "10NDA20CF001": ["F горячей сет/в на ДПТС ,т/ч",True,True],  # 13
    "10NDA20CP001": ["P горячей сет/в на деаэратор ,МПа",True,True],  # 14
    "10NDA20CT001": ["T  сет/в в горячем коллекторе ,°С",True,True],  # 25

    "10NDF91CL001": ["L в баке ДПТС №1 (№1) ,мм",True,False],  # 21
    "10NDF91CL002": ["L в баке ДПТС №1 (№2) ,мм",True,False],  # 22
    "10NDF91CL003": ["L в баке ДПТС №1 (№3) ,мм",True,False],  # 23
    "10NDF91CL901": ["Сред L ДПТС №1 ,мм",True,False],  # 24

    "F2CALCULATEDDPTS1": ["F на сливе подп/в с ДПТС №1 ,т/ч",True,False],  # рассчётное
    "10NDK11CP001": ["P подп/в перед НПТС №1 ,кПа",True,False],  # 1
    "10NDK12CP001": ["P подп/в перед НПТС №2 ,кПа",True,False],  # 2
    "10NDK13CP001": ["P подп/в перед НПТС №3 ,кПа",True,False],  # 3
    "10NDF91CT001": ["T на сливе подп/в с ДПТС №1 ,°С",True,False],  # 18

    "10QUN24CQ001": ["pH воды после ДПТС №1 ,ед.Ph",True,False],  # 20
    "10QUN24CQ002": ["O2 на сливе подп/в с ДПТС №1 ,?",True,False],  # 26 # ед измерения ?

    "10NDF70CG801": ["РК уровня в ДПТС №1 - Положение",True,True],  # 18
    "10NDA21CG801": ["РК P в ДПТС №1 - Положение",True,True],  # 18
}

class KKS_DPTS_1:
    def __init__(self, name: str, measured: bool, inside: bool, current: float):
        self.name = name          # описание
        self.measured = measured  # True = измеряемый, False = расчётный
        self.inside = inside      # True = вход, False = выход
        self.current = current    # текущее значение

    def __repr__(self):
        return f"Tag(name='{self.name}', measured={self.measured}, inside={self.inside}, current={self.current})"

# Создаём контейнер для всех тегов
tags_objects = {}

# Проходим по словарю DPTS_1
for code, (name, measured, inside) in DPTS_1.items():
    tags_objects[code] = KKS_DPTS_1(name=name, measured=measured, inside=inside, current=0.0)

# Проверка
print(tags_objects)

#################################################

