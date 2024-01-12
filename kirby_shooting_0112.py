import pyxel

PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
PLAYER_SPEED = 2
PLAYER_LIFE = 5
PLAYER_FPS = 5
PLAYER_MOTION = 10
PLAYER_DAMAGE = 30

BULLET_WIDTH = 12
BULLET_HEIGHT = 12
BULLET_SPEED = 4

ENEMY_WIDTH = 16
ENEMY_HEIGHT = 16
ENEMY_SPEED = 2
ENEMY_FPS = 4
ENEMY_RATE = 30  # 敵の出現間隔

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

bullets = []
enemies = []
blasts = []
enemies_2 = []


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
        self.inv = False
        self.damage = PLAYER_DAMAGE
        self.d_img = 0  # ホバリング2種類,攻撃1種類で3種類を切り替える

    def update(self):
        if self.is_alive:
            self.update_game()
        else:
            self.update_gamaover()

    def update_game(self):
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

    def update_gamaover(self):
        self.damage -= 1
        if self.damage < 0:
            self.y += 1

    def draw(self):
        if self.is_alive:
            self.draw_game()
        else:
            self.draw_gameover()

    def draw_game(self):
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
        if self.inv:  # 被弾
            frame = pyxel.frame_count % 2
            if frame == 0:
                pyxel.pal(8, 2)
                pyxel.pal(14, 13)
            elif frame == 1:
                pyxel.pal()
            if self.damage == 0:
                self.inv = False
                self.damage = PLAYER_DAMAGE
                pyxel.pal()
                pyxel.clip()
            self.damage -= 1

    def draw_gameover(self):
        if self.damage > 0:
            pyxel.blt(self.x, self.y, 0, 160, 0, self.w, self.h, 12)
        elif (pyxel.frame_count // 5) % 4 == 0:
            pyxel.blt(self.x, self.y, 0, 160, 0, self.w, self.h, 12)
        elif (pyxel.frame_count // 5) % 4 == 1:
            pyxel.blt(self.x, self.y, 0, 176, 0, -self.w, self.h, 12)
        elif (pyxel.frame_count // 5) % 4 == 2:
            pyxel.blt(self.x, self.y, 0, 176, 0, self.w, self.h, 12)
        elif (pyxel.frame_count // 5) % 4 == 3:
            pyxel.blt(self.x, self.y, 0, 160, 0, -self.w, self.h, 12)


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
        pyxel.blt(self.x, self.y, 0, 64, 0, self.w, self.h, 12)


class Enemy1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.f = ENEMY_FPS
        self.f_ini = pyxel.rndi(0, self.f)
        self.is_alive = True
        self.hover = pyxel.rndi(15, 35)
        self.initial = pyxel.rndi(1, self.hover * 2)
        self.d_img = 32
        enemies.append(self)

    def update(self):
        self.x -= ENEMY_SPEED
        y_move = (pyxel.frame_count + self.initial) % (self.hover * 2)
        if y_move > self.hover + (self.hover // 2):
            self.y += ENEMY_SPEED / 2
        elif y_move > self.hover:
            self.y += ENEMY_SPEED
        elif y_move > self.hover // 2:
            self.y -= ENEMY_SPEED / 2
        else:
            self.y -= ENEMY_SPEED
        if (self.x + self.w) < 0:
            self.is_alive = False

    def draw(self):
        if (pyxel.frame_count + self.f_ini) % self.f == 0:
            if self.d_img == 32:
                self.d_img = 48
            else:
                self.d_img = 32
        pyxel.blt(self.x, self.y, 0, self.d_img, 0, self.w, self.h, 12)


class Enemy2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.f = ENEMY_FPS
        self.f_ini = pyxel.rndi(0, self.f)
        self.is_alive = True
        self.d_img = 32
        enemies_2.append(self)

    def update(self):
        self.x -= ENEMY_SPEED
        if (self.x + self.w) < 0:
            self.is_alive = False

    def draw(self):
        if (pyxel.frame_count + self.f_ini) % self.f == 0:
            if self.d_img == 128:
                self.d_img = 144
            else:
                self.d_img = 128
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
        pyxel.load("assets/kirby_0110.pyxres")
        self.score = -10
        self.rate = ENEMY_RATE
        self.rateup = 150
        self.player = Player(10, pyxel.height / 2)
        self.attack = []
        self.is_alive = True
        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.player.is_alive:
            self.update_play()
        else:
            self.player.update()
            if self.player.damage == 0:
                pyxel.playm(1, loop=False)

    def update_play(self):

        if pyxel.frame_count % self.rate == 0:  # 敵を生成
            symbol = pyxel.rndi(1, 4)
            if symbol == 1:
                Enemy2(pyxel.width, pyxel.rndi(0, pyxel.height - ENEMY_HEIGHT))
            else:
                Enemy1(pyxel.width, pyxel.rndi(15, pyxel.height - ENEMY_HEIGHT - 15))
        if self.score > self.rateup:  # スコアに変動して敵が多くなる
            self.rateup += 150
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
                    self.score += 50

        for enemy2 in enemies_2:  # 敵と弾の当たり判定
            for bullet in bullets:
                if (
                        enemy2.x + enemy2.w > bullet.x
                        and bullet.x + bullet.w > enemy2.x
                        and enemy2.y + enemy2.h > bullet.y
                        and bullet.y + bullet.h > enemy2.y
                ):  # 弾が敵の判定の内部に入ったとき
                    bullet.is_alive = False

        if not self.player.inv:
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
                    self.player.inv = True

                    if self.player.l == 0:
                        self.player.is_alive = False
                        pyxel.stop()

            for enemy2 in enemies_2:  # 障害物と自機の当たり判定
                if (
                        self.player.x + self.player.w > enemy2.x
                        and enemy2.x + enemy2.w > self.player.x
                        and self.player.y + self.player.h > enemy2.y
                        and enemy2.y + enemy2.h > self.player.y
                ):
                    self.player.l -= 1
                    pyxel.play(2, 8)
                    self.player.inv = True

                    if self.player.l == 0:
                        self.player.is_alive = False
                        pyxel.stop

        if pyxel.frame_count % 100 == 0:
            self.score += 10

        self.player.update()
        update_list(bullets)
        update_list(enemies)
        update_list(blasts)
        update_list(enemies_2)
        cleanup_list(enemies)
        cleanup_list(bullets)
        cleanup_list(blasts)
        cleanup_list(enemies_2)

    def draw(self):
        pyxel.cls(12)
        if self.player.is_alive:
            self.draw_game()
        else:
            self.draw_gameover()

    def draw_game(self):

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
        draw_list(enemies_2)

        # Draw score
        s = f"SCORE {self.score:>4}"
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)
        for i in range(PLAYER_LIFE):
            if self.player.l > i:
                pyxel.blt(100 + (i * 9), 2, 0, 112, 0, 8, 8, 12)
            else:
                pyxel.blt(100 + (i * 9), 2, 0, 120, 0, 8, 8, 12)

    def draw_gameover(self):
        self.player.draw()
        s = f"SCORE {self.score:>4}"
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)
        for i in range(PLAYER_LIFE):
            if self.player.l > i:
                pyxel.blt(100 + (i * 9), 2, 0, 112, 0, 8, 8, 12)
            else:
                pyxel.blt(100 + (i * 9), 2, 0, 120, 0, 8, 8, 12)


App()
