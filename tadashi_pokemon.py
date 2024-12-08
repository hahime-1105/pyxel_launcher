import pyxel
from enum import Enum, auto


# ポケモンのタイプ
class Ele(Enum):
    Normal = 'ノーマル'
    Fire = 'ほのお'
    Water = 'みず'
    Grass = 'くさ'
    Electric = 'でんき'
    Ice = 'こおり'
    Fighting = 'かくとう'
    Poison = 'どく'
    Ground = 'じめん'
    Flying = 'ひこう'
    Psychic = 'エスパー'
    Bug = 'むし'
    Rock = 'いわ'
    Ghost = 'ゴースト'
    Dragon = 'ドラゴン'
    Dark = 'あく'
    Steel = 'はがね'
    Fairy = 'フェアリー'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.name


# ワザの分類
class Cat(Enum):
    physical = 'ぶつり'
    special = 'とくしゅ'
    status = 'へんか'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.name


# 追加効果
class Effect:
    def none(self):
        pass


# タイプ相性
def comp(atk_ele, dff_ele):
    return 1


# ターン処理
class Turn:
    def __init__(self, my_poke, op_poke):
        self.my_poke = my_poke
        self.op_poke = op_poke

    def senkou(self):
        # 先攻の判断
        if self.my_poke.s > self.op_poke.s:
            pri = True
        if self.my_poke.s < self.op_poke.s:
            pri = False
        if self.my_poke.s == self.op_poke.s:
            tmp = pyxel.rndi(1, 2)
            if tmp == 1:
                pri = True
            else:
                pri = False
        return pri

    def up_attack(self, my_flag, cmd):
        if my_flag:
            atk_poke = self.my_poke
            dff_poke = self.op_poke
        else:
            atk_poke = self.my_poke
            dff_poke = self.op_poke
        tmp1 = int((atk_poke.lv * 2 / 5) + 2)
        if cmd[2] == Cat.physical:
            tmp2 = atk_poke.a * cmd[3]
            tmp3 = int(tmp1 * tmp2 / dff_poke.b)
        if cmd[2] == Cat.special:
            tmp2 = atk_poke.c * cmd[3]
            tmp3 = int(tmp1 * tmp2 / dff_poke.d)
        tmp4 = int((tmp3 / 50) + 2)
        tmp5 = 1.0 * pyxel.rndi(85, 100) / 100
        damage = int(tmp4 * tmp5)
        return damage

    def dw_attack(self, my_flag, cmd, font):
        if my_flag:
            atk_poke = self.my_poke
        else:
            atk_poke = self.op_poke
        pyxel.text(10, 102, f'{atk_poke.name} の {cmd[0]} !', 0, font)


# ワザ[技名、タイプ、分類、威力、命中、PP、効果]
class Cmd:
    eff = Effect()
    Fusion_Flare = ['クロスフレイム', Ele.Fire, Cat.special, 100, 100, 5, eff.none()]
    Fusion_Bolt = ['クロスサンダー', Ele.Electric, Cat.physical, 100, 100, 5, eff.none()]
    Dragon_Breath = ['りゅうのいぶき', Ele.Dragon, Cat.special, 60, 100, 20, eff.none()]
    Dragon_Claw = ['ドラゴンクロー', Ele.Dragon, Cat.physical, 80, 100, 15, eff.none()]
    Hyper_Beam = ['はかいこうせん', Ele.Normal, Cat.special, 150, 90, 5, eff.none()]
    Giga_Impact = ['ギガインパクト', Ele.Normal, Cat.physical, 150, 90, 5, eff.none()]
    Zen_Headbutt = ['しねんのずつき', Ele.Psychic, Cat.physical, 80, 90, 15, eff.none()]
    Extrasensory = ['じんつうりき', Ele.Psychic, Cat.special, 80, 100, 30, eff.none()]


# ポケモン
class Pokemon:
    # ワザとステータス、graはイメージバンクの位置、myは自分だったらTrue, 相手だったらFalse
    def __init__(self, name, h, a, b, c, d, s, cmd1, cmd2, cmd3, cmd4, tp1, tp2, lv, gra, my):
        self.name = name
        self.h_max = h
        self.h = h
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.s = s
        self.cmd = []
        self.cmd.append(cmd1)
        self.cmd.append(cmd2)
        self.cmd.append(cmd3)
        self.cmd.append(cmd4)
        self.pp_now = []
        self.pp_now.append(cmd1[5])
        self.pp_now.append(cmd2[5])
        self.pp_now.append(cmd3[5])
        self.pp_now.append(cmd4[5])
        self.tp = []
        self.tp.append(tp1)
        self.tp.append(tp2)
        self.lv = lv
        self.gra = gra
        self.my = my
        if my:
            self.poke_x = 15
            self.poke_y = 45
            self.name_x = 60
            self.name_y = 50
            self.hp_digit = True
        else:
            self.poke_x = 100
            self.poke_y = 5
            self.name_x = 30
            self.name_y = 10
            self.hp_digit = False

    def command(self):
        return self.cmd

    def pp(self):
        return self.pp_now

    # ポケモンの描画
    def poke_draw(self, font):
        pyxel.blt(self.poke_x, self.poke_y, 0, self.gra[0], self.gra[1], 32, 32)
        pyxel.text(self.name_x, self.name_y, self.name, 0, font)
        pyxel.text(self.name_x + 40, self.name_y, ('Lv.' + str(self.lv)), 0, font)
        pyxel.text(self.name_x, self.name_y + 8, 'HP', 0, font)
        pyxel.rect(self.name_x + 10, self.name_y + 8, 50, 5, 0)
        pyxel.rect(self.name_x + 10, self.name_y + 8, (50 * self.h / self.h_max), 5, 10)
        if self.hp_digit:
            pyxel.text(self.name_x + 15, self.name_y + 15, str(self.h), 0, font)
            pyxel.text(self.name_x + 30, self.name_y + 15, '/', 0, font)
            pyxel.text(self.name_x + 35, self.name_y + 15, str(self.h_max), 0, font)


class Trainer:
    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.member = []
        self.member.append(p1)
        self.member.append(p2)
        self.member.append(p3)
        self.member.append(p4)
        self.member.append(p5)
        self.member.append(p6)
        self.fainting = [True, True, True, True, True, True]
        self.field_poke = 0

    def cpu_cmd(self):
        return pyxel.rndi(0, 3)


class Input(Enum):
    Battle = 'たたかう'
    Pokemon = 'ポケモン'
    Bag = 'バッグ'
    Run = 'にげる'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


# 行動選択
class Choice:
    def __init__(self, command, pp):
        self.command = command
        self.pp = pp
        self.input_list = [a for a in Input]
        self.cursor = 1
        self.cmd_cursor = 1
        self.tmp_cmd = None
        self.rtn_cmd = None

    def up_player_choice(self):
        # ワザを選択
        if self.tmp_cmd == Input.Battle:
            self.up_cmd_choice()

        # 攻撃、交代を選択
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.tmp_cmd = self.input_list[self.cursor - 1]
        else:
            if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                if self.cursor % 2 == 0:
                    self.cursor -= 1
            if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                if self.cursor % 2 == 1:
                    self.cursor += 1
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                if self.cursor > 2:
                    self.cursor -= 2
            if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                if self.cursor < 3:
                    self.cursor += 2

        return self.rtn_cmd

    def dw_player_choice(self, font):
        if self.tmp_cmd is None:
            pyxel.text(85, 102, str(Input.Battle), 0, font)
            pyxel.text(125, 102, str(Input.Pokemon), 0, font)
            pyxel.text(85, 111, str(Input.Bag), 0, font)
            pyxel.text(125, 111, str(Input.Run), 0, font)
            if self.cursor % 2 == 0:
                cursor_x = 120
            else:
                cursor_x = 80
            if self.cursor > 2:
                cursor_y = 111
            else:
                cursor_y = 102
            pyxel.text(cursor_x, cursor_y, '>', 1)
        if self.tmp_cmd == Input.Battle:
            self.dw_cmd_choice(font)

    # ワザの選択
    def up_cmd_choice(self):
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            # コマンド選択は通し番号1からなので、-1している
            self.rtn_cmd = self.cmd_cursor - 1
        else:
            if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                if self.cmd_cursor % 2 == 0:
                    self.cmd_cursor -= 1
            if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                if self.cmd_cursor % 2 == 1:
                    self.cmd_cursor += 1
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                if self.cmd_cursor > 2:
                    self.cmd_cursor -= 2
            if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                if self.cmd_cursor < 3:
                    self.cmd_cursor += 2

        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.tmp_cmd = None

    def dw_cmd_choice(self, font):
        pyxel.text(10, 102, self.command[0][0], 0, font)
        pyxel.text(80, 102, self.command[1][0], 0, font)
        pyxel.text(10, 111, self.command[2][0], 0, font)
        pyxel.text(80, 111, self.command[3][0], 0, font)
        if self.cmd_cursor % 2 == 0:
            cursor_x = 75
        else:
            cursor_x = 5
        if self.cmd_cursor > 2:
            cursor_y = 111
        else:
            cursor_y = 102
        pyxel.text(cursor_x, cursor_y, '>', 1)

        # 技の説明
        pyxel.rect(0, 80, 160, 20, 6)
        pyxel.rectb(0, 80, 160, 20, 0)
        pyxel.text(5, 82, f'{self.command[self.cmd_cursor - 1][1]}', 0, font)
        pyxel.text(50, 82, f'{self.command[self.cmd_cursor - 1][2]}', 0, font)
        pyxel.text(5, 91, f'いりょく {self.command[self.cmd_cursor - 1][3]}', 0, font)
        pyxel.text(70, 91, f'めいちゅう {self.command[self.cmd_cursor - 1][4]}', 0, font)


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.font = pyxel.Font('assets\\misaki_gothic.bdf')
        pyxel.load('assets\\tadashi_pokemon.pyxres')
        pyxel.playm(0)

        # self.emboar = Pokemon('エンブオー', 176, 135, 93, 112, 94, 97, )
        # self.galvantula = Pokemon('デンチュラ', 136, 87, 77, 177, 76, 112, )
        # self.unfezant = Pokemon('ケンホロウ', 138, 118, 88, 69, 65, 100, )
        # self.seismitoad = Pokemon('ガマゲロゲ', 164, 111, 87, 93, 88, 85, )
        # self.deino = Pokemon('モノズ', 98, 58, 51, 42, 46, 45, )
        # self.gigigiaru = Pokemon('ギギギアル', 135, 120, 135, 90, 105, 110, )
        # self.abagora = Pokemon('アバゴーラ', 149, 128, 153, 103, 85, 52, )
        # self.akeosu = Pokemon('アーケオス', 150, 160, 85, 132, 85, 130, )
        # self.baibanira = Pokemon('バイバニラ', 146, 115, 105, 130, 115, 99, )
        # self.zoroaku = Pokemon('ゾロアーク', 135, 125, 80, 140, 80, 125, )

        self.zekrom = Pokemon('ゼクロム', 182, 177, 145, 145, 125, 114, Cmd.Fusion_Bolt, Cmd.Dragon_Claw,
                              Cmd.Zen_Headbutt, Cmd.Giga_Impact, Ele.Electric, Ele.Dragon, 52, [0, 0], False)
        self.reshiram = Pokemon('レシラム', 175, 140, 120, 170, 140, 110, Cmd.Fusion_Flare, Cmd.Dragon_Breath,
                                Cmd.Extrasensory, Cmd.Hyper_Beam, Ele.Fire, Ele.Dragon, 50, [32, 0], True)
        # イントロの終了
        self.end = True
        # 演出の遅延時間
        self.delay = 0
        # HPバーの表示
        self.damage = 0
        self.hp_count = 0
        self.hp_bef = 0

        # プレイヤーの行動選択のクラス
        self.choice = Choice(self.reshiram.command(), self.reshiram.pp())
        self.player_cmd = None
        self.turn = Turn(self.reshiram, self.zekrom)
        # CPUの行動
        self.cpu_cmd = None
        # プレイヤーが先攻ならTrue
        self.senkou = None

        pyxel.run(self.update, self.draw)

    def update(self):
        # イントロが終了したらループ部分を流す
        intro = pyxel.play_pos(0)
        if (intro == None and self.end):
            self.end = False
            pyxel.playm(1, loop=True)

        if self.delay == 0 and self.player_cmd is None and self.cpu_cmd is None and self.senkou is None:
            # プレイヤーの行動選択
            self.player_cmd = self.choice.up_player_choice()
            if self.player_cmd is not None:
                self.cpu_cmd = pyxel.rndi(0, 3)
                self.senkou = self.turn.senkou()

        # ダメ計
        if self.delay == 0 and self.senkou is not None and (self.player_cmd is not None or self.cpu_cmd is not None):
            if self.senkou:
                self.hp_bef = self.zekrom.h
                self.damage = self.turn.up_attack(my_flag=self.senkou, cmd=self.reshiram.cmd[self.player_cmd])
                self.hp_count = int(self.damage / 30)
                self.choice = Choice(self.reshiram.command(), self.reshiram.pp())
                self.delay = 60

            if not self.senkou:
                self.hp_bef = self.reshiram.h
                self.damage = self.turn.up_attack(my_flag=self.senkou, cmd=self.zekrom.cmd[self.cpu_cmd])
                self.hp_count = int(self.damage / 30)
                self.choice = Choice(self.zekrom.command(), self.zekrom.pp())
                self.delay = 60

        # 画面演出の遅延
        if self.delay >= 1:
            self.delay -= 1
        # 現在HPを更新
        if self.senkou is not None:

            if self.senkou:
                self.zekrom.h = self.zekrom.h - self.hp_count
                if self.zekrom.h < (self.hp_bef - self.damage):
                    self.zekrom.h = self.hp_bef - self.damage
                    self.damage = 0
                    self.hp_count = 0
                    self.hp_bef = 0
                    self.player_cmd = None

            if not self.senkou:
                self.reshiram.h = self.reshiram.h - self.hp_count
                if self.reshiram.h < (self.hp_bef - self.damage):
                    self.reshiram.h = self.hp_bef - self.damage
                    self.damage = 0
                    self.hp_count = 0
                    self.hp_bef = 0
                    self.cpu_cmd = None

            if self.player_cmd is None and self.cpu_cmd is None and self.delay == 0:
                self.senkou = None
                self.choice = Choice(self.reshiram.command(), self.reshiram.pp())
            elif (self.player_cmd is None or self.cpu_cmd is None) and self.delay == 0:
                self.senkou = not self.senkou

    def draw(self):

        # 背景の描画
        pyxel.blt(0, 0, 1, 0, 0, 160, 120)
        # テキストボックスを描画
        pyxel.rect(0, 100, 160, 20, 7)
        pyxel.rectb(0, 100, 160, 20, 0)
        # ポケモンを描画
        self.zekrom.poke_draw(self.font)
        self.reshiram.poke_draw(self.font)
        # テキストを描画
        if self.player_cmd is None and self.cpu_cmd is None and self.delay == 0:
            self.choice.dw_player_choice(self.font)

        if (self.player_cmd is not None or self.cpu_cmd is not None) and self.delay > 5:
            if self.senkou and self.player_cmd is not None:
                self.turn.dw_attack(my_flag=self.senkou, cmd=self.reshiram.cmd[self.player_cmd], font=self.font)
            if not self.senkou and self.cpu_cmd is not None:
                self.turn.dw_attack(my_flag=self.senkou, cmd=self.zekrom.cmd[self.cpu_cmd], font=self.font)


App()
