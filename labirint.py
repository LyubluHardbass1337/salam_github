from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

win_width = 700
win_height = 500
display.set_caption('Лабиринт')
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)

w1 = GameSprite('platform_h.png', win_width / 2 - win_height / 2, 300, 100, 30)
w2 = GameSprite('platform_v.png', 370, 100, 30, 100)

packman = Player('hero.png', 5, win_height - 80, 80, 80, 0, 0)

barriers = sprite.Group(w1, w2)
monster = GameSprite('cyborg.png', 600, win_height - 80, 80, 80)
final_sprite = GameSprite('treasure.png', win_width - 80, win_height - 80, 80, 80)

finish = False

while not finish:
    for e in event.get():
        if e.type == QUIT:
            finish = True
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0

    packman.update()

    if sprite.collide_rect(packman, monster):
        finish = True
        img = image.load('game-over_1.jpg')
        d = img.get_width() // img.get_height()
        window.fill((255, 225, 225))
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

    if sprite.collide_rect(packman, final_sprite):
        finish = True
        img = image.load('thumb.jpg')
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

    window.fill(back)
    barriers.draw(window)
    monster.reset(window)
    final_sprite.reset(window)
    packman.reset(window)

    display.update()
    time.delay(50)

quit()
``


