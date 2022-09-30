import os

name = input("Как зовут персонажа? ")
if not name: name = "Илья Муромец"

way_1 = True
way_2 = True
way_3 = True
game = True
user_hp = 100
key = ""


while game:

    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")        
        print(f"Подъезжает {name} к четырём дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть»")
        if way_1:
            print("убитому быть.1")
        if way_2:
            print("женатым быть.2")
        if way_3:
            print("богатым быть.3")

        user_choice = input("какой вариант? ")     
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            key += user_choice
        

    if key == "1" and way_1:
       os.system("cls")
       print("Ехал он по этой дороге, и вдруг напало на него сорок тысяч разбойников.")
       print("1 вариант")
       print("2 вариант")
       user_choice = input("Что выберишь?")
       if user_choice == "1" or user_choice == "2":
            key += user_choice
       

    if key == "11" and way_1:
       os.system("cls")
       print("Дорога 1 - умер")
       way_1 = False
       key = ""
       input("ENTER - дальше")

    if key == "12" and way_1:
        os.system("cls")
        print("Дорога 1 - выжил")
        game = False

    if key == "2":
        os.system("cls")
        print("Отправился Илья по той дороге, которая обещала ему женитьбу.")
        print("1 вариант")
        print("2 вариант")
        user_choice = input("Что выберишь?")
        if user_choice == "1" or user_choice == "2":
        
            key += user_choice
        
    if key == "21" and way_2:
        os.system("cls")
        print("Дорога 2 - женился")
        way_2 = False
        key = ""
        input("ENTER - дальше")

    if key == "22" and way_2:
        os.system("cls")
        print("Дорога 2 - получил леща от бывшой")
        game = False

    if key == "3":
        os.system("cls")
        print("Поехал Илья по третьей дороге и скоро увидал глубокие погреба, полные несметных богатств: золота и драгоценных каменьев.")
        print("1 вариант")
        print("2 вариант")

        user_choice = input("Что выберишь?")
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            key += user_choice

    if key == "31" and way_3:
        os.system("cls")
        print("Дорога 3 - съел цербер")
        way_3 = False
        key = ""
        input("ENTER - дальше")

    if key == "32" and way_3:
        os.system("cls")
        print("Дорога 3 - победил цербера и забрал все золото")
        game = False

    if way_1 == way_2 == way_3 == False:
        
        os.system("cls")
        print("Все дороги пройдены!")
        print("ВЫ : выжили,женились и обогатели")