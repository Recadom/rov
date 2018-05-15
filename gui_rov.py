import time, os
import pygame
#import serial
from pygame.locals import *
from filedit import File_Name

global first_time

#Const
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (173,255,47)
BLUE = (0, 0, 255)
PEACH_1 = (205,175,149)
PEACH_2 = (255,218,185)
YELLOW = (255,255,0)
ORANGE = (218,165,32)
GRAY = (190,190,190)
LIGHT_GRAY = (211,211,211)
LIGHT_BLUE = (135,206,250)
DARK_GREY = (105,105,105)

#inits
pygame.init()
#pygame.joystick.init()
#joystick = pygame.joystick.Joystick(0)
#joystick.init()

WIDTH = 1021
HEIGHT = 510
Baudrate = 9600
FPS = 15

#Screen
pygame.display.set_caption('ROV GUI')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((WIDTH,HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)

'''
    class seri(object): # OLD
    
    def __init__(self): # To make anything global to all functions / Also, for usb connection, use '/dev/ttyUSB1' instead of /dev/ttyAMA0 which is for rx and tx pins! Try:  /dev/ttyS1 or  /dev/ttyS2
        self.ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout=1
                                 )
            self.ser.close()
            self.ser.open()

    def read(self): # Reads the data
    #       if ser.inWaiting() > 0:
    #            data = ser.read()
    #            return data
        return self.ser.read()
    
    def close(self): # To close program
        self.ser.close()
'''

'''
class uart(object): #rate is usually 9600
    
    def __init__(self,rate):
        self.ser = serial.Serial('/dev/ttyAMA0')
        self.ser.baudrate(rate)
    
    def read(self, FPS, FPS_tic, seconds_wait): #Returns the main value, if nothing is being read, it returns False
        v = FPS * seconds_wait
        FPS_tic += 1
        if int(v) == int(FPS_tic):
            FPS_tic = 0
            return FPS_tic, slef.ser.readline()
        else:
            return FPS_tic, False
'''

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,player_img_1):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img_1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self,n,s,clear=False,x=0,y=0,where = False):
        self.rect.y += n
        self.rect.x += s
        if clear == True: self.rect.center = (x, y)
        elif self.rect.top > HEIGHT or self.rect.bottom < 0 : self.rect.y = 0
        elif self.rect.right > WIDTH/2.2 or self.rect.left < 0: self.rect.x = WIDTH/4
        if where == True:
            return self.rect.x, self.rect.y


def message_display(s,text,x,y): #freesansbold.ttf
    largeText = pygame.font.Font('freesansbold.ttf',s)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

def message_display_l(s,text,x,y): #freesansbold.ttf
    largeText = pygame.font.Font('freesansbold.ttf',s)
    TextSurf, TextRect = text_objects(text, largeText) #max is (655)
    TextRect = (x,y)
    screen.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def buttons(s,msg,x,y,w,h,ic,ac,number_1,action = None,action_1 = None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if action_1 != None:
            action_1()
        if action != None and click[0] == 1:
            cooldown = 0
            return cooldown,action(number_1)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",s)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def button_for_tasks(cooldown,s,msg,x,y,w,h,ic,ac,number_1,number_3,number_4,number_5,action = None,action_1 = None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if cooldown < 10: cooldown += 1
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if action_1 != None: action_1(number_4,number_5)
        if action != None and click[0] == 1 and cooldown > 9:
            cooldown = 0
            action(number_1,number_3)
            return cooldown
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",s)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    return cooldown


#In game functions below!!!!

def finished_function(time,color_list):
    if color_list[time] == (0, 255, 0):
        color_list[time] = (255, 0, 0)
    elif color_list[time] == (255, 0, 0):
        color_list[time] = (0, 255, 0)

def task_dicfun(tasks_dic,color_list): #use this for gathering the tasks names and duties.
    for (i,n),(o,m) in zip((sorted(tasks_dic.items())),color_list.items()):
        if m == (255, 0, 0):
            v = list(i)
            kim = "".join(v[-3:-1])
            try:
                try: #Two digit
                    kim = "".join(v[-3:-1])
                    yield i,n,m,int(kim)
                
                except: #One digit
                    kim = "".join(v[-2])
                    yield i,n,m,int(kim)
            except:
                print('Faulty point system in tasks, take a look at the list!')
                yield i,n,m,0
        
        else:
            yield i,n,m,0

def task_area(difer,start_space,amount_tasks): #use this for gathering the tasks names and duties.
    for i in int(amount_tasks):
        n = start_space
        start_space += difer
        return int(n)

def task_discription(name_task,disc_task): #Displays task
    message_display(15,name_task,WIDTH/3.4,HEIGHT/27) #title

    task_1 = list(disc_task)
    line_1 = task_1[0:100]
    line_2 = task_1[100:200]
    line_3 = task_1[200:300]
    
    
    message_display_l(13,"".join(line_1),WIDTH/5.5,HEIGHT/16)
    
    message_display_l(13,"".join(line_2),WIDTH/5.5,HEIGHT/11)
    
    message_display_l(13,"".join(line_3),WIDTH/5.5,HEIGHT/8)


#Gets self location of the tasks and grabs the data
folder = os.path.dirname(__file__)
tasks_1 = File_Name('Tasks',folder)
tasks = tasks_1.all_data()
amount_tasks = 0
amount_var = 0
tasks_dic = {}
color_list = {}
for i in tasks:
    if amount_tasks % 2 == 0 or (amount_tasks+1) % 2 == 0:
        z = i
    else:
        tasks_dic[str(z)] = str(i)
        color_list[amount_var] = GREEN
        amount_var += 1
    amount_tasks += 0.5

#Check if tasks are okay
if amount_tasks % 2 != 0.0 and (amount_tasks+1) % 2 != 0.0:
    print('Problem with the tasks list file, take a look at the ratio.')
    print('Closing...')
    pygame.quit()
    quit()

difer = (HEIGHT - (HEIGHT/18))/amount_tasks
start_space = HEIGHT/18

#constants in running pygame
axis_forward_back = 1
axis_left_right = 0
axis_up_down = 2
axis_twist = 3

run = True
seconds_wait = 1 #Amount of seconds to wait untill you grab the next data.
forwLeft = 100 #delete soon
reset_start_space = start_space
task_color = GREEN
task_state = True
click_color = LIGHT_GRAY
#seri = uart(Baudrate)
cooldown = 9
first_time = True

while run:
    
    clock.tick(FPS)
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
    
    #FPS_tic, ser_data = seri.read(FPS, FPS_tic, seconds_wait)


    screen.fill(LIGHT_BLUE)

    '''
    forwLeft = joystick.get_axis(axis_forward_back) * 100
    forwRight = joystick.get_axis(axis_forward_back) * 100
    vertLeft = joystick.get_axis(axis_up_down) * 100
    vertRight = joystick.get_axis(axis_up_down) * 100
    '''
# Motors
    message_display(17,'Motor 1 = ' + str(forwLeft) +'%',WIDTH/1.1,HEIGHT/20 )
    message_display(17,'Motor 2 = ' + str(forwLeft) +'%',WIDTH/1.1,HEIGHT/12 )
    message_display(17,'Motor 3 = ' + str(forwLeft) +'%',WIDTH/1.1,HEIGHT/8.7 )
    message_display(17,'Motor 4 = ' + str(forwLeft) +'%',WIDTH/1.1,HEIGHT/6.75 )
# Tasks
    message_display(24,'Tasks',WIDTH/12,HEIGHT/27)
    pygame.draw.rect(screen, BLACK,(WIDTH/6,0,3,HEIGHT)) #list vert
    pygame.draw.rect(screen, WHITE,(WIDTH/2.45,0,3,HEIGHT/19)) #name seperation
    pygame.draw.rect(screen, BLACK,(0,HEIGHT/19,WIDTH/1.2,3)) #list horiz
    pygame.draw.rect(screen, BLACK,(0,HEIGHT/6,WIDTH/1.2,3)) #discr horiz
    pygame.draw.rect(screen, BLACK,(WIDTH/1.2,0,3,HEIGHT)) #discr vert
    task_time = 0
    points = 0
    start_space = reset_start_space
    for message in task_dicfun(tasks_dic,color_list):
        name_task,disc_task,task_color,point = message
        points += point
        
        if cooldown != None: cooldown_1 = cooldown
        cooldown = button_for_tasks(cooldown_1,13,name_task,0,start_space,WIDTH/6,difer,task_color,click_color,task_time,color_list,name_task,disc_task,finished_function,task_discription)
        start_space += difer
        task_time += 1
    
    message_display(17,str(points) + ' points',WIDTH/2.2,HEIGHT/26)



    pygame.display.flip()


pygame.quit()
#ser.close()
print ('Successful closing!')
quit()












