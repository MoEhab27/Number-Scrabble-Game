#----------------------------------------------------------------------------------
# ---------------------------Number Scrabble Game----------------------------------
# --------------------------------------------------------------------------------- 
# The first player who collects 3 numbers which add  up to 15 wins the game
# Each player are allowed to play 4 time only 
# If there's 8 turns and no one wins, then the game is draw
# V 0.1
# By : Mohamed Ehab Tawfik ----- ID : 20210331
#Under The Supervision of: Dr. Mohamed El-Ramly
#-----------------------------------------------------------------------------------
# IMPORTANT Note :
# To run the game properly go to file > open folder > and choose the folder " Number Scrabble "


import pygame
import os

numsTop, numsBot = [1, 2, 3, 4, 5], [6, 7, 8, 9]
players, player1, player2 = [], [], []
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Scrabble")

FPS = 60

#------------------------------
#-----Importing the assest-----
#------------------------------

# Players Wins 
P1, P2 = pygame.image.load(os.path.join('Assets', 'PLR1.png')), pygame.image.load(os.path.join('Assets', 'PLR2.png'))
DRW, AGAIN = pygame.image.load(os.path.join('Assets', 'DRW.png')), pygame.image.load(os.path.join('Assets', 'AGAIN.png'))

fif = pygame.image.load(os.path.join('Assets', 'fifteen.png'))
pygame.display.set_icon(fif)

# Yellow Numbers
Y1, Y2 = pygame.image.load(os.path.join('Assets', '1Y.png')), pygame.image.load(os.path.join('Assets', '2Y.png'))
Y3, Y4 = pygame.image.load(os.path.join('Assets', '3Y.png')), pygame.image.load(os.path.join('Assets', '4Y.png'))
Y5, Y6 = pygame.image.load(os.path.join('Assets', '5Y.png')), pygame.image.load(os.path.join('Assets', '6Y.png'))
Y7, Y8, Y9 = pygame.image.load(os.path.join('Assets', '7Y.png')), pygame.image.load(os.path.join('Assets', '8Y.png')), pygame.image.load(os.path.join('Assets', '9Y.png'))
yNums = [Y1 ,Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9]
shownY = []

# Blue Numbers 
B1, B2 = pygame.image.load(os.path.join('Assets', '1B.png')), pygame.image.load(os.path.join('Assets', '2B.png'))
B3, B4 = pygame.image.load(os.path.join('Assets', '3B.png')), pygame.image.load(os.path.join('Assets', '4B.png'))
B5, B6 = pygame.image.load(os.path.join('Assets', '5B.png')), pygame.image.load(os.path.join('Assets', '6B.png'))
B7, B8, B9 = pygame.image.load(os.path.join('Assets', '7B.png')), pygame.image.load(os.path.join('Assets', '8B.png')), pygame.image.load(os.path.join('Assets', '9B.png'))
bNums = [B1, B2, B3, B4, B5, B6, B7, B8, B9]
shownB = []

# White Numbers 
W1, W2 = pygame.image.load(os.path.join('Assets', '1W.png')), pygame.image.load(os.path.join('Assets', '2W.png'))
W3, W4 = pygame.image.load(os.path.join('Assets', '3W.png')), pygame.image.load(os.path.join('Assets', '4W.png'))
W5, W6 = pygame.image.load(os.path.join('Assets', '5W.png')), pygame.image.load(os.path.join('Assets', '6W.png'))
W7, W8, W9 = pygame.image.load(os.path.join('Assets', '7W.png')), pygame.image.load(os.path.join('Assets', '8W.png')), pygame.image.load(os.path.join('Assets', '9W.png'))
wNums = [W1, W2, W3, W4, W5, W6, W7, W8, W9]
topRow, botRow = wNums[0:5], wNums[5:9]

BG = pygame.image.load(os.path.join('Assets', 'BG.png'))
liTop, liBot = [], []

def nothing(): # Function to reset all the variable so whe the try again button is clicked the game restarts 
    global liTop, liBot, topRow, botRow, wNums, bNums, yNums, topB, botB, shownB,topY, botY, shownY, numsBot, numsTop, player1, players, player2
    wNums = [W1, W2, W3, W4, W5, W6, W7, W8, W9]
    topRow, botRow = wNums[0:5], wNums[5:9]
    bNums = [B1, B2, B3, B4, B5, B6, B7, B8, B9]
    yNums = [Y1 ,Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9]
    numsTop, numsBot = [1, 2, 3, 4, 5], [6, 7, 8, 9]
    players, player1, player2, shownY, shownB, liBot, liTop= [], [], [], [], [], [], []

def Again():           # Displays the tryagain button if someone won or if the game draw
    if checkWin(player1) or checkWin(player2) or gameDraw():
        WIN.blit(AGAIN, (522, 563))

def drawGame():   # The function which displays all the assets on the sreen
    global liBot, liTop
    WIN.blit(BG,(0, 0))  # the background of the game
    wWidth = 420
    for i in topRow:  # The top white row of the game 
        WIN.blit(i, (wWidth, 318))
        b = pygame.Rect(wWidth, 318, 70, 70)
        liTop.append(b) # appending the assets in a list to display them on the screen
        wWidth += 93
    wWidth = 466
    for i in botRow:  # the bot white row of the game 
        b = pygame.Rect(wWidth, 409, 70, 70)
        liBot.append(b)
        WIN.blit(i, (wWidth, 409))
        wWidth += 93

    bHeight = 220  
    for i in shownB:       #Blues Display
        WIN.blit(i, (1025, bHeight))
        bHeight += 91

    bHeight = 220
    for i in shownY:    # Yellows display
        WIN.blit(i, (183, bHeight))
        bHeight += 91

    if checkWin(player1):  # checks if someone won to  end the game 
        WIN.blit(P1, (330, 228))
    elif checkWin(player2):
        WIN.blit(P2, (330, 228)) 
    if gameDraw():
        WIN.blit(DRW, (330, 228))
    Again()      # shows the try again button
    if gameDraw() or checkWin(player1) or checkWin(player2):
        liBot = []
        liTop = []
    pygame.display.update()

tryAgain = pygame.Rect(522, 563, 236, 82)

def updatePlayers(y):         # Append yellow and blue Buttons in the showing lists when player click them
    if len(players) % 2 !=0 : # append Yellow
        shownY.append(yNums[y-1])
    else:                     # append Blue
        shownB.append(bNums[y-1])                      

def checkWin(i):              # Check if there's a winners from players lists 
    if len(i) == 4:
        if i[0] + i[1] + i[3] ==15 or i[0] + i[2] + i[3] ==15 or i[1] + i[2] +i[3] == 15:
            return True
    if len(i) == 3:
        if i[0] + i[1] + i[2] == 15:
            return True

def gameDraw():               # Check if every player played 4 times and no one won 
    if len(player1) == 4 and len(player2) == 4:
        if not checkWin(player1) and not checkWin(player2):
            return True

def appending(player1, player2, players, y):    # Appends numbers in player lists " DataBase " so we can check win on them
    players.append(y)
    if len(players) % 2 != 0:
        player1.append(y)
    else:
        player2.append(y)
    print(f"\nPlayer One Set Is : {player1} \nPlayer Two Set Is : {player2} \nPicked Numbers Are : {players}\n")  # Prints the database

def mouseClick(event):             # Mouse Click Function
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if tryAgain.collidepoint(mouse):    # if try again button clicked it calls the reset function to reset the game
            nothing()
        try:
            for i in liTop:
                if i.collidepoint(mouse): # checks where the mouse clicked to assign a number
                    x = liTop.index(i)  
                    del topRow[x]           # Deletes the chosen number from tha main list and appends it in a player list
                    y = numsTop[x]
                    del numsTop[x]
                    appending(player1, player2, players, y)    # appends the moved number in a list where we chick if someone won
                    updatePlayers(y)        # moves the chosen number to a player side 
                    break
# since i have to rows in the game i had to do two for loops each one to display each row
            for i in liBot:
                if i.collidepoint(mouse): 
                    x = liBot.index(i)          # Same stuff but with the lower row XD
                    del botRow[x]
                    y = numsBot[x]
                    del numsBot[x]
                    appending(player1, player2, players, y)
                    updatePlayers(y)
                    break         
        except:
            pass

def main():             # The main function to run the game 
    clock = pygame.time.Clock()
    run = True 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False 
            mouseClick(event)
        drawGame()
    pygame.quit()

if __name__ == "__main__":
    main()

