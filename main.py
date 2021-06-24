import random
from data import Player
from data import Map
import pygame
from pygame.locals import *
import time

pygame.init()

# Create Map
mapInfo = [
    ["起點", 0, 950, 970], ["台灣", 800, 820, 900],
    ["日本", 2000, 758, 860], ["南韓", 1600, 682, 813],
    ["北韓", 200, 615, 760], ["肯亞", 600, 543, 715],
    ["剛果", 400, 472, 670], ["南非", 1000, 404, 630],
    ["無人島", 0, 268, 514], ["俄羅斯", 1200, 400, 436],
    ["蒙古", 600, 473, 389], ["中國", 1800, 547, 345],
    ["越南", 600, 631, 298], ["阿根廷", 1000, 687, 252],
    ["巴西", 1200, 763, 210], ["智利", 800, 824, 162],
    ["機會", 0, 948, 81], ["菲律賓", 600, 1078, 160],
    ["馬來西亞", 700, 1148, 205], ["新加坡", 1800, 1223, 256],
    ["泰國", 700, 1295, 302], ["英國", 2000, 1364, 346],
    ["法國", 1800, 1436, 393], ["德國", 1800, 1501, 440],
    ["飛機場", 0, 1630, 518], ["緬甸", 600, 1507, 620],
    ["印度", 1200, 1432, 670], ["印尼", 700, 1366, 720],
    ["澳大利亞", 1300, 1290, 760], ["墨西哥", 800, 1219, 810],
    ["加拿大", 1600, 1142, 850], ["美國", 2200, 1080, 900]
]
house_position = [
    [950, 970], [900, 840], [831, 787], [756, 742],
    [686, 693], [617, 650], [548, 605], [480, 561],
    [268, 514], [478, 492], [552, 443], [626, 394],
    [698, 350], [765, 305], [837, 255], [910, 210],
    [948, 81], [1020, 218], [1084, 264], [1153, 307],
    [1228, 356], [1306, 403], [1373, 445], [1445, 492],
    [1630, 518], [1436, 560], [1367, 603], [1297, 652],
    [1229, 699], [1162, 741], [1094, 787], [1022, 834]
]

mapName = []
for i in mapInfo:
    mapName.append(i[0])

map1 = []
for i in mapInfo:
    map1.append(Map(i[0], i[1], i[2], i[3]))

# Crate screen
screen = pygame.display.set_mode((1920, 1080))

# Background
background = pygame.image.load("background1.png")

# Title and Icon
pygame.display.set_caption("大富翁")
# icon = pygame.image.load('dragonman.png')
# pygame.display.set_icon(icon)

# Player
player = []
playerNum = [0, 1, 2, 3]
player.append(Player(pygame.image.load('pink_player.png'), 0))
player.append(Player(pygame.image.load('blue_player .png'), 1))
player.append(Player(pygame.image.load('lightblue_player.png'), 2))
player.append(Player(pygame.image.load('red_player.png'), 3))
player_info_position = [(0, 0), (1500, 0), (0, 950), (1500, 950)]

# DiceNum
font = pygame.font.Font('freesansbold.ttf', 32)
money_font = pygame.font.Font('freesansbold.ttf', 24)
dice_x = 900
dice_y = 300
diceNum = 0

# house
pink_house1 = pygame.image.load("pink_house1.png")
pink_house2 = pygame.image.load("pink_house2.png")
pink_house3 = pygame.image.load("pink_house3.png")
pink_house = [pink_house1, pink_house2, pink_house3]

blue_house1 = pygame.image.load("blue_house1.png")
blue_house2 = pygame.image.load("blue_house2.png")
blue_house3 = pygame.image.load("blue_house3.png")
blue_house = [blue_house1, blue_house2, blue_house3]


lightblue_house1 = pygame.image.load("lightblue_house1.png")
lightblue_house2 = pygame.image.load("lightblue_house2.png")
lightblue_house3 = pygame.image.load("lightblue_house3.png")
lightblue_house = [lightblue_house1, lightblue_house2, lightblue_house3]


red_house1 = pygame.image.load("red_house1.png")
red_house2 = pygame.image.load("red_house2.png")
red_house3 = pygame.image.load("red_house3.png")
red_house = [red_house1, red_house2, red_house3]


# button
clicked = False
question0 = font.render("Do you want to buy the house? ", True, (0, 0, 0))
question1 = font.render("Do you want to buy his house? ", True, (0, 0, 0))
question_ticket = font.render("You got a ticket!!", True, (0, 0, 0))
question_lottery = font.render("You won a lottery!!", True, (0, 0, 0))
question_airport = font.render(
    "You're in the airport,click your destination on the map!!", True, (0, 0, 0))
question_island = font.render("You went into the island!!", True, (0, 0, 0))


class Button:
    # colours for button and text
    button_col = (0, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (255, 0, 255)
    width = 90
    height = 70
    font = pygame.font.Font('freesansbold.ttf', 32)

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    @property
    def draw_button(self):

        global clicked
        global font
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                # print('0')
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) -
                    int(text_len / 2), self.y + 25))
        return action


# Button
button_rect1 = Button(800, 650, "Yes")
button_rect2 = Button(1070, 650, "No")


def screen_refresh():
    screen.blit(background, (0, 0))

    for l in range(len(map1)):
        i = map1[l].level
        if map1[l].who == 0:
            screen.blit(pink_house[i - 1],
                        (house_position[l][0], house_position[l][1]))
        elif map1[l].who == 1:
            screen.blit(blue_house[i - 1],
                        (house_position[l][0], house_position[l][1]))
        elif map1[l].who == 2:
            screen.blit(
                lightblue_house[i - 1], (house_position[l][0], house_position[l][1]))
        elif map1[l].who == 3:
            screen.blit(red_house[i - 1],
                        (house_position[l][0], house_position[l][1]))

    for j in range(len(player)):  # player move display
        screen.blit(player[j].img, (player[j].x, player[j].y))

    for i in range(len(player)):
        show_player_info(player[i], player_info_position[i])

    for i in map1:
        if i.name in "起點無人島機會飛機場":
            continue
        price = money_font.render(str(i.price), True, (0, 0, 0))
        screen.blit(price, (i.x, i.y))


def show_player_info(player, position):
    screen.blit(player.img, (position[0], position[1]))
    money_show = font.render("Money :" + str(player.bank), True, (0, 0, 0))
    status_show = font.render(
        "Status : " + " ".join(list(map(str, player.status))), True, (0, 0, 0))
    screen.blit(money_show, (position[0], position[1] + 50))
    screen.blit(status_show, (position[0], position[1] + 100))


def show_dice(x, y):
    dice_show = font.render("DiceNum :" + str(diceNum), True, (0, 0, 0))
    screen.blit(dice_show, (x, y))


def move(mapInfo, player_current, nowplaying):
    global diceNum
    diceNum = random.randint(1, 6)
    show_dice(dice_x, dice_y)
    if player_current.position + diceNum >= 32:
        for l in range(diceNum):
            if player_current.position + 1 >= 32:
                player_current.position = 0
                # 經過、到起點給錢+換位置
                player_current.give_money(1000)
            else:
                player_current.position += 1
            player_current.x = mapInfo[player_current.position][-2]
            player_current.y = mapInfo[player_current.position][-1]

            screen_refresh()
            show_dice(dice_x, dice_y)

            pygame.display.update()
            time.sleep(0.2)
    else:
        for l in range(diceNum):
            player_current.position += 1
            player_current.x = mapInfo[player_current.position][-2]
            player_current.y = mapInfo[player_current.position][-1]

            screen_refresh()
            show_dice(dice_x, dice_y)

            pygame.display.update()
            time.sleep(0.2)


def button_show():
    run = True
    while run:
        if button_rect1.draw_button:
            return True
        if button_rect2.draw_button:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


def button_show1():
    run = True
    while run:
        if button_rect1.draw_button:
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


def airport_show(button_rect):
    run = True
    while run:
        for i in button_rect:
            if i.draw_button:
                run = False
                return button_rect.index(i)
        screen_refresh()
        screen.blit(question_airport, (550, 525))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


def airport():
    button_rect = []
    for i in map1:
        button_rect.append(Button(i.x, i.y, "x"))
    destination = airport_show(button_rect)
    player_current.position = destination
    player_current.x, player_current.y = map1[destination].x, map1[destination].y
    screen_refresh()
    pygame.display.update()


position = 0
# Game loop
running = True
nowPlaying = -1
existPlaying = 4
while running:

    # R G B
    screen.fill((255, 255, 255))
    # Background Image
    screen_refresh()

    # 破產刪人
    if player[nowPlaying].bank < 0:
        existPlaying -= 1
        for i in range(len(mapInfo)):
            if map1[i].who == player[nowPlaying].num:
                map1[i] = Map(mapInfo[i][0], mapInfo[i][1],
                              mapInfo[i][2], mapInfo[i][3])
        del player[nowPlaying]
        del playerNum[nowPlaying]
        nowPlaying -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if existPlaying == 1:
            pass
            print(str(player[0].num) + "贏了!")
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 下面一位
                nowPlaying += 1
                # nowPlaying數字循環
                if nowPlaying == existPlaying:
                    nowPlaying -= existPlaying

                player_current = player[nowPlaying]

                # 判斷是否在無人島
                if player_current.isisland():
                    continue

                # 移動
                move(mapInfo, player_current, nowPlaying)

                map_current = map1[player_current.position]

                if map_current.name == "飛機場":
                    airport()
                    map_current = map1[player_current.position]
                    if player_current.position == 24:
                        continue

                if map_current.name == "機會":
                    fate = random.randint(1, 4)
                    if fate == 1:
                        screen.blit(question_ticket, (840, 500))
                        if button_show1():
                            ticket = random.randint(10, 20)
                            player_current.pay_money(ticket * 100)
                            continue

                    elif fate == 2:
                        screen.blit(question_lottery, (840, 500))
                        if button_show1():
                            ticket = random.randint(15, 30)
                            player_current.give_money(ticket * 100)
                            continue

                    elif fate == 3:
                        player_current.position = mapInfo.index(
                            ["無人島", 0, 268, 514])
                        player_current.x, player_current.y = 268, 514
                        screen.blit(question_island, (840, 500))
                        if button_show1():
                            player_current.island()
                            screen_refresh()
                        continue

                    else:
                        airport()
                        map_current = map1[player_current.position]
                        if player_current.position == 24 or player_current.position == 16:
                            continue

                if map_current.name == "無人島":
                    player_current.island()
                    continue  # 換下一位

                if map_current.name in "起點":
                    continue

                # 踩到空地
                if map_current.who == -1:
                    screen.blit(question0, (750, 500))
                    if button_show():
                        if map_current.empty(player_current):
                            map_current.buy(
                                player_current)

                # 踩到自己的地
                elif map_current.who == player_current.num:
                    screen.blit(question0, (750, 500))
                    if button_show():
                        if player_current.bank >= map_current.price:  # 返回True時
                            map_current.buy(
                                player_current)  # 加蓋(買地)

                # 踩到別人買的地
                else:
                    # 給過路費
                    map_current.having(player, nowPlaying, playerNum)

                    if player_current.bank >= map_current.price:  # 玩家錢夠返回True
                        screen.blit(question1, (750, 500))
                        if button_show():
                            Player.give_money(player[playerNum.index(
                                map_current.who)], map_current.tolls,)
                            map_current.buy(
                                player_current)
    screen_refresh()
    show_dice(dice_x, dice_y)
    pygame.display.update()
