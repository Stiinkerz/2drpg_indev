import time

import pygame

from player import Player


class Game:

    def __init__(self):
        self.player = Player(500, 400)
        self.idleState = False
        self.clock = None
        self.screen = pygame.display.set_mode((1000, 800))
        self.game = True
        self.image_font = pygame.transform.scale(pygame.image.load("assets/image/fond.jpg"), (1000, 800))
        self.i = 0

    def run(self):
        self.clock = pygame.time.Clock()

        while self.game:
            key_pressed = pygame.key.get_pressed()

            self.screen.blit(self.image_font, (0, 0))
            if self.player.state == "runLeft":
                self.screen.blit(
                    pygame.transform.flip(self.player.allimg[self.player.state][round(self.player.i)], True, False),
                    self.player.position)
            elif self.player.state == "climbDown":
                self.screen.blit(
                    pygame.transform.flip(self.player.allimg[self.player.state][round(self.player.i)], False, True),
                    self.player.position)
            elif self.player.state == "idleLeft":
                self.screen.blit(
                    pygame.transform.flip(self.player.allimg[self.player.state][round(self.player.i)], True, False),
                    self.player.position)
            elif self.player.state == "idle":
                self.screen.blit(self.player.allimg[self.player.state][round(self.player.i)], self.player.position)
            else:
                self.screen.blit(self.player.allimg[self.player.state][round(self.player.i)], self.player.position)
                if self.player.state == "attack1" and round(self.player.i) == len(self.player.allimg["attack1"]) - 1:
                    self.player.state = "idle"
                elif self.player.state == "attack2" and round(self.player.i) == len(self.player.allimg["attack2"]) - 1:
                    self.player.state = "idle"
                elif self.player.state == "attack3" and round(self.player.i) == len(self.player.allimg["attack3"]) - 1:
                    self.player.state = "idle"
                elif self.player.state == "punch" and round(self.player.i) == len(self.player.allimg["punch"]) - 1:
                    self.player.state = "idle"
                elif self.player.state == "runAttack" and round(self.player.i) == len(self.player.allimg["runAttack"]) - 1:
                    self.player.state = "idle"
                elif self.player.state == "runAttack":
                    self.player.position[0] += 4
            if self.player.i < len(self.player.allimg[self.player.state]) - 1:
                self.player.i += 0.15
            else:
                self.player.i = 0

            self.player.control(key_pressed)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game = False
                    else:
                        pass
            pygame.display.update()
            pygame.display.flip()
            pygame.event.pump()
            self.clock.tick(60)
