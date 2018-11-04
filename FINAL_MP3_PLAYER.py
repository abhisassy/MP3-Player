import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import time
import random
import os
import sys
from pygame import mixer # Load the required library
#mixer pakcage is for mp3 decoding


#pygame.init()

black = (0,0,0) #rgb values later used in pygame
white = (255,255,255)
button=(0,0,128)
        

#DATA STRUCTURE QUEUE
class CircularQueue:
    flag=0

    #Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 0
        

    #Adding elements to the queue
    def enqueue(self,data):
        #print(self.maxSize)
        if self.size() == self.maxSize-1:
            print("Queue Full!")
            return
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    #Removing elements from the queue
    def dequeue(self):
        if self.size()==0:
            print ("Queue Empty!")
            return 0 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    #Calculating the size of the queue
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))
    #display contents of queue in console
    def disp(self):
        if(mixer.music.get_busy()): #if the music is palying
            i=1
        else:
            i=0
        print("NEXT UP:")
        while(True):
            
            if ((self.head+i)%self.maxSize) == self.tail or self.size()==0:
                print("END")
                break;
            print(self.queue[(self.head+i)%self.maxSize])
            i=i+1
            
    

#searches for mp3 files in the directory given and stores in gloabl list 'file' 
def song_list():
    print("list of songs:")
    i=0
    for filename in os.listdir("C:/Users/jedib/Desktop/3sem/DS/dsproj"):  #enter the directory of music folder
        if filename.endswith(".mp3"):
            file.append(filename)
            print((i+1),file[i])
            i=i+1
#retrns number of songs in directory
def size2():
    count=0
    for filename in os.listdir("C:/Users/jedib/Desktop/3sem/DS/dsproj"):
        if filename.endswith(".mp3"):
            count=count+1
    return count;

#pygame console 
def pygm():
        pygame.init() #iintitialize pygame environment
        gameDisplay=pygame.display.set_mode((1080,720)) #dimensions of the pygame window
        pygame.display.set_caption("MP3 Player")                        
        gameDisplay.fill((230,230,250)) # Background colour

        
        pygame.font.init() # you have to call this at the start, 
                           # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont.render('MP3 PLAYER', False, (0, 0, 0))
        gameDisplay.blit(textsurface,(373,50))
        pygame.display.update() #updates the display and prints elements
        
        #pygame.draw.rect(gameDisplay, blue,(50,40,120,120))#border

        #Drawing the buttons
        #volume buttons
        pygame.draw.rect(gameDisplay, button,(950,120,50,50))
        textsurface = myfont.render('+', False, white)
        gameDisplay.blit(textsurface,(962,95))
        
        pygame.draw.rect(gameDisplay, button,(950,200,50,50))
        textsurface = myfont.render('-', False, white)
        gameDisplay.blit(textsurface,(962,175))

        
        #exit
        pygame.draw.rect(gameDisplay, button,(50,120,75,75))
        textsurface = myfont.render('X', False, white)
        gameDisplay.blit(textsurface,(64,110))
        
        #play,next and prev bttn
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        pygame.draw.rect(gameDisplay, button,(350,300,100,100))
        pygame.draw.rect(gameDisplay, button,(500,300,100,100))
        pygame.draw.rect(gameDisplay, button,(650,300,100,100))
        
        textsurface = myfont.render('<    p   >', False, white)
        gameDisplay.blit(textsurface,(375,259))
        
        #pause unpause and rewind
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        pygame.draw.rect(gameDisplay, button,(300,450,100,100))
        pygame.draw.rect(gameDisplay, button,(500,450,100,100))
        pygame.draw.rect(gameDisplay, button,(700,450,100,100))

        textsurface = myfont.render('pause                un               rewind', False, white)
        gameDisplay.blit(textsurface,(312,460))
        textsurface = myfont.render('pause', False, white)
        gameDisplay.blit(textsurface,(510,480))
        #disp,list and que
        pygame.draw.rect(gameDisplay, button,(950,400,50,50))
        pygame.draw.rect(gameDisplay, button,(950,500,50,50))
        pygame.draw.rect(gameDisplay, button,(950,600,50,50))

        textsurface = myfont.render('Q', False, white)
        gameDisplay.blit(textsurface,(960,400))
        textsurface = myfont.render('L', False, white)
        gameDisplay.blit(textsurface,(960,500))
        textsurface = myfont.render('D', False, white)
        gameDisplay.blit(textsurface,(960,600))

        pygame.display.update()


        print(q.size())
        if q.size()==0: #Display no songs on pygame if no songs are queued. initially no songs will be queued.
                print("NO SONG ")
                textsurface = myfont.render('NO SONG PLAYING', False, white)
                gameDisplay.blit(textsurface,(400,180))
                pygame.display.update()
                #return
        else:
                mixer.music.load(q.queue[q.head])  #load the first song in queue
                mixer.music.play()
                print("Now Playing :",q.queue[q.head])
                print("VOLUME: ",mixer.music.get_volume())
                textsurface = myfont.render(q.queue[q.head], False, white)
                gameDisplay.blit(textsurface,(400,200))
                pygame.display.update()
        
        while True:

                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                        
                
                
                mouse=pygame.mouse.get_pos() # print(click)Gets co-ordinates of mouse
                click=pygame.mouse.get_pressed() #( 0,0,0 ) turns to 1 if left click,center click, right click respetively
                #print(mouse)
                #print(click)

                pygame.draw.rect(gameDisplay, button,(50,250,150,40))
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render("VOL "+str(float("{0:.2f}".format(mixer.music.get_volume()))), False, white) #displays the volume  upto 2 decimal places
                gameDisplay.blit(textsurface,(50,250))
                pygame.display.update()
                
                if mixer.music.get_busy()!=1 and q.size()!=0: #when no song is playing but queue is not empty , play next song 
                        #print("lol")
                        #print(q.size())
                        if q.size()!=0:
                            q.dequeue()
                            pygm()
                        else:
                            print("NO SONGS LEFT IN Queue")
                
                if q.size()>0 and mixer.music.get_busy()==1 and q.flag==1: #this is to display the song duration
                    pygame.draw.rect(gameDisplay, button,(700,250,180,40))
                    myfont = pygame.font.SysFont('Comic Sans MS', 30)
                    if(mixer.music.get_pos()/1000>60):
                        textsurface = myfont.render(str(float("{0:.2f}".format(mixer.music.get_pos()/(1000*60))))+" min", False, white)
                    else:
                        textsurface = myfont.render(str(float("{0:.2f}".format(mixer.music.get_pos()/(1000))))+" sec", False, white)
                    gameDisplay.blit(textsurface,(720,250))
                    #time.sleep(0.5)
                    pygame.display.update()
            
                        
                #different on click events 
                #X
                if ((50+75)> mouse[0] > 50) and ((120+75) > mouse[1]> 120) and click[0]==1 :
                        pygame.quit()
                        exit()
                #play      
                if ((500+100)> mouse[0] > 500) and ((300+100) > mouse[1]> 300) and click[0]==1 :
                        time.sleep(0.5)
                        q.flag=1;
                        pygm()
                        

                #Q
                if ((950+50)> mouse[0] > 950) and ((400+50) > mouse[1]> 400) and click[0]==1 :
                        num=int(input("Enter Song No. to queue"))
                        #print(type(num))
                        if num<=size2():
                            q.enqueue(file[num-1])
                        else:
                            print("invalid")
                        
                #L
                if ((950+50)> mouse[0] > 950) and ((500+50) > mouse[1]> 500) and click[0]==1 :
                        time.sleep(0.5)
                        song_list()
                        
                #D      
                if ((950+50)> mouse[0] > 950) and ((600+50) > mouse[1]> 600) and click[0]==1 :
                        time.sleep(0.5)
                        q.disp()


                #+
                if ((950+500)> mouse[0] > 950) and ((120+50) > mouse[1]> 120) and click[0]==1 :
                        time.sleep(0.5)
                        
                        if mixer.music.get_volume()==1:
                            print("MAX VOLUME")
                        else:
                            mixer.music.set_volume(mixer.music.get_volume()+0.1)
                            print(mixer.music.get_volume())
                #-            
                if ((950+500)> mouse[0] > 950) and ((200+50) > mouse[1]> 200) and click[0]==1 :
                        time.sleep(0.5)
                        if mixer.music.get_volume()>0.09:
                           mixer.music.set_volume(mixer.music.get_volume()-0.1)
                           print(mixer.music.get_volume())
                        else:
                            mixer.music.set_volume(0)
                            print("VOLUME IS ZERO")
                #<
                if ((350+100)> mouse[0] > 350) and ((300+100) > mouse[1]> 300) and click[0]==1 :
                        time.sleep(0.5)
                        if q.head!=0 and q.size!=0:
                            q.head=(q.head-1)%q.maxSize;
                            pygm()
                        else:
                            print("NO SONG")
                #>
                if ((650+100)> mouse[0] > 650) and ((300+100) > mouse[1]> 300) and click[0]==1 :
                        time.sleep(0.5)
                        if q.size()==1:
                           print("NO SONGS IN QUEUE")
                        else:
                            q.dequeue()
                            pygm()
                #pause        
                if ((300+100)> mouse[0] > 300) and ((450+100) > mouse[1]> 450) and click[0]==1 :
                        time.sleep(0.5)
                        mixer.music.pause()
                #unpause
                if ((500+100)> mouse[0] > 500) and ((450+100) > mouse[1]> 450) and click[0]==1 :
                        time.sleep(0.5)
                        mixer.music.unpause()
                #rewind
                if ((700+100)> mouse[0] > 700) and ((450+100) > mouse[1]> 450) and click[0]==1 :
                        time.sleep(0.5)
                        mixer.music.play()
                        #mixer.music.set_pos(0.0)

                
                        
                        
#global variables
q = CircularQueue()
q.maxSize=size2()-1
file=[]
#initialize mp3 decoder
mixer.init()
mixer.music.set_volume(0.5)
#get list of songs from directory
song_list()
#play a blank mp3 intially which is required for code to run intially without any glitches
mixer.music.load('C:/Users/jedib/Downloads/blank.mp3')
mixer.music.play()
#call main func pygm which opens pygame window
pygm()
