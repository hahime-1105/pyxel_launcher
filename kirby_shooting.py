import pyxel

PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
PLAYER_SPEED = 2
PLAYER_LIFE = 5
PLAYER_FPS = 5
PLAYER_MOTION = 10

BULLET_WIDTH = 16
BULLET_HEIGHT = 16
BULLET_SPEED = 4

ENEMY_WIDTH = 16
ENEMY_HEIGHT = 16
ENEMY_SPEED = 2
ENEMY_FPS = 4
ENEMY_RATE = 30

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

bullets = []
enemies = []
blasts = []


def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        elem.draw()


def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.i = PLAYER_MOTION  # 攻撃モーション時間
        self.f = PLAYER_FPS  # 自機アニメーションのfps
        self.a = True  # 攻撃中か否か判定(攻撃中はFalse)
        self.l = PLAYER_LIFE
        self.is_alive = True
        self.d_img = 0  # ホバリング2種類,攻撃1種類で3種類を切り替える

    def update(self):
        # 移動
        if self.a:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.x -= PLAYER_SPEED
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.x += PLAYER_SPEED
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                self.y -= PLAYER_SPEED
            if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                self.y += PLAYER_SPEED

        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.w)
        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.h)

        # 攻撃
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B)) and self.a:
            Bullet(self.x + PLAYER_WIDTH / 2, self.y)
            pyxel.play(3, 9)
            self.a = False
            self.d_img = 80

    def draw(self):
        if self.a:
            if pyxel.frame_count % self.f == 0:
                if self.d_img == 16:
                    self.d_img = 0
                else:
                    self.d_img = 16
        else:
            if self.i == 0:
                self.d_img = 16
                self.i = PLAYER_MOTION
                self.a = True
            self.i -= 1

        pyxel.blt(
            self.x,
            self.y,
            0,
            self.d_img,
            0,
            self.w,
            self.h,
            12
        )


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.is_alive = True
        bullets.append(self)

    def update(self):
        self.x += BULLET_SPEED
        if self.x + self.w > pyxel.width:  # 画面外に出たら判定を消す
            self.is_alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 96, 0, self.w, self.h, 12)


class Enemy1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.f = ENEMY_FPS
        self.is_alive = True
        self.d_img = 32
        enemies.append(self)

    def update(self):
        self.x -= ENEMY_SPEED
        if (self.x + self.w) < 0:
            self.is_alive = False

    def draw(self):
        if pyxel.frame_count % self.f == 0:
            if self.d_img == 32:
                self.d_img = 48
            else:
                self.d_img = 32
        pyxel.blt(self.x, self.y, 0, self.d_img, 0, self.w, self.h, 12)


class Blast:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLAST_START_RADIUS
        self.is_alive = True
        blasts.append(self)

    def update(self):
        self.radius += 1
        if self.radius > BLAST_END_RADIUS:
            self.is_alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, BLAST_COLOR_IN)
        pyxel.circb(self.x, self.y, self.radius, BLAST_COLOR_OUT)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="じゃがバターシューティング")
        pyxel.load("assets/kirby.pyxres")
        self.score = -10
        self.rate = ENEMY_RATE
        self.rateup = 200
        self.player = Player(0, pyxel.height / 2)
        self.attack = []
        self.is_alive = True
        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]
        self.fruit = [
            (i * 60, pyxel.rndi(0, 104), pyxel.rndi(0, 2), True) for i in range(4)
        ]
        print(self.fruit)
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.frame_count % self.rate == 0:
            Enemy1(pyxel.width, pyxel.rndi(0, pyxel.height - ENEMY_HEIGHT))
        if self.score > self.rateup:
            self.rateup += 200
            self.rate -= 1
            self.rate = max(self.rate, 10)

        for enemy in enemies:  # 敵と弾の当たり判定
            for bullet in bullets:
                if (
                        enemy.x + enemy.w > bullet.x
                        and bullet.x + bullet.w > enemy.x
                        and enemy.y + enemy.h > bullet.y
                        and bullet.y + bullet.h > enemy.y
                ):  # 弾が敵の判定の内部に入ったとき
                    enemy.is_alive = False
                    bullet.is_alive = False
                    blasts.append(
                        Blast(enemy.x + ENEMY_WIDTH / 2, enemy.y + ENEMY_HEIGHT / 2)
                    )
                    pyxel.play(2, 8)
                    self.score += 100

        for enemy in enemies:  # 敵と自機の当たり判定
            if (
                    self.player.x + self.player.w > enemy.x
                    and enemy.x + enemy.w > self.player.x
                    and self.player.y + self.player.h > enemy.y
                    and enemy.y + enemy.h > self.player.y
            ):
                enemy.is_alive = False
                self.player.l -= 1
                pyxel.play(2, 8)
                if self.player.l == 0:
                    blasts.append(
                        Blast(
                            self.player.x + PLAYER_WIDTH / 2,
                            self.player.y + PLAYER_HEIGHT / 2,
                        )
                    )
        if pyxel.frame_count % 100 == 0:
            self.score += 10

        self.player.update()
        update_list(bullets)
        update_list(enemies)
        update_list(blasts)
        cleanup_list(enemies)
        cleanup_list(bullets)
        cleanup_list(blasts)

    def draw(self):
        pyxel.cls(12)

        # Draw sky
        pyxel.blt(0, 88, 0, 0, 88, 160, 32)

        # Draw mountain
        pyxel.blt(0, 88, 0, 0, 64, 160, 24, 12)

        # Draw trees
        offset = pyxel.frame_count % 160
        for i in range(2):
            pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

        # Draw clouds
        offset = (pyxel.frame_count // 16) % 160
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 64, 32, 32, 8, 12)
        offset = (pyxel.frame_count // 8) % 160
        for i in range(2):
            for x, y in self.near_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)

        self.player.draw()
        draw_list(bullets)
        draw_list(enemies)
        draw_list(blasts)

        # Draw score
        s = f"SCORE {self.score:>4}"
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)


App()
