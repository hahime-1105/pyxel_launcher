import pyxel

tile_load = (0, 0)
tile_wall = (1, 0)
tile_step = (2, 0)
tile_stat = (3, 0)
maze_size = 30

dir_up = 0
dir_down = 1
dir_left = 2
dir_right = 3

unit = 2

player_life = 10
key_hold = 10


def isblank(xi, yi, direction):
    ret = False
    if direction == dir_up:
        yi -= 1
    elif direction == dir_down:
        yi += 1
    elif direction == dir_left:
        xi -= 1
    elif direction == dir_right:
        xi += 1
    if pyxel.tilemap(0).pget(xi, yi) != tile_wall:
        ret = True
    return ret


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = maze_size
        self.dir = 1
        self.goal = False

    def update(self):
        # 壁との当たり判定
        if pyxel.btnp(key=pyxel.KEY_UP, hold=key_hold, repeat=key_hold):
            self.dir = 0
            if isblank(self.x, self.y, self.dir):
                self.y -= 1
        elif pyxel.btnp(key=pyxel.KEY_LEFT, hold=key_hold, repeat=key_hold):
            self.dir = 2
            if isblank(self.x, self.y, self.dir):
                self.x -= 1

        if pyxel.btnp(key=pyxel.KEY_DOWN, hold=key_hold, repeat=key_hold):
            self.dir = 1
            if isblank(self.x, self.y, self.dir):
                self.y += 1
        elif pyxel.btnp(key=pyxel.KEY_RIGHT, hold=key_hold, repeat=key_hold):
            self.dir = 3
            if isblank(self.x, self.y, self.dir):
                self.x += 1

    def draw(self, d_x, d_y):
        pyxel.blt((self.x * 8) - d_x, (self.y * 8) - d_y, 0, 0, 8, 8, 8, 7)


class Stage:
    def __init__(self):
        self.size = maze_size
        self.load = tile_load
        self.wall = tile_wall
        self.step = tile_step
        self.start = tile_stat
        pyxel.tilemap(0).imgsrc = 0
        self.unit = unit

    def initmaze(self):
        for yi in range(self.size):
            for xi in range(self.size):
                pyxel.tilemap(0).pset(xi, yi, self.load)

    def makemaze(self):
        self.initmaze()

        # 外周を作成
        for yi in range(self.size + 1):
            pyxel.tilemap(0).pset(0, yi, self.wall)
            pyxel.tilemap(0).pset(self.size, yi, self.wall)
            if yi == 0 or yi == self.size:
                for xi in range(1, self.size):
                    pyxel.tilemap(0).pset(xi, yi, self.wall)

        # 迷路を作成(棒倒し法)
        for yi in range(self.unit, self.size, self.unit):
            for xi in range(self.unit, self.size, self.unit):
                pyxel.tilemap(0).pset(xi, yi, self.wall)

                # 棒倒しの向き
                if yi == self.unit:
                    diff = [pyxel.rndf(-1, 1), pyxel.rndf(-1, 1)]
                else:
                    diff = [pyxel.rndf(-1, 1), pyxel.rndf(0, 1)]
                if abs(diff[0]) >= abs(diff[1]):
                    diff[0] = int((self.unit) * (diff[0] / abs(diff[0])))
                    diff[1] = 0
                else:
                    diff[0] = 0
                    diff[1] = int((self.unit) * (diff[1] / abs(diff[1])))

                # 棒を倒す
                if diff[1] == 0:
                    for dx in range(0, diff[0], int((diff[0] / abs(diff[0])))):
                        pyxel.tilemap(0).pset(xi + dx, yi, self.wall)
                else:
                    for dy in range(0, diff[1], int((diff[1] / abs(diff[1])))):
                        pyxel.tilemap(0).pset(xi, yi + dy, self.wall)
        sx, sy, gx, gy = self.set_root()
        return sx, sy, gx, gy

    # スタートとゴール設定
    def set_root(self):
        while True:
            goal_x = pyxel.rndi(1, self.size - 1)
            goal_y = pyxel.rndi(1, self.size - 1)
            start_x = pyxel.rndi(1, self.size - 1)
            start_y = pyxel.rndi(1, self.size - 1)
            if (
                    pyxel.tilemap(0).pget(goal_x, goal_y) == self.load and
                    pyxel.tilemap(0).pget(start_x, start_y) == self.load and
                    abs(goal_x - start_x) > 5 and
                    abs(goal_y - start_y) > 5 and
                    (((goal_x - start_x) * (goal_x - start_x)) + ((goal_y - start_y) * (goal_y - start_y))) > 225
            ):
                break
        pyxel.tilemap(0).pset(goal_x, goal_y, self.step)
        pyxel.tilemap(0).pset(start_x, start_y, self.start)
        return start_x, start_y, goal_x, goal_y

    def update(self):
        pass

    def draw(self, scroll_x, scroll_y):
        pyxel.cls(7)
        pyxel.bltm(0, 0, 0, scroll_x, scroll_y, pyxel.width, pyxel.height, 7)


class App:
    def __init__(self):
        pyxel.init(150, 150, title='カービィのフシギなダンジョン')
        pyxel.load('assets/rogue_like.pyxres')
        self.scene = 1
        self.floor = 1
        self.stg = Stage()
        self.player = Player()
        self.p_draw_x = 0
        self.p_draw_y = 0
        self.gx = 10
        self.gy = 10
        self.scroll_x = 0
        self.scroll_y = 0
        self.width = (maze_size + 1) * 8
        self.height = (maze_size + 1) * 8
        self.ui_border_x = 96
        self.ui_border_y = 96

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE):
            sx, sy, gx, gy = self.stg.makemaze()
            self.player.x = sx
            self.player.y = sy
            self.gx = gx
            self.gy = gy
        self.player.update()

        # ゴール時に次のフロアに進む
        if (
                self.player.x == self.gx and
                self.player.y == self.gy
        ):
            sx, sy, gx, gy = self.stg.makemaze()
            self.player.x = sx
            self.player.y = sy
            self.gx = gx
            self.gy = gy
            self.floor += 1

        # スクロール
        self.scroll_x = max((self.player.x * 8) - 40, 0)
        if self.scroll_x > (self.width - self.ui_border_x):
            self.scroll_x = self.width - self.ui_border_x
        self.scroll_y = max((self.player.y * 8) - 40, 0)
        if self.scroll_y > (self.height - self.ui_border_y):
            self.scroll_y = self.height - self.ui_border_y

    def draw(self):
        pyxel.camera()
        self.stg.draw(scroll_x=self.scroll_x, scroll_y=self.scroll_y)
        self.player.draw(self.scroll_x, self.scroll_y)
        pyxel.camera(self.scroll_x, self.scroll_y)
        self.draw_ui()

    def draw_ui(self):
        pyxel.rect(self.ui_border_x + self.scroll_x, self.scroll_y, self.width - self.ui_border_x, self.height, 0)
        pyxel.rect(self.scroll_x, self.ui_border_y + self.scroll_y, self.width, self.height - self.ui_border_y, 0)
        pyxel.text(self.ui_border_x + self.scroll_x, self.scroll_y + 8, 'FLOOR %s' % self.floor, 7)


App()
