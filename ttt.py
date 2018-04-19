from random import *

f=True

while f:
    board=[0,1,2,
       3,4,5,
       6,7,8]

    def show():
         print(board[0],'|',board[1],'|',board[2])
         print('----------')
         print(board[3],'|',board[4],'|',board[5])
         print('----------')
         print(board[6],'|',board[7],'|',board[8])
         print('\n')
   


    
    def check(char,p1,p2,p3):
        if(board[p1]==char and board[p2]==char and board[p3]==char):
            return True
        else:
            return False
    
    def checkAll(char):
        if(check(char,0,1,2)):
            return True
        if(check(char,0,3,6)):
            return True
        if(check(char,0,4,8)):
            return True
        if(check(char,1,4,7)):
            return True
        if(check(char,2,5,8)):
            return True
        if(check(char,3,4,5)):
            return True
        if(check(char,6,7,8)):
            return True
        if(check(char,2,4,6)):
            return True
    
    print('WELCOME TO TIC TAC TOE GAME ; TEST YOUR BRAIN HERE \n')
    ch=input('press s for singleplayer and m for multiplayer game')
    show()
    if(ch=='s'):
        while True:
            flag=True
            while flag:
                 pos=int(input('your turn: please insert position'))
                 if(board[pos]!='x' and board[pos]!='o'):
                       board[pos]='x'
                       flag=False
                 else:
                     print('position already occupied')
            show()
        
            if(checkAll('x')):
                print('YIPPEE,YOU WON')
                break
            if((board[0]=='x' or board[0]=='o') and (board[1]=='x' or board[1]=='o') and (board[2]=='x' or board[2]=='o') and (board[3]=='x' or board[3]=='o') and (board[4]=='x' or board[4]=='o') and (board[5]=='x' or board[5]=='o') and (board[6]=='x' or board[6]=='o') and (board[7]=='x' or board[7]=='o') and (board[8]=='x' or board[8]=='o')):
                print('MATCH DRAWN')
                break
            flag=True
        
            while flag:
                pos=randint(0,8)
                if(board[pos]!='x' and board[pos]!='o'):
                       board[pos]='o'
                       flag=False
                   
            show()
        
            if(checkAll('o')):
                print('YOU LOST THE GAME')
                break

            if((board[0]=='x' or board[0]=='o') and (board[1]=='x' or board[1]=='o') and (board[2]=='x' or board[2]=='o') and (board[3]=='x' or board[3]=='o') and (board[4]=='x' or board[4]=='o') and (board[5]=='x' or board[5]=='o') and (board[6]=='x' or board[6]=='o') and (board[7]=='x' or board[7]=='o') and (board[8]=='x' or board[8]=='o')):
                print('match drawn')
                break
            
    elif(ch=='m'):
          while True:
            flag=True
            while flag:
                 pos=int(input('player 1 turn: please insert position'))
                 if(board[pos]!='x' and board[pos]!='o'):
                       board[pos]='x'
                       flag=False
                 else:
                     print('position already occupied')
            show()
        
            if(checkAll('x')):
                print('YIPPEE! PLAYER 1 WON')
                break
            if((board[0]=='x' or board[0]=='o') and (board[1]=='x' or board[1]=='o') and (board[2]=='x' or board[2]=='o') and (board[3]=='x' or board[3]=='o') and (board[4]=='x' or board[4]=='o') and (board[5]=='x' or board[5]=='o') and (board[6]=='x' or board[6]=='o') and (board[7]=='x' or board[7]=='o') and (board[8]=='x' or board[8]=='o')):
                print('MATCH DRAWN')
                break
            flag=True
        
            while flag:
                pos=int(input('player 2 turn: please insert position'))
                if(board[pos]!='x' and board[pos]!='o'):
                       board[pos]='o'
                       flag=False
                else:
                     print('position already occupied')
                
                   
            show()
        
            if(checkAll('o')):
                print('BRAVO! PLAYER 2 WON')
                break

            if((board[0]=='x' or board[0]=='o') and (board[1]=='x' or board[1]=='o') and (board[2]=='x' or board[2]=='o') and (board[3]=='x' or board[3]=='o') and (board[4]=='x' or board[4]=='o') and (board[5]=='x' or board[5]=='o') and (board[6]=='x' or board[6]=='o') and (board[7]=='x' or board[7]=='o') and (board[8]=='x' or board[8]=='o')):
                print('MATCH DRAWN')
                break
         
    
    again=input('try again: y or n')
    if(again=='n'):
        break

      
   
