import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.idleState = None
        self.state = "idle"
        self.position = [float(x), float(y)]
        self.player_idle = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_idle.png"), (384, 96))
        self.player_run = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_run.png"), (576, 96))
        self.player_attack1 = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_attack1.png"), (576, 96))
        self.player_attack2 = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_attack2.png"), (768, 96))
        self.player_attack3 = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_attack3.png"), (768, 96))
        self.player_runAttack = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_run_attack.png"), (576, 96))
        self.player_jump = pygame.image.load("assets/sprite/2 Punk/Punk_jump.png")
        self.player_doublejump = pygame.image.load("assets/sprite/2 Punk/Punk_doublejump.png")
        self.player_death = pygame.image.load("assets/sprite/2 Punk/Punk_death.png")
        self.player_climb = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_climb.png"), (576, 96))
        self.player_punch = pygame.transform.scale(pygame.image.load("assets/sprite/2 Punk/Punk_punch.png"), (576, 96))
        self.allimg = {
            "idle": [self.player_idle.subsurface((i*96, 0, 96, 96)) for i in range(4)],
            "idleLeft": [self.player_idle.subsurface((i*96, 0, 96, 96)) for i in range(4)],
            "runRight": [self.player_run.subsurface((i*96, 0, 96, 96)) for i in range(6)],
            "runLeft": [self.player_run.subsurface((i * 96, 0, 96, 96)) for i in range(6)],
            "climb":[self.player_climb.subsurface((i * 96, 0, 96, 96)) for i in range(6)],
            "climbDown":[self.player_climb.subsurface((i * 96, 0, 96, 96)) for i in range(6)],
            "punch": [self.player_punch.subsurface((i * 96, 0, 96, 96)) for i in range(6)],
            "attack1":[self.player_attack1.subsurface((i * 96, 0, 96, 96)) for i in range(6)],
            "attack2": [self.player_attack2.subsurface((i * 96, 0, 96, 96)) for i in range(8)],
            "attack3": [self.player_attack3.subsurface((i * 96, 0, 96, 96)) for i in range(8)],
            "runAttack": [self.player_runAttack.subsurface((i * 96, 0, 96, 96)) for i in range(6)]
        }
        self.i = 0

    def control(self, key_pressed):
        if key_pressed[pygame.K_UP]:
            print(self.idleState)
            self.position[1] -= 4
            self.state = "climb"
            self.idleState = True
        elif key_pressed[pygame.K_DOWN]:
            print(self.idleState)
            self.position[1] += 4
            self.state = "climb"
            self.idleState = True
        elif key_pressed[pygame.K_LEFT]:
            print(self.idleState)
            self.position[0] -= 4
            if self.state == "runRight" or self.state == 'idle':
                self.position[0] -= 48
            self.state = "runLeft"
            self.idleState = True
        elif key_pressed[pygame.K_RIGHT]:
            print(self.idleState)
            self.position[0] += 4
            if self.state == "runLeft" or self.state == "idleLeft":
                self.position[0] += 48
            self.state = "runRight"
            self.idleState = True
        elif key_pressed[pygame.K_w]:
            self.state = "punch"
            self.i = 0
        elif key_pressed[pygame.K_x]:
            self.state = "attack1"
            self.i = 0
        elif key_pressed[pygame.K_c]:
            self.state = "attack2"
            self.i = 0
        elif key_pressed[pygame.K_v]:
            self.state = "attack3"
            self.i = 0
        elif key_pressed[pygame.K_b]:
            self.state = "runAttack"
            self.i = 0
        else:
            if self.state == "runLeft":
                self.state = "idleLeft"
                self.i = 0
            elif self.state == "runRight":
                self.state = "idle"
                self.i = 0
            if self.idleState:
                i = 0
                self.idleState = False





