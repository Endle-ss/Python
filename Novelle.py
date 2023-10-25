import random
from random import choices 
act = 0 
attack = 0
loot = 0
brave = 0
mining = 0
strong = 0
stonks = 0
event = 0
infoPerson = 0
anomaly = 0
kromer = 0
def randommining(loot, mining = 0):
    loot = choices([1, 2, 3], [.8, .15, .05])
    if loot == [1]:  
        print("Вы получили обычные инструменты для добычи минералов.\nДобыча +2")
        mining = mining + 2
        return mining + 2
    if loot == [2]:
        print("Вы получили редкое снаряжение для добычи минералов.\nДобыча +5")
        mining = mining + 5
        return mining
    if loot == [3]:
        print("ВЫ ПОЛУЧИЛИ ЛЕГЕНДАРНОЕ СНАРЯЖЕНИЕ!\nУДАЧА СОПУТСТВУЕТ ВАМ!\nДобыча +20")
        mining = mining + 20
        return mining
def eventplanet(act, kromer, stats, event, loot, attack):
    event = choices([1, 2, 3], [.4, .4,  .2])
    if event == [1]:
        from shutil import get_terminal_size
        gameLine = get_terminal_size()[0]
        print('*'*gameLine)
        print("Вы наткнулись на монстров!")
        stats[2] = stats[2] + fightsystem(attack, act)
    if event == [2]:
        from shutil import get_terminal_size
        gameLine = get_terminal_size()[0]
        print('*'*gameLine)
        print("Вы наткнулись на ирмалит\nВы можете добыть его!\nДобыть?\n1)Да\n2)Нет")
        act = input()
        if act == "1":
            print("Вы добыли ирмалит! \nСила духа отряда повысилась на 1!")
            stats[2] = stats[2] + 1
        if act == "2":
            print("Вы решили не добывать ирмалит...")
            print("Странное решение...")
    if event == [3]:
        from shutil import get_terminal_size
        gameLine = get_terminal_size()[0]
        print('*'*gameLine)
        print("Ничего не произошло...")
# def treasure(loot, kromer, stonks):  Не получилось встроить функцию в код.
#     loot = choices([1,2,3,4], [.4,.3,.2,.1])
#     if loot == [1]:
#         stonks = 100 * planetcost
#         print("Вы получили немного кромеров.\nКромеры +", stonks)
#         kromer = kromer + stonks
#         return 100 * planetcost
#     if loot == [2]:
#         stonks = 250 * planetcost
#         print("Вы получили", stonks," кромеров")
#         kromer = kromer + stonks
#         return 250 * planetcost
#     if loot == [3]:
#         stonks = 500 * planetcost
#         print("Вы получили большое количество кромеров!\nКромеры +", stonks)
#         kromer = kromer + stonks
#         return 500 * planetcost
#     if  loot == [4]:
#         stonks = 1000 * planetcost
#         print("Вы получили очень много кромеров!!!!!\nКромеры +", stonks)
#         kromer = kromer + stonks
#         return 1000 * planetcost
def fightsystem(attack, act):
    attack = choices([1, 2, 3], weights=[.33, .34, .33])
    if attack == [1]:
        print("Монстр делает сильный удар сверху!\n1) Отпрыгнуть\n2) Заблокировать\n3) Контратаковать")
        act = input()
        if act == "1":
            print("Вы попытались отпрыгнуть, но монстр всё равно вас достал.\nВы проиграли сражение.\nСила духа -1")
            return -1
        if act == "2":
            print("Вы попытались заблокировать удар, однако он был слишком силён для вас!\nВы проиграли сражение.\nСила духа -1")
            return -1
        if act == "3":
            print("Из-за сильного замаха у монстра появилась брешь в защите и вы успешно контратаковали монстра!\nВЫ победили!\nСила духа отряда увеличилась на 3!")
            return 3
    if attack == [2]:
        print("Монстр бьёт по вашим ногам своим хвостом!\n1) Отпрыгнуть\n2) Заблокировать\n3) Контратаковать")
        act = input()
        if act == "1":
            print("Вы отпрыгнули и монстр не попал по вам, падая он ударился об камень и умер.\nВы победили!\nСила духа повысилась на 3!")
            return 3
        if act == "2":
            print("Вы попытались заблокировать удар, однако ноги блокировать вы не умеете!\nВы проиграли сражение.\nСила духа -1")
            return -1
        if act == "3":
            print("Вы попытались контратаковать, но удар по вам прошёл слишком быстро!\nВы проиграли сражение!\nСила духа -1")
            return -1
    if attack == [3]:
        print("Монстр бьёт по вам прямым ударом с руки!\n1) Отпрыгнуть\n2) Заблокировать\n3) Контратаковать")
        act = input()
        if act == "1":
            print("Вы отпрыгнули и монстр не попал по вам, однако он сразу нанёс ещё один удар к которому вы не были готовы!.\nВы проиграли сражение!.\nСила духа -1")
            return -1
        if act == "2":
            print("Вы заблокировали удар, монстру показалось будто он ударил гору, он испугался и убажел!!\nВы победили!\nСила духа повысилась на 3")
            return 3
        if act == "3":
            print("Вы попытались контратаковать, но удар по вам прошёл слишком быстро!\nВы проиграли сражение!\nСила духа -1")
            return -1
from shutil import get_terminal_size
gameLine = get_terminal_size()[0]
print('*'*gameLine)
while act != "Выход" or act != "выход" or kromer != 10000:
    print("Здравствуй, Добро пожаловать в мою новеллу!\nЧтобы начать введи имя, пол и возраст персонажа которого ты хочешь создать: ")
    infoPerson = input()
    infoList = []
    print(100*'\n')
    for person in infoPerson.split(" "):
        infoList.append(person)
    print("Управление осуществляется через ввод символов через консоль. Чтобы выйти введите \"Выйти\"")
    print("Вы - космический пират и капитан космического корабля.\nВы вместе со своей комндой добываете ресурсы на различных планетах солнечной системы используя особые предметы.\nОднако всё не так просто, на планетах обитают различные существа которые защищают свои сокровища и сокровища погибших пиратов, которые надеялись обогатиться.\n")
    print("Ваша задача добыть 10.000 кромеров(местной валюты) чтобы победить.")
    from shutil import get_terminal_size
    gameLine = get_terminal_size()[0]
    print('*'*gameLine)
    print ("\n\nВыберите свою команду: \n1) Молодежь: Уверенные в себе, перспективные молодые люди. Они новички в добыче ресурсов, однако быстро учатся, и при хорошем снаряжении будут неплохо справляться. Хорошо противостоят монстрам.\n2) Шахтёры: опытные добытчики ресурсов, однако при встрече с монстрами не смогут дать им достойный отпор без дорогого снаряжения.\n3) Солдаты: лучшие в борьбе против монстров однако абсолютно не готовы к добыче ресурсов.")
    act = input()
    if act == "Выход" or act == "выход":
        break
    print(100*'\n')
    from shutil import get_terminal_size
    gameLine = get_terminal_size()[0]
    print('*'*gameLine)
    kromer = 0
    if act == "1":
        print("!!Под символами \"*\" показываются ваши нынешние характеристики и нынешнее количество кромеров. Они появляются перед выбором планет!!\nВы выбрали молодёжь. Статистика вашей команды: \nСила: 10\nДобыча: 13\nСила духа: 7")#\\ Сила определяет какиех противников вы сможете победить. Добыча показывает какие ресурсы вы сожете добыть. Сила духа показывает боятся ли ваши союзники морально посетить ту, или иную планету, повышается при прохождениии той, или иной планеты.
        stats = [10, 13, 7]
    if act == "2":
        print("Вы выбрали шахтёров. Статистика вашей команды: \nСила: 5\nДобыча: 15\nСила духа: 10")
        stats = [5, 15, 10]
    if act == "3":
        print("Вы выбрали военных. Статистика вашей команды: \nСила: 15\nДобыча: 0\nСила духа: 15")
        stats = [15, 0, 15]
    skip = input()
    print(100*'\n')
    act = 0
    while kromer != 10000:
        if kromer != 10000:
            from shutil import get_terminal_size
            gameLine = get_terminal_size()[0]
            print('*'*gameLine)
            if kromer >= 10000:
                print(100*'\n')
                print("ПОЗДРАВЛЯЮ, ВЫ СОБРАЛИ 10000 КРОМЕРОВ. УРА!")
                print("Вы прошли игру!")
                break
            else:
                print(stats, kromer)
                print("Выберите планету куда хотите отправиться:\n1) Меркурий     (Требования к силе духа - 30, за прохождение планеты +1000 кромеров)\n2) Венера     (Требования к силе духа - 15 за прохождение планеты +500 кромеров)\n3) Марс     (Требования к силе духа - 5, за прохождение планеты +250 кромеров)")
                act = input()
                if act == "Выход" or act == "выход":
                    break
                print(100*'\n')
                from shutil import get_terminal_size
                gameLine = get_terminal_size()[0]
                print('*'*gameLine)
                if act == "1":
                    if stats[2] < 30:
                        print("Ваша команда морально не готова(\n\nПопробуйте исследовать другие планеты и повысить силу духа вашей команды.")
                    else:
                        print("Добро пожаловать на меркурий!")
                        place = choices([1, 2], weights=[.3, .7])
                        kromer = kromer + 1000
                        if place == [1]:
                            print("\n\nВы высаживаетесь на платформу вокруг которой лава и сразу видите недорогие минераллы.\nХотите ли вы собрать их или пройти дальше?\n1) Собрать\n2) Продолжить исследовать")
                            act = input()
                            if act == "Выход" or act == "выход":
                                break
                            if act == "1":
                                print("Вы собрали Ксалоремит на сумму 300 кроммеров. Сила духа вашего отряда повысилась на 1!")
                                stats[2] = stats[2] + 1
                                kromer = kromer + 300
                                eventplanet(act, kromer, stats, event, loot, attack)
                            else:
                                print("Вы решили продолжить исследования, и пролетев несколько метров видите пещеру в которой находятся монстры, охраняющие сокровища. Вы можете атаковать их, либо улететь что выберите:\n1) Атака\n2) Игнорировать")
                                act = input()
                                if act == "выход" or act == "Выход":
                                    break
                                if act == "1":
                                    fightsystem(attack, act)
                        else:
                            print("Вы высодились на пустой платформе, рядом с вами ничего нет.\nПродолжить исследование?\n1) Да\n2) Нет")
                            act = input()
                            if act =="1":
                                print("Вы решаете продолжить исследование.")
                                eventplanet(act, kromer, stats, event, loot, attack)
                if act == "2":
                    if stats[2] < 15:
                        print("Ваша команда морально не готова(\n\nПопробуйте исследовать другие планеты и повысить силу духа вашей команды.")
                    else:
                        print("Вы на Венере!")
                        kromer = kromer + 500
                        print("\n\nВы высаживаетесь на путой площади, рядом с вами ничего нет.\nВы продолжаете своё исследование")
                        eventplanet(act, kromer, stats, event, loot, attack)
                        eventplanet(act, kromer, stats, event, loot, attack)
                        eventplanet(act, kromer, stats, event, loot, attack)
                if act == "3":
                    if stats[2] < 5:
                        print("Ваша команда морально не готова(\n\nПопробуйте исследовать другие планеты и повысить силу духа вашей команды.")
                    else:
                        print("Вы прибыли на марс!")
                        kromer = kromer + 250
                        print("Вы высадились на поверхности марса, вас поражают здешние виды, однако надо двигаться дальше")
                        eventplanet(act, kromer, stats, event, loot, attack)
                        eventplanet(act, kromer, stats, event, loot, attack)
                        eventplanet(act, kromer, stats, event, loot, attack)
                        eventplanet(act, kromer, stats, event, loot, attack)
        else:
            print(100*'\n')
            print("ПОЗДРАВЛЯЮ, ВЫ СОБРАЛИ 10000 КРОМЕРОВ. УРА!")
            print("Вы прошли игру!")
            break
    else:
        print(100*'\n')
        print("ПОЗДРАВЛЯЮ, ВЫ СОБРАЛИ 10000 КРОМЕРОВ. УРА!")
        print("Вы прошли игру!")
        break
    break

