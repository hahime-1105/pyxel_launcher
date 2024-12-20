import pyxel
from assets import pokemon_base as base

# 日本語フォント
font = pyxel.Font('assets\\misaki_gothic.bdf')


# ポケモンの攻撃
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
        if cmd[2] == base.Cat.physical:
            tmp2 = atk_poke.a * cmd[3]
            tmp3 = int(tmp1 * tmp2 / dff_poke.b)
        if cmd[2] == base.Cat.special:
            tmp2 = atk_poke.c * cmd[3]
            tmp3 = int(tmp1 * tmp2 / dff_poke.d)
        tmp4 = int((tmp3 / 50) + 2)
        tmp5 = 1.0 * pyxel.rndi(85, 100) / 100
        damage = int(tmp4 * tmp5)
        return damage

    def dw_attack(self, my_flag, cmd):
        if my_flag:
            atk_poke = self.my_poke
        else:
            atk_poke = self.op_poke
        pyxel.text(10, 102, f'{atk_poke.name} の {cmd[0]} !', 0, font)


# プレイヤーの行動選択
class Choice:
    def __init__(self, poke):
        self.command = poke.command()
        self.pp = poke.pp()
        self.input_list = [a for a in base.Input]
        self.cursor = 1
        self.cmd_cursor = 1
        self.tmp_cmd = None
        self.rtn_cmd = None

    def up_player_choice(self):
        # ワザを選択
        if self.tmp_cmd == base.Input.Battle:
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

    def dw_player_choice(self):
        if self.tmp_cmd is None:
            pyxel.text(85, 102, str(base.Input.Battle), 0, font)
            pyxel.text(125, 102, str(base.Input.Pokemon), 0, font)
            pyxel.text(85, 111, str(base.Input.Bag), 0, font)
            pyxel.text(125, 111, str(base.Input.Run), 0, font)
            if self.cursor % 2 == 0:
                cursor_x = 120
            else:
                cursor_x = 80
            if self.cursor > 2:
                cursor_y = 111
            else:
                cursor_y = 102
            pyxel.text(cursor_x, cursor_y, '>', 1, font)
        if self.tmp_cmd == base.Input.Battle:
            self.dw_cmd_choice()

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

    def dw_cmd_choice(self):
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
        pyxel.text(cursor_x, cursor_y, '>', 1, font)

        # 技の説明
        pyxel.rect(0, 80, 160, 20, 6)
        pyxel.rectb(0, 80, 160, 20, 0)
        pyxel.text(5, 82, f'{self.command[self.cmd_cursor - 1][1]}', 0, font)
        pyxel.text(50, 82, f'{self.command[self.cmd_cursor - 1][2]}', 0, font)
        pyxel.text(5, 91, f'いりょく {self.command[self.cmd_cursor - 1][3]}', 0, font)
        pyxel.text(70, 91, f'めいちゅう {self.command[self.cmd_cursor - 1][4]}', 0, font)


def draw_my_poke(poke):
    poke_x = 15
    poke_y = 45
    name_x = 60
    name_y = 50
    pyxel.blt(poke_x, poke_y, 0, poke.gra[0], poke.gra[1], 32, 32)
    pyxel.text(name_x, name_y, poke.name, 0, font)
    pyxel.text(name_x + 40, name_y, ('Lv.' + str(poke.lv)), 0, font)
    pyxel.text(name_x, name_y + 8, 'HP', 0, font)
    pyxel.rect(name_x + 10, name_y + 8, 50, 5, 0)
    pyxel.rect(name_x + 10, name_y + 8, (50 * poke.h / poke.h_max), 5, 10)
    pyxel.text(name_x + 15, name_y + 15, str(poke.h), 0, font)
    pyxel.text(name_x + 30, name_y + 15, '/', 0, font)
    pyxel.text(name_x + 35, name_y + 15, str(poke.h_max), 0, font)


def draw_opp_poke(poke):
    poke_x = 100
    poke_y = 5
    name_x = 30
    name_y = 10
    pyxel.blt(poke_x, poke_y, 0, poke.gra[0], poke.gra[1], 32, 32)
    pyxel.text(name_x, name_y, poke.name, 0, font)
    pyxel.text(name_x + 40, name_y, ('Lv.' + str(poke.lv)), 0, font)
    pyxel.text(name_x, name_y + 8, 'HP', 0, font)
    pyxel.rect(name_x + 10, name_y + 8, 50, 5, 0)
    pyxel.rect(name_x + 10, name_y + 8, (50 * poke.h / poke.h_max), 5, 10)


def update_battle_status(delay, player_cmd, cpu_cmd, senkou, knockout):
    if delay == 0 and player_cmd is None and cpu_cmd is None and senkou is None:
        return '-input-'

    if delay == 0 and senkou is not None and (player_cmd is not None or cpu_cmd is not None):
        return '-damage-'


class App:
    def __init__(self):
        pyxel.init(160, 120)

        pyxel.load('assets\\tadashi_pokemon.pyxres')
        pyxel.playm(0)

        # 場面設定
        self.scene = '-battle-'
        self.battle_status = '-neutral-'
        self.knockout = '-none-'

        # イントロの終了
        self.end = True
        # 演出の遅延時間
        self.delay = 0
        # HPバーの表示
        self.damage = 0
        self.hp_count = 0
        self.hp_bef = 0

        # 各プレイヤー
        self.t = base.tadashi()
        self.n = base.plasma_n()

        # プレイヤーの行動選択のクラス
        self.choice = Choice(self.t.field())
        self.player_cmd = None
        self.turn = Turn(self.t.field(), self.n.field())
        # CPUの行動
        self.cpu_cmd = None
        # プレイヤーが先攻ならTrue
        self.senkou = None

        pyxel.run(self.update, self.draw)

    def update(self):
        # イントロが終了したらループ部分を流す
        intro = pyxel.play_pos(0)
        if intro is None and self.end:
            self.end = False
            pyxel.playm(1, loop=True)

        if self.scene == '-battle-':

            self.battle_status = update_battle_status(
                self.delay, self.player_cmd, self.cpu_cmd, self.senkou, self.knockout
            )

            # プレイヤーの行動入力
            if self.battle_status == '-input-':
                self.player_cmd = self.choice.up_player_choice()

                # プレイヤーの行動が入力されたら
                if self.player_cmd is not None:
                    # CPUの攻撃をランダムに選択
                    self.cpu_cmd = pyxel.rndi(0, 3)
                    # 先攻を判定
                    self.senkou = self.turn.senkou()

            # ダメ計
            if self.battle_status == '-damage-':
                self.delay = 60
                if self.senkou:
                    self.hp_bef = self.n.field().h
                    self.damage = self.turn.up_attack(my_flag=self.senkou, cmd=self.t.field().cmd[self.player_cmd])
                    self.hp_count = int(self.damage / 30)
                    self.choice = Choice(self.t.field())

                if not self.senkou:
                    self.hp_bef = self.t.field().h
                    self.damage = self.turn.up_attack(my_flag=self.senkou, cmd=self.n.field().cmd[self.cpu_cmd])
                    self.hp_count = int(self.damage / 30)
                    self.choice = Choice(self.n.field())

            # 画面演出の遅延
            if self.delay >= 1:
                self.delay -= 1

            # 現在HPを更新
            if self.senkou is not None:
                # プレイヤーの攻撃描画
                if self.senkou:
                    self.n.field().h = self.n.field().h - self.hp_count

                    # HPが0になった
                    if self.n.field().h <= 0:
                        self.n.field().h = 0
                        self.damage = 0
                        self.hp_count = 0
                        self.hp_bef = 0
                        self.player_cmd = None
                        self.knockout = '-cpu-'

                    # HPバーの処理が完了
                    if self.n.field().h < (self.hp_bef - self.damage):
                        self.n.field().h = self.hp_bef - self.damage
                        self.damage = 0
                        self.hp_count = 0
                        self.hp_bef = 0
                        self.player_cmd = None

                # cpuの攻撃描画
                if not self.senkou:
                    self.t.field().h = self.t.field().h - self.hp_count

                    if self.t.field().h <= 0:
                        self.t.field().h = 0
                        self.damage = 0
                        self.hp_count = 0
                        self.hp_bef = 0
                        self.cpu_cmd = None
                        self.knockout = '-player-'

                    if self.t.field().h < (self.hp_bef - self.damage):
                        self.t.field().h = self.hp_bef - self.damage
                        self.damage = 0
                        self.hp_count = 0
                        self.hp_bef = 0
                        self.cpu_cmd = None

                if self.knockout == '-none-':
                    # 次のターンにいく
                    if self.player_cmd is None and self.cpu_cmd is None and self.delay == 0:
                        self.senkou = None
                        self.choice = Choice(self.t.field())

                    # 後攻の攻撃を処理
                    elif (self.player_cmd is None or self.cpu_cmd is None) and self.delay == 0:
                        self.senkou = not self.senkou
                        print('攻守交替')

                if self.knockout == '-cpu-' and self.delay == 0:
                    self.n.now += 1
                    self.senkou = None
                    self.cpu_cmd = None
                    self.choice = Choice(self.t.field())
                    self.turn = Turn(self.t.field(), self.n.field())
                    self.knockout = '-none-'

    def draw(self):

        if self.scene == '-battle-':
            # 背景の描画
            pyxel.blt(0, 0, 1, 0, 0, 160, 120)
            # テキストボックスを描画
            pyxel.rect(0, 100, 160, 20, 7)
            pyxel.rectb(0, 100, 160, 20, 0)
            # ポケモンを描画
            draw_my_poke(self.t.field())
            draw_opp_poke(self.n.field())
            # テキストを描画
            if self.player_cmd is None and self.cpu_cmd is None and self.delay == 0:
                self.choice.dw_player_choice()

            if (self.player_cmd is not None or self.cpu_cmd is not None) and self.delay > 5:
                if self.senkou and self.player_cmd is not None:
                    self.turn.dw_attack(my_flag=self.senkou, cmd=self.t.field().cmd[self.player_cmd])
                if not self.senkou and self.cpu_cmd is not None:
                    self.turn.dw_attack(my_flag=self.senkou, cmd=self.n.field().cmd[self.cpu_cmd])


App()
