class Player:
    def __init__(self, img, num):
        self.num = num
        self.bank = 10000.0
        self.position = 0  # 玩家位置
        # 狀態 [0] = "free" or "freeze" [1] = 0 or 1 or 2
        self.status = ["free", 0]
        self.x = 950
        self.y = 970
        self.img = img

    def isisland(self):
        if self.status[0] == "freeze":
            self.status[1] -= 1
            if self.status[1] == 0:
                self.status[0] = "free"
            return True

    def island(self):
        self.status = ["freeze", 2]

    # 給錢
    def give_money(self, money):
        self.bank += money

    # 付錢
    def pay_money(self, money):
        self.bank -= money


class Map:
    def __init__(self, name, price, x, y):
        self.name = name
        self.price = price  # 購買價格
        self.who = -1  # 誰的地
        self.level = 0  # 幾棟房子 0, 1, 2, 3 棟
        self.tolls = 0  # 過路費
        self.x = x
        self.y = y

        # 買地
    def buy(self, player):
        Player.pay_money(player, self.price)  # 付錢
        if self.level < 3:  # 蓋房子(收購自動加蓋)
            self.level += 1
        self.price += 500 * self.level  # 價格上升
        self.who = player.num  # 更改地權
        self.tolls = self.price + 500  # 過路費()

    # 踩到空地
    def empty(self, player):
        if player.bank >= self.price:  # 玩家錢夠返回True
            return True
        else:  # 玩家錢'不'夠返回False
            return False

    # 踩到別人買的地
    def having(self, player, nowPlaying, playerNum):
        Player.pay_money(
            player[nowPlaying], self.tolls)
        Player.give_money(
            player[playerNum.index(self.who)], self.tolls)
