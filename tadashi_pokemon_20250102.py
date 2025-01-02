import pyxel
from enum import Enum


# タイプ相性の表示
class Efficacy(Enum):
    Twice = 'こうかは　ばつぐんだ！'
    Half = 'こうかは　いまひとつの　ようだ…'
    Invalid = 'こうはは　ないようだ…'
    Miss = 'こうげきは　あたらなかった！'
    Critical = 'きゅうしょに　あたった！'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.name


# ポケモン交換の選択
class ChangeCursor(Enum):
    Change = 'いれかえる'
    Status = 'つよさをみる'
    Cancel = 'やめる'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.name


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


# ワザ[技名、タイプ、分類、威力、命中、PP、効果]
class Cmd:
    eff = Effect()
    Fusion_Flare = ['クロスフレイム', Ele.Fire, Cat.special, 100, 100, 5, eff.none()]
    Fusion_Bolt = ['クロスサンダー', Ele.Electric, Cat.physical, 100, 100, 5, eff.none()]
    Dragon_Breath = ['りゅうのいぶき', Ele.Dragon, Cat.special, 60, 100, 20, eff.none()]
    Dragon_Claw = ['ドラゴンクロー', Ele.Dragon, Cat.physical, 80, 100, 15, eff.none()]
    Hyper_Beam = ['はかいこうせん', Ele.Normal, Cat.special, 150, 60, 5, eff.none()]
    Giga_Impact = ['ギガインパクト', Ele.Normal, Cat.physical, 150, 90, 5, eff.none()]
    Zen_Headbutt = ['しねんのずつき', Ele.Psychic, Cat.physical, 80, 90, 15, eff.none()]
    Extrasensory = ['じんつうりき', Ele.Psychic, Cat.special, 80, 100, 30, eff.none()]
    Brick_Break = ['かわらわり', Ele.Fighting, Cat.physical, 75, 100, 15, eff.none()]
    Flamethrower = ['かえんほうしゃ', Ele.Fire, Cat.special, 95, 100, 15, eff.none()]
    Head_Smash = ['もろはのずつき', Ele.Rock, Cat.physical, 150, 90, 5, eff.none()]
    Flame_Charge = ['ニトロチャージ', Ele.Fire, Cat.physical, 50, 100, 20, eff.none()]
    Electroweb = ['エレキネット', Ele.Electric, Cat.special, 55, 95, 15, eff.none()]
    Sucker_Punch = ['ふいうち', Ele.Dark, Cat.physical, 70, 100, 5, eff.none()]
    Eletro_Ball = ['エレキボール', Ele.Electric, Cat.special, 50, 100, 10, eff.none()]
    Signal_Beam = ['シグナルビーム', Ele.Bug, Cat.special, 75, 100, 15, eff.none()]
    Surf = ['なみのり', Ele.Water, Cat.special, 95, 100, 15, eff.none()]
    Mud_Shot = ['マッドショット', Ele.Ground, Cat.special, 55, 95, 15, eff.none()]
    Drain_Punch = ['ドレインパンチ', Ele.Fighting, Cat.physical, 75, 100, 15, eff.none()]
    Muddy_Water = ['だくりゅう', Ele.Water, Cat.special, 90, 85, 10, eff.none()]
    Crunch = ['かみくだく', Ele.Dark, Cat.physical, 80, 100, 15, eff.none()]
    Slam = ['たたきつける', Ele.Normal, Cat.physical, 80, 75, 20, eff.none()]
    Air_Slash = ['エアスラッシュ', Ele.Flying, Cat.special, 75, 95, 15, eff.none()]
    Fly = ['そらをとぶ', Ele.Flying, Cat.physical, 95, 95, 15, eff.none()]
    Quick_Attack = ['でんこうせっか', Ele.Normal, Cat.physical, 40, 100, 20, eff.none()]
    Aqua_Jet = ['アクアジェット', Ele.Water, Cat.physical, 40, 100, 20, eff.none()]
    Waterfall = ['たきのぼり', Ele.Water, Cat.physical, 80, 100, 15, eff.none()]
    Stone_Edge = ['ストーンエッジ', Ele.Rock, Cat.physical, 100, 80, 5, eff.none()]
    Thunderbolt = ['10まんボルト', Ele.Electric, Cat.special, 95, 100, 15, eff.none()]
    Flash_Cannon = ['ラスターカノン', Ele.Steel, Cat.special, 80, 100, 10, eff.none()]
    Zap_Cannon = ['でんじほう', Ele.Electric, Cat.special, 100, 50, 5, eff.none()]
    Night_Slash = ['つじぎり', Ele.Dark, Cat.physical, 75, 100, 20, eff.none()]
    Focus_Blast = ['きあいだま', Ele.Fighting, Cat.special, 120, 70, 5, eff.none()]
    Retaliate = ['かたきうち', Ele.Normal, Cat.physical, 70, 100, 5, eff.none()]
    Acrobatics = ['アクロバット', Ele.Flying, Cat.physical, 110, 100, 15, eff.none()]
    Frost_Breath = ['こおりのいぶき', Ele.Ice, Cat.special, 90, 90, 10, eff.none()]
    Blizzard = ['ふぶき', Ele.Ice, Cat.special, 110, 70, 5, eff.none()]


# タイプ相性
def comp(atk_ele, dff_ele):
    if dff_ele is None:
        return 1
    else:
        if atk_ele == Ele.Normal:
            if dff_ele == Ele.Ghost:
                return 0
            elif dff_ele == Ele.Rock or dff_ele == Ele.Steel:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Fire:
            if dff_ele == Ele.Grass or dff_ele == Ele.Ice or dff_ele == Ele.Bug or dff_ele == Ele.Steel:
                return 2
            elif dff_ele == Ele.Fire or dff_ele == Ele.Water or dff_ele == Ele.Rock or dff_ele == Ele.Dragon:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Water:
            if dff_ele == Ele.Fire or dff_ele == Ele.Ground or dff_ele == Ele.Rock:
                return 2
            elif dff_ele == Ele.Water or dff_ele == Ele.Grass or dff_ele == Ele.Dragon:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Electric:
            if dff_ele == Ele.Ground:
                return 0
            elif dff_ele == Ele.Water or dff_ele == Ele.Flying:
                return 2
            elif dff_ele == Ele.Electric or dff_ele == Ele.Grass or dff_ele == Ele.Dragon:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Grass:
            if dff_ele == Ele.Water or dff_ele == Ele.Grass or dff_ele == Ele.Rock:
                return 2
            elif dff_ele == Ele.Fire or dff_ele == Ele.Grass or dff_ele == Ele.Poison or dff_ele == Ele.Flying or dff_ele == Ele.Bug or dff_ele == Ele.Dragon or dff_ele == Ele.Steel:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Ice:
            if dff_ele == Ele.Grass or dff_ele == Ele.Ground or dff_ele == Ele.Flying or dff_ele == Ele.Dragon:
                return 2
            elif dff_ele == Ele.Fire or dff_ele == Ele.Water or dff_ele == Ele.Ice or dff_ele == Ele.Steel:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Fighting:
            if dff_ele == Ele.Normal or dff_ele == Ele.Ice or dff_ele == Ele.Rock or dff_ele == Ele.Dark or dff_ele == Ele.Steel:
                return 2
            elif dff_ele == Ele.Poison or dff_ele == Ele.Flying or dff_ele == Ele.Psychic or dff_ele == Ele.Bug or dff_ele == Ele.Fairy:
                return 0.5
            elif dff_ele == Ele.Ghost:
                return 0
            else:
                return 1
        if atk_ele == Ele.Poison:
            if dff_ele == Ele.Grass or dff_ele == Ele.Fairy:
                return 2
            elif dff_ele == Ele.Poison or dff_ele == Ele.Ground or dff_ele == Ele.Rock or dff_ele == Ele.Ghost:
                return 0.5
            elif dff_ele == Ele.Steel:
                return 0
            else:
                return 1
        if atk_ele == Ele.Ground:
            if dff_ele == Ele.Fire or dff_ele == Ele.Electric or dff_ele == Ele.Poison or dff_ele == Ele.Rock or dff_ele == Ele.Steel:
                return 2
            elif dff_ele == Ele.Grass or dff_ele == Ele.Bug:
                return 0.5
            elif dff_ele == Ele.Flying:
                return 0
            else:
                return 1
        if atk_ele == Ele.Flying:
            if dff_ele == Ele.Grass or dff_ele == Ele.Fighting or dff_ele == Ele.Bug:
                return 2
            if dff_ele == Ele.Electric or dff_ele == Ele.Rock or dff_ele == Ele.Steel:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Psychic:
            if dff_ele == Ele.Fighting or dff_ele == Ele.Poison:
                return 2
            elif dff_ele == Ele.Psychic or dff_ele == Ele.Steel:
                return 0.5
            elif dff_ele == Ele.Dark:
                return 0
            else:
                return 1
        if atk_ele == Ele.Bug:
            if dff_ele == Ele.Grass or dff_ele == Ele.Psychic or dff_ele == Ele.Dark:
                return 2
            elif dff_ele == Ele.Fire or dff_ele == Ele.Fighting or dff_ele == Ele.Poison or dff_ele == Ele.Flying or dff_ele == Ele.Ghost or dff_ele == Ele.Steel or dff_ele == Ele.Fairy:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Rock:
            if dff_ele == Ele.Fire or dff_ele == Ele.Ice or dff_ele == Ele.Flying or dff_ele == Ele.Bug:
                return 2
            elif dff_ele == Ele.Fighting or dff_ele == Ele.Ground or dff_ele == Ele.Steel:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Ghost:
            if dff_ele == Ele.Psychic or dff_ele == Ele.Ghost:
                return 2
            elif dff_ele == Ele.Dark:
                return 0.5
            elif dff_ele == Ele.Normal:
                return 0
            else:
                return 1
        if atk_ele == Ele.Dragon:
            if dff_ele == Ele.Dragon:
                return 2
            elif dff_ele == Ele.Steel:
                return 0.5
            elif dff_ele == Ele.Fairy:
                return 0
            else:
                return 1
        if atk_ele == Ele.Dark:
            if dff_ele == Ele.Psychic or dff_ele == Ele.Ghost:
                return 2
            elif dff_ele == Ele.Fighting or dff_ele == Ele.Dark or dff_ele == Ele.Fairy:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Steel:
            if dff_ele == Ele.Ice or dff_ele == Ele.Rock or dff_ele == Ele.Fairy:
                return 2
            elif dff_ele == Ele.Fire or dff_ele == Ele.Water or dff_ele == Ele.Electric or dff_ele == Ele.Steel:
                return 0.5
            else:
                return 1
        if atk_ele == Ele.Fairy:
            if dff_ele == Ele.Fire or dff_ele == Ele.Poison or dff_ele == Ele.Steel:
                return 0.5
            elif dff_ele == Ele.Fighting or dff_ele == Ele.Dragon or dff_ele == Ele.Dark:
                return 2
            else:
                return 1


class Input(Enum):
    Battle = 'たたかう'
    Pokemon = 'ポケモン'
    Bag = 'バッグ'
    Run = 'にげる'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Trainer:
    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.member = []
        self.member.append(p1)
        self.member.append(p2)
        self.member.append(p3)
        self.member.append(p4)
        self.member.append(p5)
        self.member.append(p6)
        self.now = 0

    def field(self):
        return self.member[self.now]


# ポケモン
class Pokemon:
    # ワザとステータス、graはイメージバンクの位置、myは自分だったらTrue, 相手だったらFalse
    def __init__(self, name, h, a, b, c, d, s, cmd1, cmd2, cmd3, cmd4, tp1, tp2, lv, gra):
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

    def command(self):
        return self.cmd

    def pp(self):
        return self.pp_now


def tadashi():
    reshiram = Pokemon(
        'レシラム', 175, 140, 120, 170, 140, 110,
        Cmd.Fusion_Flare, Cmd.Dragon_Breath, Cmd.Extrasensory, Cmd.Hyper_Beam,
        Ele.Fire, Ele.Dragon, 50, [32, 0]
    )
    emboar = Pokemon(
        'エンブオー', 176, 135, 93, 112, 94, 97,
        Cmd.Brick_Break, Cmd.Flamethrower, Cmd.Head_Smash, Cmd.Flame_Charge,
        Ele.Fire, Ele.Fighting, 50, [0, 0]
    )
    galvantula = Pokemon(
        'デンチュラ', 136, 87, 77, 177, 76, 112,
        Cmd.Electroweb, Cmd.Signal_Beam, Cmd.Eletro_Ball, Cmd.Sucker_Punch,
        Ele.Electric, Ele.Bug, 50, [64, 0]
    )
    unfezant = Pokemon(
        'ケンホロウ', 138, 118, 88, 69, 65, 100,
        Cmd.Air_Slash, Cmd.Fly, Cmd.Quick_Attack, Cmd.Night_Slash,
        Ele.Normal, Ele.Flying, 44, [128, 0]
    )
    seismitoad = Pokemon(
        'ガマゲロゲ', 164, 111, 87, 93, 88, 85,
        Cmd.Surf, Cmd.Drain_Punch, Cmd.Mud_Shot, Cmd.Muddy_Water,
        Ele.Water, Ele.Ground, 47, [96, 0]
    )
    deino = Pokemon(
        'モノズ', 98, 58, 51, 42, 46, 45,
        Cmd.Crunch, Cmd.Dragon_Breath, Cmd.Slam, Cmd.Zen_Headbutt,
        Ele.Dark, Ele.Dragon, 38, [160, 0]
    )
    player = Trainer(
        reshiram, emboar, galvantula, unfezant, seismitoad, deino
    )
    return player


def plasma_n():
    gigigiaru = Pokemon(
        'ギギギアル', 135, 120, 135, 90, 105, 110,
        Cmd.Thunderbolt, Cmd.Flash_Cannon, Cmd.Hyper_Beam, Cmd.Zap_Cannon,
        Ele.Steel, None, 50, [64, 32]
    )
    abagora = Pokemon(
        'アバゴーラ', 149, 128, 153, 103, 85, 52,
        Cmd.Waterfall, Cmd.Stone_Edge, Cmd.Aqua_Jet, Cmd.Crunch,
        Ele.Rock, Ele.Water, 50, [32, 32]
    )
    akeosu = Pokemon(
        'アーケオス', 150, 160, 85, 132, 85, 130,
        Cmd.Dragon_Claw, Cmd.Acrobatics, Cmd.Stone_Edge, Cmd.Crunch,
        Ele.Rock, Ele.Flying, 50, [128, 32]
    )
    baibanira = Pokemon(
        'バイバニラ', 146, 115, 105, 130, 115, 99,
        Cmd.Frost_Breath, Cmd.Blizzard, Cmd.Flash_Cannon, Cmd.Hyper_Beam,
        Ele.Ice, None, 50, [160, 32]
    )
    zoroaku = Pokemon(
        'ゾロアーク', 135, 125, 80, 140, 80, 125,
        Cmd.Night_Slash, Cmd.Flamethrower, Cmd.Focus_Blast, Cmd.Retaliate,
        Ele.Dark, None, 50, [96, 32]
    )
    zekrom = Pokemon(
        'ゼクロム', 182, 177, 145, 145, 125, 114,
        Cmd.Fusion_Bolt, Cmd.Dragon_Claw, Cmd.Zen_Headbutt, Cmd.Giga_Impact,
        Ele.Electric, Ele.Dragon, 52, [0, 32]
    )
    n = Trainer(
        zekrom, abagora, gigigiaru, zoroaku, akeosu, baibanira
    )
    return n


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
        if cmd[2] == Cat.physical:
            tmp2 = atk_poke.a * cmd[3]
            tmp3 = int(tmp1 * tmp2 / dff_poke.b)
        if cmd[2] == Cat.special:
            tmp2 = atk_poke.c * cmd[3]
            tmp3 = int(tmp1 * tmp2 / dff_poke.d)
        tmp4 = int((tmp3 / 50) + 2)
        tmp5 = 1.0 * pyxel.rndi(85, 100) / 100
        damage = int(tmp4 * tmp5)
        # タイプ一致補正
        if cmd[1] in atk_poke.tp:
            damage = int(damage * 1.5)

        # タイプ相性
        tmp6 = 1.0 * comp(cmd[1], dff_poke.tp[0]) * comp(cmd[1], dff_poke.tp[1])
        if self.accuracy == 0:
            self.efficacy = Efficacy.Miss
            delay = 120
        elif tmp6 == 2:
            self.efficacy = Efficacy.Twice
            delay = 120
        elif tmp6 == 0.5:
            self.efficacy = Efficacy.Half
            delay = 120
        elif tmp6 == 0:
            self.efficacy = Efficacy.Invalid
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
        self.input_list = [a for a in Input]
        self.cursor = 1
        self.cmd_cursor = 1
        self.tmp_cmd = None
        self.rtn_cmd = None

    def up_player_choice(self):
        # ワザを選択
        if self.tmp_cmd == Input.Battle:
            self.up_cmd_choice()

        elif self.tmp_cmd == Input.Pokemon:
            self.rtn_cmd = Input.Pokemon

        elif self.tmp_cmd == Input.Bag:
            self.rtn_cmd = Input.Bag

        elif self.tmp_cmd == Input.Run:
            self.rtn_cmd = Input.Run

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
            pyxel.text(cursor_x, cursor_y, '>', 1, font)
        if self.tmp_cmd == Input.Battle:
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
        self.list = [a for a in ChangeCursor]

    def update_change(self, self_change):

        if self.tmp_cursor is None:

            if (pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)) and self_change:
                self.rtn_cmd = 100

            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
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
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.tmp_cursor = None

            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                if self.list[self.tmp_cursor] == ChangeCursor.Cancel:
                    self.tmp_cursor = None

                elif self.list[self.tmp_cursor] == ChangeCursor.Change:
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
                pyxel.text(10, 111, str(ChangeCursor.Change), 0, font)

            pyxel.text(65, 111, str(ChangeCursor.Status), 0, font)
            pyxel.text(120, 111, str(ChangeCursor.Cancel), 0, font)
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
            elif self.player_cmd == Input.Pokemon:
                self.scene = '-change_input-'
                self.battle_now = '-neutral-'
                if self.change_poke is not None:
                    self.scene = '-battle-'
                    self.battle_now = '-pokemon_change-'
                    self.delay = 120

            elif self.player_cmd == Input.Bag:
                self.battle_now = '-no_item-'
                self.delay = 60

            elif self.player_cmd == Input.Run:
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
        self.t = tadashi()
        self.n = plasma_n()

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
            if self.param.delay > 65:
                pyxel.blt(25, 50, 0, 48, 64, 48, 48)
            if self.param.delay < 40:
                draw_my_poke(self.t.field())
            if self.param.delay < 55 and self.param.delay > 5:
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
