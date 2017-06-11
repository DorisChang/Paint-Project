#DORIS CHANG
from pygame import * 
from random import *
from tkinter import *
from math import *
import os

os.environ["SDL_VIDEO_WINDOW_POS"]="150,150"#opens the window in a specific spot on the screen
root=Tk()
root.withdraw() #hiding the "tk window"
init()

RED  =(255,0,0)
GREEN=(0,255,0)
BLUE= (56,205,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
LIME=(212,255,0)
YELLOW=(235,255,56)
PINK=(255,56,116)
ORANGE=(255,117,26)
PURPLE=(191,82,255)
coloursArray=(RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE,RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE,RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)#RAINBOW colour array

size=(1024,768) #screen resolution
screen=display.set_mode(size)#creating a 800x600 window

display.set_caption("PAINT")

running=True #boolean variable
free=True #checks to ensure that the tool/colour won't change unless clicked on
randc=False #boolean for keeping track of the current mode of the colour tool
done=True
screen.fill(BLACK)

rieslingFont=font.Font("riesling.ttf",50)
laurenFont=font.Font("Lauren-Regular.ttf",70)
fishFont=font.Font("Fishfingers.ttf",50)
collegedFont=font.Font("Colleged.ttf",50)
penelopeFont=font.Font("PenelopeAnne.ttf",50)
courierFont=font.SysFont("Courier New",50)
lcourierFont=font.SysFont("Courier New",25)
scourierFont=font.SysFont("Courier New",15)
smcourierFont=font.SysFont("Courier New",13)
xscourierFont=font.SysFont("Courier New",10)
Text=lcourierFont.render("travel the world",True,WHITE)
screen.blit(Text,(1,5))
draw.line(screen,WHITE,(248,0),(248,40))
draw.line(screen,WHITE,(258,0),(258,40))
draw.line(screen,WHITE,(880,610),(880,768))


#------------------rect objects---------------------
panelRect=Rect(104,614,772,150)

canvasRect=Rect(0,40,1024,570)
palRect=Rect(265,0,343,40)
currentRect=Rect(249,0,9,39)
toolkitRect=Rect(2,613,875,152)
dropperRect=Rect(612,3,34,34)
undoRect=Rect(776,3,34,34)
redoRect=Rect(827,3,34,34)
openRect=Rect(878,3,34,34)
saveRect=Rect(929,3,34,34)
newRect=Rect(986,3,34,34)
infoRect=Rect(880,611,144,158)

allGeneralArray=[dropperRect,undoRect,redoRect,openRect,saveRect,newRect]


#------------rect objects in tools-------------
basicRect=Rect(2,613,50,50)
pencilRect=Rect(130,640,81,102)
eraserRect=Rect(258,640,81,102)
paintbrushRect=Rect(386,640,81,102)
highlighterRect=Rect(514,640,81,102)
sprayRect=Rect(642,640,81,102)
fillsRect=Rect(770,640,81,50)
fillRect=Rect(770,692,81,50)
basicArray=[pencilRect,eraserRect,paintbrushRect,highlighterRect,sprayRect,fillsRect,fillRect]
basicNamesArray=["pencil","eraser","paint brush","highlighter","spray","fill screen","fill"]


shapesRect=Rect(53,613,50,50)
lineRect=Rect(130,640,40,100)
rectangleRect=Rect(226,640,81,49)
frectangleRect=Rect(226,691,81,49)
squareRect=Rect(362,640,81,49)
fsquareRect=Rect(362,691,81,49)
ellipseRect=Rect(497,640,81,49)
fellipseRect=Rect(497,691,81,49)
circleRect=Rect(633,640,81,49)
fcircleRect=Rect(633,691,81,49)
irregularRect=Rect(770,640,81,49)
firregularRect=Rect(770,691,81,49)
shapesArray=[lineRect,rectangleRect,frectangleRect,squareRect,fsquareRect,ellipseRect,fellipseRect,circleRect,fcircleRect,irregularRect,firregularRect]
shapesNamesArray=["line","rectangle","filled rectangle","square","filled square","ellipse","filled ellipse","circle","filled circle","irregular","filled irregular"]

stampsRect=Rect(2,664,50,50)
smallRect=Rect(108,665,25,24)
mediumRect=Rect(135,639,25,50)
largeRect=Rect(162,618,26,71)
stampRect=Rect(108,691,80,71)
caseRect=Rect(190,618,80,71)
rainbowRect=Rect(190,691,80,71)
fujiRect=Rect(272,618,80,71)
pyramidsRect=Rect(272,691,80,71)
tajmahalRect=Rect(354,618,80,71)
louvreRect=Rect(354,691,80,71)
blossomsRect=Rect(436,618,71,144)
treeRect=Rect(509,618,71,144)
eiffelRect=Rect(582,618,71,144)
leaningRect=Rect(655,618,71,144)
building101Rect=Rect(728,618,71,144)
merlionRect=Rect(801,618,71,144)
stampsArray=[stampRect,caseRect,rainbowRect,fujiRect,pyramidsRect,tajmahalRect,louvreRect,blossomsRect,treeRect,eiffelRect,leaningRect,building101Rect,merlionRect]
stampsNamesArray=["stamp","suit case","rainbow","mtn. Fuji","pyramids","Taj Mahal","Louvre","cherry blossoms","tree","Eiffel Tower","Leaning Tower of Pisa","Taipei 101","Merlion"]

bkgsRect=Rect(53,664,50,50)
hillsRect=Rect(109,655,125,69)
springparkRect=Rect(237,655,125,69)
mapRect=Rect(364,655,125,69)
skylineRect=Rect(491,655,125,69)
beachRect=Rect(618,655,125,69)
desertRect=Rect(745,655,125,69)
bkgsArray=[hillsRect,springparkRect,mapRect,skylineRect,beachRect,desertRect]
bkgsNamesArray=["hills","spring park","world map","skyline","beach","desert"]

filtersRect=Rect(2,715,50,50)
sepiaRect=Rect(110,655,125,69)
bwRect=Rect(237,655,125,69)
brightRect=Rect(364,655,126,69)
warmRect=Rect(493,655,125,69)
filtersArray=[sepiaRect,bwRect,brightRect,warmRect]
filtersNamesArray=["sepia","black&white","bright","warm"]

textRect=Rect(53,715,50,50)
courierRect=Rect(130,640,81,102)
fishRect=Rect(258,640,81,102)
laurenRect=Rect(386,640,81,102)
penelopeRect=Rect(514,640,81,102)
collegedRect=Rect(642,640,81,102)
rieslingRect=Rect(770,640,81,102)
textArray=[courierRect,fishRect,laurenRect,penelopeRect,collegedRect,rieslingRect]
textNamesArray=["courier","fish fingers","lauren","penelope","colleged","riesling"]

btmLftArray=[basicRect,shapesRect,stampsRect,bkgsRect,filtersRect,textRect]#array for changing colour of rectangle outlines
btmNamesArray=["basic","shapes","stamps","bkgs","filters","text"]

#-------------------load images---------------------
pallettePic=image.load("images/pallette2.jpg")
randomcPic=image.load("images/rainbowsmall.jpg")
generalpanelPic=image.load("images/generalpanel.png")
toolspanelPic=image.load("images/toolspanel.png")
basictoolspanelPic=image.load("images/toolspanelbasic.png")
shapestoolspanelPic=image.load("images/toolspanelshapes.png")
bkgstoolspanelPic=image.load("images/bkg.png")
stampstoolspanelPic=image.load("images/toolspanelstamps.png")
filterstoolspanelPic=image.load("images/filters.png")
texttoolspanelPic=image.load("images/text.png")
toolkitPic=image.load("images/toolkit.png")

        #-----------load stamps--------------
#medium size
stampStamp=image.load("images/planestamp.png")
suitcaseStamp=image.load("images/suitcase.png")
rainbowStamp=image.load("images/rainbow.png")
fujiStamp=image.load("images/fuji.png")
pyramidsStamp=image.load("images/pyramids.png")
tajmahalStamp=image.load("images/TajMahal.png")
louvreStamp=image.load("images/louvre.png")

blossomStamp=image.load("images/cherryblossoms.png")
treeStamp=image.load("images/tree.png")
eiffelStamp=image.load("images/eiffeltower.png")
leaningStamp=image.load("images/leaning.png")
taipeiStamp=image.load("images/taipei101.png")
merlionStamp=image.load("images/merlion.png")
#small size
stampStamps=image.load("images/planestampsmall.png")
suitcaseStamps=image.load("images/suitcasesmall.png")
rainbowStamps=image.load("images/rainbowsmall.png")
fujiStamps=image.load("images/fujismall.png")
pyramidsStamps=image.load("images/pyramidssmall.png")
tajmahalStamps=image.load("images/TajMahalsmall.png")
louvreStamps=image.load("images/louvresmall.png")

blossomStamps=image.load("images/cherryblossomssmall.png")
treeStamps=image.load("images/treesmall.png")
eiffelStamps=image.load("images/eiffeltowersmall.png")
leaningStamps=image.load("images/leaningsmall.png")
taipeiStamps=image.load("images/taipei101small.png")
merlionStamps=image.load("images/merlionsmall.png")
#large size
stampStampl=image.load("images/planestamplarge.png")
suitcaseStampl=image.load("images/suitcaselarge.png")
rainbowStampl=image.load("images/rainbowlarge.png")
fujiStampl=image.load("images/fujilarge.png")
pyramidsStampl=image.load("images/pyramidslarge.png")
tajmahalStampl=image.load("images/TajMahallarge.png")
louvreStampl=image.load("images/louvrelarge.png")

blossomStampl=image.load("images/cherryblossomslarge.png")
treeStampl=image.load("images/treelarge.png")
eiffelStampl=image.load("images/eiffeltowerlarge.png")
leaningStampl=image.load("images/leaninglarge.png")
taipeiStampl=image.load("images/taipei101large.png")
merlionStampl=image.load("images/merlionlarge.png")

        #------------load bkgs---------------
hillsBkg=image.load("images/rollinghillsbkg.jpeg")
springparkBkg=image.load("images/springparkbkg.png")
mapBkg=image.load("images/worldmap.png")
skylineBkg=image.load("images/skyline.png")
beachBkg=image.load("images/beach.jpg")
desertBkg=image.load("images/desert.jpg")
bkgArray=[hillsBkg,springparkBkg,mapBkg,skylineBkg,beachBkg,desertBkg]
bkgNamesArray=["hills","spring park","world map","skyline","beach","desert"]

#-------------------blit images---------------------
screen.blit(pallettePic,(265,0))#colour pallette
screen.blit(generalpanelPic,(608,0))#top right tools
screen.blit(toolkitPic,(3,613))#bottom left tools
screen.blit(basictoolspanelPic,(104,614))#basic tools on bottom

draw.rect(screen,WHITE,canvasRect)
draw.line(screen,WHITE,(0,39),(1024,39))
draw.line(screen,WHITE,(0,610),(1024,610))
draw.rect(screen,WHITE,toolkitRect,1)
col=(0,0,0)#current colour variable
undoArray=[]#array where all screen captures go
redoArray=[]#array where screen captures go after the undo button has been pressed
sz=2#current size
tooltype="basic"
tool="pencil"
font="none"
mx,my=0,0#mouse position
icount=0#variable for the irregular tool (how many vertices)
iArray=[]#array for the coordinate of the vertices
undoArray.append(screen.subsurface(canvasRect).copy())#adding blank canvas to the undoArray
undo=False#variable to check if undo has been done
redo=False#variable to check if redo ha been done
canvasChanged=False#boolean to see if anything has been changed in the canvas
pressed=False#for colour changing (randomly generated or plain)
screenBuff=screen.copy()#screen capture
text=[]#array where most (excluding things like space, enter, backspace,...) of the keys pressed on
stampsize="small"
bkg=False#variable to know if there is currently a bkg on the canvas (used for the eraser tool)

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                start=evt.pos #start is a tuple(x,y)-the starting point of a line
                back=screen.copy()

        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) and mb[2]==1 and tool=="text":#gets text tool prepared every time the mouse is pressed on the screen
                text=[]
                tx=mx
                ty=my
                undoArray.append(screen.subsurface(canvasRect).copy())
            free=True
            if evt.button==4 and sz<20: #scrolling up to change current size
                sz+=2
            if evt.button==5 and sz>2: #scrolling down to change current size
                sz-=2

        #---------------text tool-----------------
        if tooltype!="text":#ensures that you won't be able to type without being in the text tool
            font="none"
        if evt.type==KEYDOWN and tool=="text" and 40<=ty<=560 and font!="none":
            #NEED TO RIGHT CLICK TO ADD TEXT TO UNDO ARRAY and CLEAR THE TEXT ARRAY (right click after each time you finish typing a line)
            name=evt.unicode#actal key pressed (ex. "g" when g is pressed)
            if evt.key==8 and len(text)>=2:#backspace
                del(text[-1])#delete last item in the text array
            elif evt.key==8 and len(text)<2:
                text=[]#make text empty when deleting the last item
            elif evt.key!=13 and evt.key!=9:
                text.append(name)#add the key pressed to the name array if it is not the space or the tab key
            if evt.key==9:#tab
                for i in range(4):
                    text.append(" ")
            if name=="space":
                text.append(" ")
            if font!="none":#update canvas so there is no overlap after each time a key is pressed
                screen.blit(back,(0,0))
            #----blit the text using current font----
            if font=="courier":
                screen.blit(courierFont.render(("").join(text),True,col),(tx,ty))
            elif font=="fish fingers":
                screen.blit(fishFont.render(("").join(text),True,col),(tx,ty))
            elif font=="lauren":
                screen.blit(laurenFont.render(("").join(text),True,col),(tx,ty))
            elif font=="penelope":
                screen.blit(penelopeFont.render(("").join(text),True,col),(tx,ty))
            elif font=="colleged":
                screen.blit(collegedFont.render(("").join(text),True,col),(tx,ty))
            elif font=="riesling":
                screen.blit(rieslingFont.render(("").join(text),True,col),(tx,ty))
            if evt.key==13:#enter
                back=screen.copy()#add the last line of text to the canvas
                ty+=50
                text=[]#empty the list so the previous line of text is not in the array


    #-----------------DISPLAYS FOR BORDERS AROUND TOOLS---------------------
    if currentRect.collidepoint(mx,my) and my>1:#when mouse is over the rectangle showing current colour
        draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(248,0),(248,38))
        draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(258,0),(258,38))
    else:
        draw.line(screen,WHITE,(248,0),(248,38))
        draw.line(screen,WHITE,(258,0),(258,38))
    
    for a in allGeneralArray:#for tools on the top (eye dropper, undo/redo, save, open, new)
        if a.collidepoint(mx,my):
            draw.rect(screen,YELLOW,a,1)
        else:
            draw.rect(screen,WHITE,a,1)

    for i in range(len(btmLftArray)):#for the bottom left display with the different tool types
        if btmLftArray[i].collidepoint(mx,my) or tooltype==btmNamesArray[i]:
            draw.rect(screen,coloursArray[i],btmLftArray[i],1)
        else:
            draw.rect(screen,WHITE,btmLftArray[i],1)
            
             #------------inside individual tools------------------
    if tooltype=="basic":
        for i in range(len(basicArray)):
            if basicArray[i].collidepoint(mx,my) or tool==basicNamesArray[i]:
                draw.rect(screen,coloursArray[i],basicArray[i],1)
            else:
                draw.rect(screen,WHITE,basicArray[i],1)

    if tooltype=="shapes":
        for i in range(len(shapesArray)):
            if shapesArray[i].collidepoint(mx,my) or tool==shapesNamesArray[i]:
                draw.rect(screen,coloursArray[i],shapesArray[i],1)
            else:
                draw.rect(screen,WHITE,shapesArray[i],1)

    if tooltype=="stamps":
        for i in range(len(stampsArray)):
            if stampsArray[i].collidepoint(mx,my) or tool==stampsNamesArray[i]:
                draw.rect(screen,coloursArray[i],stampsArray[i],1)
            else:
                draw.rect(screen,WHITE,stampsArray[i],1)

    if tooltype=="bkgs":
        for i in range(len(bkgsArray)):
            if bkgsArray[i].collidepoint(mx,my) or tool==bkgsNamesArray[i]:
                draw.rect(screen,coloursArray[i],bkgsArray[i],1)
            else:
                draw.rect(screen,WHITE,bkgsArray[i],1)

    if tooltype=="filters":
        for i in range(len(filtersArray)):
            if filtersArray[i].collidepoint(mx,my) or tool==filtersNamesArray[i]:
                draw.rect(screen,coloursArray[i],filtersArray[i],1)
            else:
                draw.rect(screen,WHITE,filtersArray[i],1)

    if tooltype=="text":
        for i in range(len(textArray)):
            if textArray[i].collidepoint(mx,my) or font==textNamesArray[i]:
                draw.rect(screen,coloursArray[i],textArray[i],1)
            else:
                draw.rect(screen,WHITE,textArray[i],1)
                
    #-------------------INFO DISPLAY ON BOTTOM RIGHT------------------------
    if 40<=my<=610 and 0<mx<1023:#if mouse is currently on the canvas
        cy=my-40#finds position of mouse relative to the canvas, not the screen
        cx=mx
    else:
        cx="---"
        cy="---"
        
    #display of the current mouse position, tool type, tool, and font
    posText="x:%-5sy:%-5s "%(cx,cy)
    displayposText=scourierFont.render(posText,True,WHITE)
    sizeText="size: %s"%(sz)
    if tool=="pencil":
        sizeText="size: 1"
    sizeText=scourierFont.render(sizeText,True,WHITE)
    tooltypeText="tool type: %s"%(tooltype)
    tooltypeText=smcourierFont.render(tooltypeText,True,WHITE)
    toolText="tool: %s"%(tool)
    toolText=xscourierFont.render(toolText,True,WHITE)
    fontText="font: %s"%(font)
    fontText=scourierFont.render(fontText,True,WHITE)
    draw.rect(screen,BLACK,infoRect)#draw black rect over the previous info to update it
    screen.blit(displayposText,(880,630))
    screen.blit(sizeText,(880,656))
    screen.blit(tooltypeText,(880,685))
    screen.blit(toolText,(882,711))
    screen.blit(fontText,(882,735))
    
    #---get current mouse position and mouse status---
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()


    #-------------------SELECTING TOOL TYPE----------------
    if dropperRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tool="eye dropper"
        draw.rect(screen,WHITE,dropperRect,1)
        
    if undoRect.collidepoint(mx,my) and mb[0]==1 and free==True and undo==False: #checks to see if the undo has been done
        draw.rect(screen,WHITE,undoRect,1)
        undo=True #undo has been done
        if len(undoArray)>1:
            screen.subsurface(canvasRect).blit(undoArray[-2],(0,0))
            redoArray.append(undoArray[-1]) #add the last item in the undo array to the redo array before deleting 
            del(undoArray[-1])
        else: #keep bliting the only item in the undo array when the button is clicked
            screen.subsurface(canvasRect).blit(undoArray[0],(0,0))
    if undoRect.collidepoint(mx,my) and mb[0]==0 and undo==True:
        undo=False#makes undo false again when mouse is released
   
    if redoRect.collidepoint(mx,my) and mb[0]==1 and free==True and redo==False: #checks to see if the redo has been done
        draw.rect(screen,WHITE,redoRect,1)
        redo=True #redo has been done
        if len(redoArray)>0:#proceed to blit and delete the last thing in the redoArray if it is not empty
            screen.subsurface(canvasRect).blit(redoArray[-1],(0,0))
            undoArray.append(redoArray[-1])#add what was the last thing in the redo array to the undo array
            del(redoArray[-1])
    if redoRect.collidepoint(mx,my) and mb[0]==0 and redo==True:
        redo=False#makes redo false again when mouse is released
        
    if saveRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        try:
            fname=filedialog.asksaveasfilename(defaultextension="png")
            #asks the user to input the file name they would like to save as
            #(default extension is PNG)
            image.save(screen.subsurface(canvasRect),fname)
        except:
             pass #if the above doesn't work, prevent crashing
    if openRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tool="open"
        try:
            fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*bmp")])
            nPic=image.load(fname)#load the picture the user wants to open
        except:
             pass

    if newRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        draw.rect(screen,WHITE,newRect,1)
        canvasChanged=True#used for knowing when to add current canvas to the undo array
        draw.rect(screen,WHITE,canvasRect)#draws a white rectangle over the canvas (new canvas)
        bkg=False#change bkg to false as the bkg would have been covered if there had been one before the new canvas

    #-----------change tooltype according to which icon was pressed and blit the corresponding pannel-----------
    if basicRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tooltype="basic"
        screen.blit(basictoolspanelPic,(104,614))
    if shapesRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tooltype="shapes"
        screen.blit(shapestoolspanelPic,(104,614))
    if stampsRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tooltype="stamps"
        screen.blit(stampstoolspanelPic,(104,615))
        draw.rect(screen,WHITE,smallRect,1)
        draw.rect(screen,WHITE,mediumRect,1)
        draw.rect(screen,WHITE,largeRect,1)
    if bkgsRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tooltype="bkgs"
        screen.blit(bkgstoolspanelPic,(104,614))
    if filtersRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tooltype="filters"
        screen.blit(filterstoolspanelPic,(104,614))
    if textRect.collidepoint(mx,my) and mb[0]==1 and free==True:
        tooltype="text"
        tool="courier"
        screen.blit(texttoolspanelPic,(104,614))
        

    #---------------------SELECTING TOOL-----------------------
    if tooltype=="basic":
        if pencilRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="pencil"
        if eraserRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="eraser"
        if paintbrushRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="paint brush"
        if highlighterRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="highlighter"
        if sprayRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="spray"
        if fillsRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="fill screen"
            screen.fill(col,canvasRect)
            bkg=False
            canvasChanged=True
        if fillRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="fill"

    if tooltype=="shapes":
        if lineRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="line"
        if rectangleRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="rectangle"
        if frectangleRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="filled rectangle"
        if squareRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="square"
        if fsquareRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="filled square"
        if ellipseRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="ellipse"
        if fellipseRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="filled ellipse"
        if circleRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="circle"
        if fcircleRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="filled circle"
        if irregularRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="irregular"
        if firregularRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="filled irregular"

    if tooltype=="stamps":
        #makes outline of the current size rectangles pink and the other two white
        if smallRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            draw.rect(screen,PINK,smallRect,1)
            stampsize="small"
        if mediumRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            draw.rect(screen,PINK,mediumRect,1)
            stampsize="medium"
        if largeRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            draw.rect(screen,PINK,largeRect,1)
            stampsize="large"
        if stampsize=="small" or smallRect.collidepoint(mx,my):
            draw.rect(screen,PINK,smallRect,1)
        else:
            draw.rect(screen,WHITE,smallRect,1)
        if stampsize=="medium" or mediumRect.collidepoint(mx,my):
            draw.rect(screen,PINK,mediumRect,1)
        else:
            draw.rect(screen,WHITE,mediumRect,1)
        if stampsize=="large" or largeRect.collidepoint(mx,my):
            draw.rect(screen,PINK,largeRect,1)
        else:
            draw.rect(screen,WHITE,largeRect,1)

        #selecting the stamp of choice
        if stampRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="stamp"
        if caseRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="suit case"
        if rainbowRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="rainbow"
        if fujiRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="mtn. Fuji"
        if pyramidsRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="pyramids"
        if tajmahalRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="Taj Mahal"
        if louvreRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="Louvre"
        if blossomsRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="cherry blossoms"
        if treeRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="tree"
        if eiffelRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="Eiffel Tower"
        if leaningRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="Leaning Tower of Pisa"
        if building101Rect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="Taipei 101"
        if merlionRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="Merlion"
                
    if tooltype=="bkgs":
        #selecting choice of bkg
        if hillsRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="hills"
            screen.blit(hillsBkg,(0,40))
            canvasChanged=True
            bkg=True
            bkgName=hillsBkg
        if springparkRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="spring park"
            screen.blit(springparkBkg,(0,40))
            canvasChanged=True
            bkg=True
            bkgName=springparkBkg
        if mapRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="world map"
            screen.blit(mapBkg,(0,40))
            canvasChanged=True
            bkg=True
            bkgName=mapBkg
        if skylineRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="skyline"
            screen.blit(skylineBkg,(0,40))
            canvasChanged=True
            bkg=True
            bkgName=skylineBkg
        if beachRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="beach"
            screen.blit(beachBkg,(0,40))
            canvasChanged=True
            bkg=True
            bkgName=beachBkg
        if desertRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="desert"
            screen.blit(desertBkg,(0,40))
            canvasChanged=True
            bkg=True
            bkgName=desertBkg

    if tooltype=="filters":
        #selecting choice of filter
        if sepiaRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="sepia"
            canvasChanged=True
            #------change each pixel in the canvas to create sepia effect------
            for x in range(1024):
                for y in range(40,610):
                    r,g,b,a=screen.get_at((x,y))
                    r2=min(255,int(r*.393+g*.769+b*.189))
                    g2=min(255,int(r*.349+g*.686+b*.168))
                    b2=min(255,int(r*.272+g*.534+b*.131))
                    screen.set_at((x,y),(r2,g2,b2))
        if bwRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="black&white"
            canvasChanged=True
            #-----change each pixel in the canvas to create black and white effect------
            for x in range(1024):
                for y in range(40,610):
                    r,g,b,a=screen.get_at((x,y))
                    grey = r*0.24+g*0.72+b*0.04
                    screen.set_at((x,y),(grey,grey,grey))
        if brightRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="bright"
            canvasChanged=True
            #-----change each pixel in the canvas to create a brighter effect------
            for x in range(1024):
                for y in range(40,610):
                    r,g,b,a=screen.get_at((x,y))
                    r2=min(255,int(r*1.75))
                    g2=min(255,int(g*1.35))
                    b2=min(255,int(b*1.55))
                    screen.set_at((x,y),(r2,g2,b2))
        if warmRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            tool="warm"
            canvasChanged=True
            #-----change each pixel in the canvas to create a warmer red look------
            for x in range(1024):
                for y in range(40,610):
                    r,g,b,a=screen.get_at((x,y))
                    r2=min(255,int(r*1.5))
                    g2=min(255,int(g*.9))
                    b2=min(255,int(b*0.8))
                    screen.set_at((x,y),(r2,g2,b2))
      
    if tooltype=="text":
        if courierRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            font="courier"
        if fishRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            font="fish fingers"
        if laurenRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            font="lauren"
        if penelopeRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            font="penelope"
        if collegedRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            font="colleged"
        if rieslingRect.collidepoint(mx,my) and mb[0]==1 and free==True:
            font="riesling"
        
    #---------------------USING THE TOOL-----------------------
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        if tool=="eye dropper":
            col=screen.get_at((mx,my))#gets colour at the current pixel
            draw.rect(screen,col,currentRect)

        screen.set_clip(canvasRect)
        done=False

        if tool=="eraser" and bkg and 20<=mx<=1004 and 60<=my<=590:#when there is a bkg on the canvas
            sample=bkgName.subsurface([mx-20,my-60,40,40])
            #surface (grab a small part of the image (40x40))
            screen.blit(sample,(mx-20,my-20))
            #and blit it on the screen
        elif tool=="eraser" and 0<mx<=1022 and 40<=my<570 and not bkg: #won't continue to erase if the mouse position is out of the canvas (since the canvas is entire width of the screen)
            #drawing a bunch of circles between where the mouse was pressed to where it is now instead of drawing a line
            dx=mx-omx
            dy=my-omy
            if dy==0==dx:
                draw.circle(screen,WHITE,(mx,my),sz)
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)#horizontal move
                dotY=int(omy+i*dy/dist)#vertical move
                draw.circle(screen,WHITE,(dotX,dotY),sz) 

        if tool=="paint brush" and 1<=mx<=1022:
            dx=mx-omx
            dy=my-omy
            if dy==0==dx:#draw one ellipse if the mouse is pressed but not moved
                draw.ellipse(screen,col,(mx-10,my-1,sz*2.5,sz*0.5))
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)#horizontal move
                dotY=int(omy+i*dy/dist)#vertical move
                draw.ellipse(screen,col,(dotX-10,dotY-1,sz*2.5,sz*0.5))#draw multiple ellipses from where the mouse was pressed to where it is now

        if tool=="pencil" and 1<=mx<=1022:
            dx=mx-omx
            dy=my-omy
            if dx==dy==0:#draw a circle if mouse is pressed but not moved
                draw.circle(screen,col,(mx,my),2)
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)#horizontal move
                dotY=int(omy+i*dy/dist)#vertical move
                draw.circle(screen,col,(dotX,dotY),2)

        if tool=="highlighter" and 1<=mx<=1022:
            brushHead=Surface((5,60),SRCALPHA) #creates a surface of 5*60
            draw.circle(brushHead,(col[0],col[1],col[2],4),(5,5),sz) 
            dx=mx-omx
            dy=my-omy
            if dx==dy==0:#blit the brushHead at current mouse location if it is not moved
                screen.blit(brushHead,(mx,my))
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)#horizontal move
                dotY=int(omy+i*dy/dist)#vertical move
                screen.blit(brushHead,(dotX,dotY)) #blit the brushHead from where the mouse was pressed to where it is now

        if tool=="spray" and 1<=mx<=1022:
            rx=randint(-sz-20,sz+20)#create random number 
            ry=randint(-sz-20,sz+20)#create random number
            if ((rx)**2+(ry)**2)**0.5<=sz+20:#checks that the distance of the random coordinate to (mx,my) is within the current size
                screen.set_at((rx+mx,ry+my),col) #change colour of the pixel

        if tool=="fill":
            ocord=mx,my#original coordinate
            co=[]#list of coordinates
            co.append(ocord)
            ocol=screen.get_at(ocord)#colour at the pixel pressed on
            if ocol!=col:#checks that the original colour is not the same as the current colour
                while len(co)>0:
                    cx,cy=co.pop()#make cx and cy take on the value of the last two items in the array then remove them
                    if canvasRect.collidepoint(cx,cy) and screen.get_at((cx,cy))==ocol: #checks that the pixel is inside the canvas and that the colour needs to be changed
                        screen.set_at((cx,cy),col)#changes the colour at the pixel
                        co+=[(cx,cy+1),(cx,cy-1),(cx+1,cy),(cx-1,cy)] #adds the four pixels around (cx,cy) to the list which will be put in the same process

        if tool=="rectangle":
            screen.blit(back,(0,0))#update canvas so there is always only one rectangle on the canvas at a time
            draw.rect(screen,col,(start[0],start[1],mx-start[0],my-start[1]),2)#draw rectangle with width of 2

        if tool=="filled rectangle":
            screen.blit(back,(0,0))
            draw.rect(screen,col,(start[0],start[1],mx-start[0],my-start[1]))#draw filled rectangle

        if tool=="square":
            screen.blit(back,(0,0))
            draw.rect(screen,col,(start[0],start[1],mx-start[0],mx-start[0]),2)#draw square with width of the length from the mx where the mouse was pressed to where the x coordinate is now

        if tool=="filled square":
            screen.blit(back,(0,0))
            draw.rect(screen,col,(start[0],start[1],mx-start[0],mx-start[0]))

        if tool=="ellipse":
            screen.blit(back,(0,0))
            ellRect=Rect(start[0],start[1],mx*1.1-start[0],my*1.1-start[1])
            if abs(ellRect[2])<6 or abs(ellRect[3])<6:#prevents the thickness of the ellipse from getting thicker than the actual ellipse  
                ellRect[2]=6
                ellRect[3]=6
            ellRect.normalize()
            draw.ellipse(screen,col,ellRect,2)
            
        if tool=="filled ellipse":
            screen.blit(back,(0,0))
            ellRect=Rect(start[0],start[1],mx-start[0],my-start[1])
            ellRect.normalize()
            draw.ellipse(screen,col,ellRect)

        if tool=="circle":
            screen.blit(back,(0,0))
            if int(((mx-start[0])**2+(my-start[1])**2)**0.5)<4:#draw tiny circle if the radius is too small
                draw.circle(screen,col,start,4,4)
            else:
                draw.circle(screen,col,start,int(((mx-start[0])**2+(my-start[1])**2)**0.5),2)#uses distance formula to find radius
            
        if tool=="filled circle":
            screen.blit(back,(0,0))
            draw.circle(screen,col,start,int(((mx-start[0])**2+(my-start[1])**2)**0.5))#uses distance formula to find radius

        if tool=="irregular" or tool=="filled irregular":
            screen.blit(back,(0,0))#update canvas for when the line is dragged around the canvas
            if len(iArray)<=1:
                draw.aaline(screen,col,start,(mx,my),sz) #draw a line from where the mouse was pressed to where it is currently
            else:
                draw.aaline(screen,col,iArray[-1],(mx,my),sz) #draw a line from the end of the last line to where it is currently

        if tool=="line":
            screen.blit(back,(0,0))#update canvas for when the mouse is dragged around the canvas
            draw.aaline(screen,col,start,(mx,my),sz)
    
        if tool=="open":
            #turns the opened picture into something similar to a stamp where it can be moved anywhere on the screen for multiple times
            screen.blit(back,(0,0))
            ssz=nPic.get_size()
            screen.subsurface(canvasRect).blit(nPic,(mx-ssz[0]//2,my-ssz[1]//2))

        #-------stamps, blit the stamp selected and the correct size selected---------
        if tool=="stamp":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=stampStamps
            if stampsize=="medium":
                stamp=stampStamp
            if stampsize=="large":
                stamp=stampStampl
            ssz=stamp.get_size()#find size of stamp
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))#blit the stamp so that the mouse is in the middle of the stamp
        if tool=="suit case":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=suitcaseStamps
            if stampsize=="medium":
                stamp=suitcaseStamp
            if stampsize=="large":
                stamp=suitcaseStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="rainbow":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=rainbowStamps
            if stampsize=="medium":
                stamp=rainbowStamp
            if stampsize=="large":
                stamp=rainbowStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="mtn. Fuji":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=fujiStamps
            if stampsize=="medium":
                stamp=fujiStamp
            if stampsize=="large":
                stamp=fujiStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="pyramids":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=pyramidsStamps
            if stampsize=="medium":
                stamp=pyramidsStamp
            if stampsize=="large":
                stamp=pyramidsStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="Taj Mahal":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=tajmahalStamps
            if stampsize=="medium":
                stamp=tajmahalStamp
            if stampsize=="large":
                stamp=tajmahalStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="Louvre":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=louvreStamps
            if stampsize=="medium":
                stamp=louvreStamp
            if stampsize=="large":
                stamp=louvreStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="cherry blossoms":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=blossomStamps
            if stampsize=="medium":
                stamp=blossomStamp
            if stampsize=="large":
                stamp=blossomStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))

        if tool=="tree":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=treeStamps
            if stampsize=="medium":
                stamp=treeStamp
            if stampsize=="large":
                stamp=treeStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="Eiffel Tower":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=eiffelStamps
            if stampsize=="medium":
                stamp=eiffelStamp
            if stampsize=="large":
                stamp=eiffelStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="Leaning Tower of Pisa":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=leaningStamps
            if stampsize=="medium":
                stamp=leaningStamp
            if stampsize=="large":
                stamp=leaningStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="Taipei 101":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=taipeiStamps
            if stampsize=="medium":
                stamp=taipeiStamp
            if stampsize=="large":
                stamp=taipeiStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
        if tool=="Merlion":
            screen.blit(back,(0,0))
            if stampsize=="small":
                stamp=merlionStamps
            if stampsize=="medium":
                stamp=merlionStamp
            if stampsize=="large":
                stamp=merlionStampl
            ssz=stamp.get_size()
            screen.blit(stamp,(mx-ssz[0]//2,my-ssz[1]//2))
            
        if tooltype=="text":
            tool="text"
            #new tx,ty everytime mouse is pressed on the canvas
            tx=mx
            ty=my
            if font=="none":
                font="courier"#makes courier the default font
            
        free=False
        screen.set_clip(None)#modify entire screen

    #--------------------WHEN MOUSE IS RELEASED IN THE CANVAS---------------------------------
    #UNDO/REDO & POLYGON TOOL
    if canvasRect.collidepoint(mx,my) and mb[0]==0 and done==False and tool!="text":
        undoArray.append(screen.subsurface(canvasRect).copy())#add screen capture to undo array when something is done on the canvas
        redoArray=[]#clears redo array
        done=True
        #----irregular (polygon) tool----
        if tool=="irregular" or tool=="filled irregular":
            if icount==0:#add first coordinate to the iArray
                iArray.append((mx,my))
                icount+=1
            else: #add coordinate to iArray and draw a line to the previous point
                iArray.append((mx,my))
                draw.aaline(screen,col,iArray[icount-1],iArray[icount],1)
                icount+=1

        
    elif canvasChanged==True and mb[0]==0:#for situations where tools such as fill,bkgs,new were used
        undoArray.append(screen.subsurface(canvasRect).copy())
        redoArray=[]#empty redoArray after something is added to the undo array
        done=True
        canvasChanged=False

           
    #------------------RIGHT CLICK ON CANVAS-------------------
    if canvasRect.collidepoint(mx,my) and mb[2]==1:
        screen.set_clip(canvasRect)
        if tool=="irregular" or tool=="filled irregular":
            if icount>2:#if there are more than three points then a polygon can be formed
                draw.aaline(screen,col,iArray[0],iArray[icount-1],1)
            if tool=="filled irregular" and len(iArray)>2:
                draw.polygon(screen,col,iArray)
        iArray=[]#clear iArray after a polygon is closed
        icount=0

        free=False
        screen.set_clip(None)#modify entire screen
        
    #------------------select or change the colour--------------------
    if palRect.collidepoint(mx,my) and mb[0]==1 and free==True and randc==False:
        col=screen.get_at((mx,my))#gets colour at the current pixel
        draw.rect(screen,col,currentRect)#update current colour display

    if randc==True:#generate a random colour if random tool is on
        col=(randint(0,255),randint(0,255),randint(0,255))
        
    if currentRect.collidepoint(mx,my) and mb[0]==1 and free==True and pressed==False:
        pressed=True#makes pressed true when mouse is pressing the colour display
        
    if currentRect.collidepoint(mx,my) and mb[0]==0 and free==True and pressed==True:
        if randc==False:#if the current mode is the normal colour one, want to change it to the random generated colour mode
            col=(randint(0,255),randint(0,255),randint(0,255))
            screen.blit(randomcPic,(249,0))#blit the colourful palette
            pressed=False
            randc=True#make randc true so random colours can be generated 
        else:# if current mode is the random colour one, want to change it to the normal colour mode
            randc=False
            draw.rect(screen,col,currentRect)#shows the current colour
            pressed=False

    display.flip()
    omx,omy=mx,my
            
quit() #closing the pygame window
