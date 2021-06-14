import pygame
from pygame.constants import QUIT
import random


pygame.init()
black=(0,0,0)
blue =(0,0,255)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
width=1240
height=620
ggreen=(134,205,50)
Clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Skarsh Snake Game")
pygame.display.update()

grass2=pygame.image.load(r"grass2.jpg")
grass2=pygame.transform.scale(grass2,(1260,650))

font = pygame.font.SysFont(None, 55)


bg=pygame.image.load("bg.jpg")
bg=pygame.transform.scale(bg,(1260,650))
grass=pygame.image.load("grass.jpg")
grass=pygame.transform.scale(grass,(1260,650))



def msg(size,message,x_pos,y_pos,color):
    font=pygame.font.SysFont(None,size)
    render=font.render(message,True,color)
    screen.blit(render , (x_pos,y_pos))
def gameplay(speed_v):
    
    score=0
    size=37
    x=100
    y=200
    fps=30
    x_apple = random.randint(20, width/2)
    y_apple = random.randint(20, height/2)
    #speed_v = 7
    x_speed=0
    y_speed=0
    list = []
    apple=pygame.image.load(r"ap.png")
    apple=pygame.transform.scale(apple,(75,50))
    s_length= 1
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    back=pygame.image.load(r"back.png")  #button png image
    back=pygame.transform.scale(back,(50,50))
    game=False 
    over=False
    while game==False:
        if over:
            screen.blit(grass2,(0,0))
            screen.blit(back,(45,10))
            msg(75,"Game Over!  Press \"Enter\" To Restart", 200, 250,blue)
            
            
                 
       
    
            for event in pygame.event.get():
                mouse=pygame.mouse.get_pos()
                click=pygame.mouse.get_pressed()
                if event.type==pygame.QUIT:
                    game=True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameplay(speed_v)

                if 50<mouse[0]<100 and 10<mouse[1]<50:
                    back=pygame.transform.scale(back,(65,65))
                    screen.blit(back,(45,10))
                    if click[0]==1:
                        level()
                
        else:                
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        x_speed = speed_v
                        y_speed = 0

                    if event.key == pygame.K_LEFT:
                        x_speed = - speed_v
                        y_speed = 0

                    if event.key == pygame.K_UP:
                        y_speed = - speed_v
                        x_speed = 0

                    if event.key == pygame.K_DOWN:
                        y_speed = speed_v
                        x_speed = 0

            x = x + x_speed
            y = y + y_speed

            if abs(x - x_apple)<18 and abs(y - y_apple)<18:
                score +=1
                x_apple = random.randint(20, width / 2)
                y_apple = random.randint(20, height / 2)
                s_length +=5
            screen.blit(grass2,(0,0))
            screen.blit(apple,(x_apple,y_apple))
            msg(60,"Points:" + str(score * 10), 1000, 8,red)    
        #pygame.draw.rect(screen, red, [x_apple, y_apple, size, size])


            head = []
            head.append(x)
            head.append(y)
            list.append(head)

            if len(list)>s_length:
                del list[0]
            if head in list[:-1]:
                over = True

            if x<0 or x>width or y<0 or y>height:
                over = True

        
            snake_length(screen, blue, list, size)
        pygame.display.update()
        Clock.tick(fps)

    pygame.QUIT()
    quit()
     
    
def level():    #all buttons 
    back=pygame.image.load(r"back.png")  #button png image
    back=pygame.transform.scale(back,(50,50))
    level_game=False
    while level_game==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                level_game=True

            grass2=pygame.image.load("grass2.jpg")
            grass2=pygame.transform.scale(grass2,(1289,605))
            screen.blit(bg,(0,0))
            level1=pygame.image.load("level1.png")  #button png image
            level2=pygame.image.load("level2.png")  #button png image
            level3=pygame.image.load("level3.png")  #button png image
            level4=pygame.image.load("level4.png")
            level5=pygame.image.load("level5.png")  #button png image
            level6=pygame.image.load("level6.png")
            level1=pygame.transform.scale(level1,(180,180))
            level2=pygame.transform.scale(level2,(180,180))
            level3=pygame.transform.scale(level3,(180,180))
            level4=pygame.transform.scale(level4,(180,180))
            level5=pygame.transform.scale(level5,(180,180))
            level6=pygame.transform.scale(level6,(180,180))
    
            screen.blit(level1,(60,170))
            screen.blit(level2,(260,170))
            screen.blit(level3,(460,170))
            screen.blit(level4,(660,170))
            screen.blit(level5,(860,170))
            screen.blit(level6,(1060,170))
            screen.blit(back,(45,10))
    
    
    #msg(100,"PLAY",565,346,white)
    #msg(100,   "QUIT",565,500,white)
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
    
            if 60<mouse[0]<250 and 170<mouse[1]<370:
                level1=pygame.transform.scale(level1,(200,200))
                screen.blit(level1,(50,160))   
                if click[0]==1:
                    gameplay(speed_v=6)

            if 260<mouse[0]<450 and 170<mouse[1]<370:
                level2=pygame.transform.scale(level2,(200,200))
                screen.blit(level2,(250,160))   
                if click[0]==1:
                    gameplay(speed_v=7)
                
            
                
    
            if 460<mouse[0]<650 and 170<mouse[1]<370:
                level3=pygame.transform.scale(level3,(200,200))
                screen.blit(level3,(450,160))
                if click[0]==1:
                    gameplay(speed_v=9)


            
            if 660<mouse[0]<850 and 170<mouse[1]<370:
                level4=pygame.transform.scale(level4,(200,200))
                screen.blit(level4,(650,160))
                if click[0]==1:
                    gameplay(speed_v=10)
                
                
            if 860<mouse[0]<1050 and 170<mouse[1]<370:
                level5=pygame.transform.scale(level5,(200,200))
                screen.blit(level5,(850,160))
                if click[0]==1:
                    gameplay(speed_v=12)

            if 1060<mouse[0]<1250 and 170<mouse[1]<370:
                level6=pygame.transform.scale(level6,(200,200))
                screen.blit(level6,(1050,160))
                if click[0]==1:
                    gameplay(speed_v=13)

            
            if 50<mouse[0]<100 and 10<mouse[1]<50:
                back=pygame.transform.scale(back,(65,65))
                screen.blit(back,(45,10))
                if click[0]==1:
                    start_display()
                

                
    #msg(100,message,x_pos,y_pos,white)
                
        pygame.display.update()
    pygame.QUIT()
    quit()
     



def snake_length(screen, color, list, size):
    for x,y in list:
        pygame.draw.rect(screen, color, [x, y, size, size])
    
    
def buttons():    #all buttons 
    
    P_button=pygame.image.load(r"PLAY.png")  #button png image
    Q_button=pygame.image.load(r"QUIT.png")  #button png image
    P_button=pygame.transform.scale(P_button,(450,150))
    Q_button=pygame.transform.scale(Q_button,(450,150))
    Font=pygame.font.SysFont('timesnewroman',160)
    snake_msg=Font.render("Snake Game",True,ggreen)
    screen.blit(snake_msg,(270,100))
    
    screen.blit(P_button,(420,300))
    screen.blit(Q_button,(420,450))
    #msg(190,"Snake Game",220,95,ggreen)
    #msg(100,"PLAY",565,346,white)
    #msg(100,"QUIT",565,500,white)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if 500<mouse[0]<780 and 320<mouse[1]<480:
        P_button=pygame.transform.scale(P_button,(540,190))
        screen.blit(P_button,(380,280))
        if click[0]==1:
            level()

    if 500<mouse[0]<780 and 470<mouse[1]<580:
        Q_button=pygame.transform.scale(Q_button,(540,190))
        screen.blit(Q_button,(380,430))
        if click[0]==1:
            
            pygame.QUIT()
            quit()
    #msg(100,message,x_pos,y_pos,white)
    

    
pygame.display.update()
def snake_length(screen, color, list,size):
    for x,y in list:
        pygame.draw.rect(screen, color, [x, y, size, size])



def start_display():
    intro=False
    while intro == False:
        screen.blit(grass,(0,0))
        buttons()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        pygame.display.update()

        
        
start_display()


pygame.quit()
