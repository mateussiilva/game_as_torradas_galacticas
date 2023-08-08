from pygame.sprite import Sprite
from pygame.image import load
from random import randint

class Inimigo(Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = load("images/inimigo_1.png")
        self.velocidade = 1
        self.rect = self.image.get_rect(
            center=(800,300)
        )

    def update(self):
        if self.rect.x <= 10:
            self.rect.x = randint(400,800)
            self.rect.y = randint(100,600)
                
        self.rect.x -= self.velocidade

# if __name__ == "__main__":
#     from pygame.sprite import Sprite
#     from pygame.image import load
#     from random import randint
