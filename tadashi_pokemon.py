import pyxel
from assets import pokemon_base as base

# 日本語フォント
font = pyxel.Font('assets\\misaki_gothic.bdf')


# ポケモンの攻撃
class Turn:
    def __init__(self, my_poke, op_poke):
        self.my_poke = my_poke
        self.op_poke = op_poke
        self.accuracy = None
        self.efficacy = None
        self.critical = None

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
            atk_poke = self.op_poke
            dff_poke = self.my_poke

        # 命中判定
        tmp7 = pyxel.rndi(1, 100)
        if tmp7 > cmd[4]:
            self.accuracy = 0
        else:
            self.accuracy = 1

        # ダメージ計算
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
        # タイプ一致補正
        if cmd[1] in atk_poke.tp:
            damage = int(damage * 1.5)

        # タイプ相性
        tmp6 = 1.0 * base.comp(cmd[1], dff_poke.tp[0]) * base.comp(cmd[1], dff_poke.tp[1])
        if self.accuracy == 0:
            self.efficacy = base.Efficacy.Miss
            delay = 120
        elif tmp6 == 2:
            self.efficacy = base.Efficacy.Twice
            delay = 120
        elif tmp6 == 0.5:
            self.efficacy = base.Efficacy.Half
            delay = 120
        elif tmp6 == 0:
            self.efficacy = base.Efficacy.Invalid
            delay = 120
        else:
            self.efficacy = None
            delay = 60
        damage = int(damage * tmp6 * self.accuracy)
        return damage, delay

    def dw_attack(self, my_flag, cmd, delay):
        if my_flag:
            atk_poke = self.my_poke
        else:
            atk_poke = self.op_poke
        if self.efficacy is None:
            pyxel.text(10, 102, f'{atk_poke.name} の {cmd[0]} !', 0, font)
        else:
            if delay > 65:
                pyxel.text(10, 102, f'{atk_poke.name} の {cmd[0]} !', 0, font)
            elif delay < 55 and delay > 5:
                pyxel.text(10, 102, str(self.efficacy), 0, font)


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

        elif self.tmp_cmd == base.Input.Pokemon:
            self.rtn_cmd = base.Input.Pokemon

        elif self.tmp_cmd == base.Input.Bag:
            self.rtn_cmd = base.Input.Bag

        elif self.tmp_cmd == base.Input.Run:
            self.rtn_cmd = base.Input.Run

        # 攻撃、交代を選択
        elif pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
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
            self.cmd_cursor = 1

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
    poke_x = 25
    poke_y = 45
    name_x = 70
    name_y = 50
    pyxel.blt(poke_x, poke_y, 0, poke.gra[0], poke.gra[1], 32, 32)
    pyxel.text(name_x, name_y, poke.name, 0, font)
    pyxel.text(name_x + 45, name_y, ('Lv.' + str(poke.lv)), 0, font)
    pyxel.text(name_x - 10, name_y + 8, 'HP', 0, font)
    pyxel.rect(name_x, name_y + 8, 70, 5, 0)
    pyxel.rect(name_x, name_y + 8, (70 * poke.h / poke.h_max), 5, 10)
    pyxel.text(name_x + 5, name_y + 15, str(poke.h), 0, font)
    pyxel.text(name_x + 20, name_y + 15, '/', 0, font)
    pyxel.text(name_x + 25, name_y + 15, str(poke.h_max), 0, font)


def draw_opp_poke(poke):
    poke_x = 100
    poke_y = 5
    name_x = 15
    name_y = 10
    pyxel.blt(poke_x, poke_y, 0, poke.gra[0], poke.gra[1], 32, 32)
    pyxel.text(name_x + 10, name_y, poke.name, 0, font)
    pyxel.text(name_x + 55, name_y, ('Lv.' + str(poke.lv)), 0, font)
    pyxel.text(name_x, name_y + 8, 'HP', 0, font)
    pyxel.rect(name_x + 10, name_y + 8, 70, 5, 0)
    pyxel.rect(name_x + 10, name_y + 8, (70 * poke.h / poke.h_max), 5, 10)


class PokemonChange:
    def __init__(self, trainer):
        self.trainer = trainer
        self.tmp_cmd = trainer.now
        self.tmp_cursor = None
        self.rtn_cmd = None
        self.list = [a for a in base.ChangeCursor]

    def update_change(self, self_change):

        if self.tmp_cursor is None:

            if pyxel.btnp(pyxel.KEY_Z or pyxel.GAMEPAD1_BUTTON_A) and self_change:
                self.rtn_cmd = 100

            if pyxel.btnp(pyxel.KEY_SPACE or pyxel.GAMEPAD1_BUTTON_B):
                if self.tmp_cmd == self.trainer.now:
                    self.tmp_cursor = 1
                else:
                    self.tmp_cursor = 0
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                if self.tmp_cmd > 0:
                    self.tmp_cmd -= 1
            if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                if self.tmp_cmd < 5:
                    self.tmp_cmd += 1
        else:
            if pyxel.btnp(pyxel.KEY_Z or pyxel.GAMEPAD1_BUTTON_A):
                self.tmp_cursor = None

            if pyxel.btnp(pyxel.KEY_SPACE or pyxel.GAMEPAD1_BUTTON_B):
                if self.list[self.tmp_cursor] == base.ChangeCursor.Cancel:
                    self.tmp_cursor = None

                elif self.list[self.tmp_cursor] == base.ChangeCursor.Change:
                    self.rtn_cmd = self.tmp_cmd

            if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                if (self.tmp_cmd == self.trainer.now and self.tmp_cursor > 1) or (
                        self.tmp_cmd != self.trainer.now and self.tmp_cursor > 0):
                    self.tmp_cursor -= 1
            if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                if self.tmp_cursor < 2:
                    self.tmp_cursor += 1

        return self.rtn_cmd

    def dw_change(self):
        x = 10
        y = 10
        # ポケモンとカーソル
        for i in range(6):
            pyxel.text(x, y + (i * 15), f'{self.trainer.member[i].name}', 0, font)
            pyxel.text(x + 45, y + (i * 15), f'Lv.{self.trainer.member[i].lv}', 0, font)
            if self.trainer.member[i].h == 0:
                pyxel.text(x + 70, y + (i * 15), 'ひんし', 0, font)
            pyxel.text(x + 100, y + (i * 15), f'{self.trainer.member[i].h} / {self.trainer.member[i].h_max}', 0, font)

        if self.tmp_cursor is None:
            pyxel.text(x - 5, 10 + (15 * self.tmp_cmd), '>', 1, font)

        else:
            pyxel.text(10, 102, f'{self.trainer.member[self.tmp_cmd].name}　を　どうする？', 0, font)

            if self.tmp_cmd != self.trainer.now:
                pyxel.text(10, 111, str(base.ChangeCursor.Change), 0, font)

            pyxel.text(65, 111, str(base.ChangeCursor.Status), 0, font)
            pyxel.text(120, 111, str(base.ChangeCursor.Cancel), 0, font)
            pyxel.text(5 + (55 * self.tmp_cursor), 111, '>', 1, font)


class BattleStatus:
    def __init__(self):
        self.scene = '-intro-'
        self.battle_now = '-neutral-'
        self.knockout = '-none-'
        self.delay = 180
        self.damage = None
        self.hp_count = 0
        self.hp_bef = None
        self.player_cmd = None
        self.cpu_cmd = None
        self.change_poke = None
        self.self_change = True

        # プレイヤーが先攻ならTrue
        self.senkou = None

    def param_reset(self):
        self.scene = '-battle-'
        self.battle_now = '-neutral-'
        self.knockout = '-none-'
        self.delay = 0
        self.damage = None
        self.hp_count = None
        self.hp_bef = None
        self.player_cmd = None
        self.cpu_cmd = None
        self.senkou = None
        self.change_poke = None

    def update_battle_now(self):
        if self.delay == 0:
            if self.scene == '-intro-':
                self.param_reset()

            # 自分のポケモンが倒れたとき
            if self.battle_now == '-player_knockout-' or self.battle_now == '-next_pokemon-':
                self.battle_now = '-next_pokemon-'
                self.scene = '-change_input-'
                self.self_change = False
                if self.change_poke is not None:
                    self.scene = '-battle-'
                    self.delay = 60
                    self.self_change = True

            # ポケモンを交代するとき
            elif self.player_cmd == base.Input.Pokemon:
                self.scene = '-change_input-'
                self.battle_now = '-neutral-'
                if self.change_poke is not None:
                    self.scene = '-battle-'
                    self.battle_now = '-pokemon_change-'
                    self.delay = 120

            elif self.player_cmd == base.Input.Bag:
                self.battle_now = '-no_item-'
                self.delay = 60

            elif self.player_cmd == base.Input.Run:
                self.battle_now = '-no_run-'
                self.delay = 60

            elif self.knockout == '-cpu-':
                self.delay = 180
                self.battle_now = '-cpu_knockout-'

            elif self.knockout == '-player-':
                self.delay = 60
                self.battle_now = '-player_knockout-'

            elif self.player_cmd is None and self.cpu_cmd is None and self.senkou is None:
                self.battle_now = '-input-'

            elif self.senkou and self.player_cmd is not None and self.hp_bef is None:
                self.delay = 60
                self.battle_now = '-player_attack-'

            elif not self.senkou and self.cpu_cmd is not None and self.hp_bef is None:
                self.delay = 60
                self.battle_now = '-cpu_attack-'

        elif self.delay > 0:
            self.delay -= 1


class App:
    def __init__(self):
        pyxel.init(160, 120)

        pyxel.load('assets\\tadashi_pokemon.pyxres')
        pyxel.playm(0)

        # 場面設定
        self.param = BattleStatus()

        # イントロの終了
        self.end = True

        # 各プレイヤー
        self.t = base.tadashi()
        self.n = base.plasma_n()

        # プレイヤーの行動選択のクラス
        self.choice = Choice(self.t.field())
        self.turn = Turn(self.t.field(), self.n.field())

        # ポケモン交代のクラス
        self.change = PokemonChange(self.t)

        pyxel.run(self.update, self.draw)

    def update(self):
        # イントロが終了したらループ部分を流す
        intro = pyxel.play_pos(0)
        if intro is None and self.end:
            self.end = False
            pyxel.playm(1, loop=True)

        self.param.update_battle_now()
        if self.param.scene == '-change_input-':
            self.param.change_poke = self.change.update_change(self.param.self_change)
            if self.param.change_poke == 100:
                self.param.param_reset()
                self.choice = Choice(self.t.field())
                self.change = PokemonChange(self.t)

        if self.param.scene == '-battle-':

            # プレイヤーの行動入力
            if self.param.battle_now == '-input-':
                self.param.player_cmd = self.choice.up_player_choice()
                # プレイヤーの行動が入力されたら
                if self.param.player_cmd is not None:
                    # CPUの攻撃をランダムに選択
                    self.param.cpu_cmd = pyxel.rndi(0, 3)
                    # 先攻を判定
                    self.param.senkou = self.turn.senkou()

            # ポケモン交換
            if self.param.battle_now == '-pokemon_change-':
                if self.param.delay == 60:
                    self.t.now = self.param.change_poke
                    self.param.change_poke = None
                    self.param.player_cmd = None
                    self.param.senkou = False
                    self.change = PokemonChange(self.t)
                    self.choice = Choice(self.t.field())
                    self.turn = Turn(self.t.field(), self.n.field())

            if self.param.battle_now == '-next_pokemon-':
                if self.param.delay == 60:
                    self.t.now = self.param.change_poke
                    self.change = PokemonChange(self.t)
                    self.choice = Choice(self.t.field())
                    self.turn = Turn(self.t.field(), self.n.field())

                if self.param.delay == 1:
                    self.param.param_reset()

            if (self.param.battle_now == '-no_item-' or self.param.battle_now == '-no_run-') and self.param.delay < 2:
                self.param.param_reset()
                self.choice = Choice(self.t.field())

            # ダメ計
            if self.param.battle_now == '-player_attack-':
                if self.param.hp_bef is None:
                    self.param.hp_bef = self.n.field().h
                    self.param.damage, self.param.delay = self.turn.up_attack(self.param.senkou,
                                                                              self.t.field().cmd[self.param.player_cmd])
                    self.param.hp_count = int(self.param.damage / 30)
                    if self.param.hp_count == 0 and self.param.damage != 0:
                        self.param.hp_count = 1
                    self.choice = Choice(self.t.field())

                # 攻撃描画
                self.n.field().h = self.n.field().h - self.param.hp_count
                # HPが0になった
                if self.n.field().h <= 0:
                    self.n.field().h = 0
                    self.param.param_reset()
                    self.param.knockout = '-cpu-'


                # HPバーの処理が完了
                elif self.n.field().h <= (self.param.hp_bef - self.param.damage):
                    self.n.field().h = self.param.hp_bef - self.param.damage
                    if self.param.delay == 0:
                        self.param.damage = None
                        self.param.hp_count = None
                        self.param.hp_bef = None
                        self.param.player_cmd = None

                        if self.param.cpu_cmd is not None:
                            self.param.senkou = not self.param.senkou
                        if self.param.cpu_cmd is None:
                            self.param.param_reset()

            if self.param.battle_now == '-cpu_attack-':
                if self.param.hp_bef is None:
                    self.param.hp_bef = self.t.field().h
                    self.param.damage, self.param.delay = self.turn.up_attack(self.param.senkou,
                                                                              self.n.field().cmd[self.param.cpu_cmd])
                    self.param.hp_count = int(self.param.damage / 30)
                    if self.param.hp_count == 0 and self.param.damage != 0:
                        self.param.hp_count = 1

                # 攻撃描画
                self.t.field().h = self.t.field().h - self.param.hp_count

                # HPが0になった
                if self.t.field().h <= 0:
                    self.t.field().h = 0
                    self.param.param_reset()
                    self.param.knockout = '-player-'
                # HPバーの処理が完了
                elif self.t.field().h <= (self.param.hp_bef - self.param.damage):
                    self.t.field().h = self.param.hp_bef - self.param.damage
                    if self.param.delay == 0:
                        self.param.damage = None
                        self.param.hp_count = None
                        self.param.hp_bef = None
                        self.param.cpu_cmd = None

                        if self.param.player_cmd is not None:
                            self.param.senkou = not self.param.senkou

                        if self.param.player_cmd is None:
                            self.param.param_reset()

            if self.param.battle_now == '-cpu_knockout-':
                if self.param.delay == 90:
                    self.n.now += 1
                if self.param.delay == 0:
                    self.param.param_reset()
                    self.turn = Turn(self.t.field(), self.n.field())

    def draw(self):

        pyxel.cls(1)

        # 背景の描画
        pyxel.blt(0, 0, 1, 0, 0, 160, 120)
        # テキストボックスを描画
        pyxel.rect(0, 100, 160, 20, 7)
        pyxel.rectb(0, 100, 160, 20, 0)

        if self.param.scene == '-intro-':
            if self.param.delay > 125:
                pyxel.blt(100, 5, 0, 0, 64, 48, 48)
                pyxel.text(10, 102, 'プラズマだんの　N が', 0, font)
                pyxel.text(10, 111, 'しょうぶを　しかけてきた！', 0, font)
            if self.param.delay < 100:
                draw_opp_poke(self.n.field())
            if self.param.delay < 120 and self.param.delay > 65:
                pyxel.text(10, 102, 'プラズマだんの　N は', 0, font)
                pyxel.text(10, 111, 'ゼクロム　を　くりだした！', 0, font)
            if self.param.delay>65:
                pyxel.blt(25,50,0,48,64,48,48)
            if self.param.delay<40:
                draw_my_poke(self.t.field())
            if self.param.delay<55 and self.param.delay>5:
                pyxel.text(10, 102, f'ゆけっ！　{self.t.field().name}！', 0, font)

        if self.param.scene == '-change_input-':
            self.change.dw_change()

        if self.param.scene == '-battle-':

            # ポケモンを描画
            draw_my_poke(self.t.field())
            draw_opp_poke(self.n.field())
            if self.param.battle_now == '-pokemon_change-':
                if self.param.delay < 115 and self.param.delay > 65:
                    pyxel.text(10, 102, f'もどれ！　{self.t.field().name}！', 0, font)

                if self.param.delay < 55 and self.param.delay > 5:
                    pyxel.text(10, 102, f'ゆけっ！　{self.t.field().name}！', 0, font)

            if self.param.battle_now == '-next_pokemon-':
                if self.param.delay < 55 and self.param.delay > 5:
                    pyxel.text(10, 102, f'ゆけっ！　{self.t.field().name}！', 0, font)

            if self.param.battle_now == '-no_item-' and self.param.delay > 5:
                pyxel.text(10, 102, 'どうぐを　もっていない！', 0, font)

            if self.param.battle_now == '-no_run-' and self.param.delay > 5:
                pyxel.text(10, 102, 'だめだ！　しょうぶの　さいちゅうに', 0, font)
                pyxel.text(10, 111, 'てきに　せなかを　みせられない！', 0, font)
            # テキストを描画
            if self.param.battle_now == '-input-':
                self.choice.dw_player_choice()

            if self.param.battle_now == '-player_attack-' and self.param.delay > 5:
                self.turn.dw_attack(self.param.senkou, self.t.field().cmd[self.param.player_cmd], self.param.delay)

            if self.param.battle_now == '-cpu_attack-' and self.param.delay > 5:
                self.turn.dw_attack(self.param.senkou, self.n.field().cmd[self.param.cpu_cmd], self.param.delay)

            if self.param.battle_now == '-cpu_knockout-':
                if self.param.delay < 170 and self.param.delay > 95:
                    pyxel.text(10, 102, f'あいての　{self.n.field().name}　は　たおれた！', 0, font)

                if self.param.delay < 85 and self.param.delay > 10:
                    pyxel.text(10, 102, 'プラズマだんの　N　は', 0, font)
                    pyxel.text(10, 111, f'{self.n.field().name}を　くりだした！', 0, font)

            if self.param.battle_now == '-player_knockout-':
                if self.param.delay < 55 and self.param.delay > 5:
                    pyxel.text(10, 102, f'{self.t.field().name}　は　たおれた！', 0, font)


App()
