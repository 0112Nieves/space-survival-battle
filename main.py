import pygame

FPS = 60

WIDTH = 500
HEIGHT = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 遊戲初始化 & 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space survival battle")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

# 遊戲迴圈
while running:
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 更新遊戲
    all_sprites.update()
    
    # 畫面顯示
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
    
pygame.quit()