from enum import Enum
from wsgiref.util import request_uri

from setuptools.sandbox import run_setup


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
