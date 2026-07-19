# this will be good
import pygame,sys
import random

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.width = 20
        self.height = 20
        self.gravity = 0.8
        self.velocity_y = 0
        self.direct = ""
        
    def down(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

    def up(self):
        self.velocity_y = -12

    def collison(self):
        for p in game.list:
            if self.x + self.width >= p.x and self.x < p.x + p.width:
                if self.y < p.h1 or self.y + self.height > p.h1 + p.gap:
                    self.x = 100
                    self.y = 300
                    self.velocity_y = 0
                    return True
            if self.y <= 0 or self.y + self.height > game.height:
                self.x = 100
                self.y = 300
                self.velocity_y = 0
                return True
        

            
            

        
  


    def draw(self):
        pygame.draw.rect(game.screen,(255,255,255),(self.x,self.y,self.width,self.height))



class Pipe:
    def __init__(self):
        self.x = 810
        self.y = 0
        self.gap = 150
        self.speed = 5
        self.width = 60
        self.h1 = random.randint(50,400)
        self.h2 = 600 - self.h1 - self.gap
        self.scored = False
    
    
    
    
    def update(self):


         
        pass

    

        
    

    def move(self):
        self.x -= self.speed

    def draw(self):
        
        b_y = self.y+self.h1+self.gap
        

        pygame.draw.rect(game.screen,(255,0,0),(self.x,self.y,self.width,self.h1)) # top 

        pygame.draw.rect(game.screen,(255,0,0),(self.x,b_y,self.width,self.h2)) # bottom 
        
        
    












class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.score = 0 
        self.font = pygame.font.Font(None,36)
        

        self.list = []
        self.spawn_timer = 0

        self.width = 800
        self.height = 600 
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("best")

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()

    def update(self):
        bird.down()
        



        if bird.collison() == True:
            self.list.clear()
            self.score = 0 


        self.spawn_timer += 1

        if self.spawn_timer >= 60:
            self.list.append(Pipe())
            
            self.spawn_timer = 0

        for i in self.list:

            i.move()
        
        for p in game.list:
            if p.x + p.width < bird.x and p.scored == False:
                self.score += 1
                p.scored = True
    
        
        new_list = []
        for p in self.list:
            if p.x > -p.width:
                new_list.append(p)
            
        self.list = new_list
        
        

        
            
        

        

                             # later game logic goes here

    def draw(self):
        self.screen.fill((30, 30, 30))
        score_text = self.font.render(f"Score::{self.score}",True,(255,255,255))  
        self.screen.blit(score_text,(10,10))# dark background
        bird.draw()
        for i in self.list:
            i.draw()
            



if __name__ == "__main__":
    bird = Bird()
    game = Game()
    game.run()