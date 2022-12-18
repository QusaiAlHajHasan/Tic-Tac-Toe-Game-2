# Name : Qussai Al-Hajj Hasan , ID : 121075
# Name : Sarah Shuqairat , ID : 113343

from math import inf as infinity
from random import choice
import random
from array import *

################################################################## TicTacToe Class ###################################################################

class TicTacToe:
        def __init__(self,depth):
                self.__board = [['','',''],['','',''],['','','']]
                self.__Computer = 'X'
                self.__Human = 'O'
                self.__Depth = depth

################################################################## Draw_Board Method #################################################################
                
        def Draw_Board(self):
                print('    |    |    ')
                print(' ' + self.__board[0][0] + '    ' + self.__board[0][1] + '    ' + self.__board[0][2])
                print('    |    |    ')
                print('---------------')
                print('    |    |    ')
                print(' ' + self.__board[1][0] + '    ' + self.__board[1][1] + '    ' + self.__board[1][2])
                print('    |    |    ')
                print('---------------')
                print('    |    |    ')
                print(' ' + self.__board[2][0] + '    ' + self.__board[2][1] + '    ' + self.__board[2][2])
                print('    |    |    ')

################################################################# Clear_Board Method #################################################################
                
        def Clear_Board(self):
                for i in range(0,3):
                        for j in range(0,3):
                                self.__board[i][j] = ''

################################################################## Check_Win Method ##################################################################
                                
        def Check_Win(self,l):
                return ((self.__board[0][0] == l and self.__board[0][1] == l and self.__board[0][2] == l) or
                        (self.__board[1][0] == l and self.__board[1][1] == l and self.__board[1][2] == l) or
                        (self.__board[2][0] == l and self.__board[2][1] == l and self.__board[2][2] == l) or
                        (self.__board[0][0] == l and self.__board[1][0] == l and self.__board[2][0] == l) or
                        (self.__board[0][1] == l and self.__board[1][1] == l and self.__board[2][1] == l) or
                        (self.__board[0][2] == l and self.__board[1][2] == l and self.__board[2][2] == l) or
                        (self.__board[0][0] == l and self.__board[1][1] == l and self.__board[2][2] == l) or
                        (self.__board[0][2] == l and self.__board[1][1] == l and self.__board[2][0] == l))

################################################################ Is_Index_Free Method ################################################################
            
        def Is_Index_Free(self , x , y):
                if x<=2 and x>=0 and y<=2 and y>=0:
                        if self.__board[x][y] == '':
                                return True
                return False

################################################################### New_Game Method ##################################################################
            
        def New_Game(self):
                print('Do Want To Play Again (Y : Yes , N : No) :')
                return input().lower()

################################################################## Check_Tie Method ##################################################################
            
        def Check_Tie(self):
                for i in range(0,3):
                        for j in range(0,3):
                                if self.Is_Index_Free(i,j):
                                        return False
                                return True

############################################################### Get_Player_Move Method ###############################################################
                            
        def Get_Player_Move(self):
                print('Enter your move (row[0-2] column[0-2]):')
                x , y = input().split()
                return x , y

################################################################## Make_Move Method ##################################################################
            
        def Make_Move(self , x , y, l):
                self.__board[x][y] = l

############################################################### MinMax_Decision Method ###############################################################
                
        def MinMax_Decision(self,state):
                U = self.Max_Value(0,state)
                child = []
                action = []
                action , child = self.Successors(state,self.__Human)
                for i in child:
                                U2 = self.Evaluation(child[i])
                                if U == U2:
                                        return action[i][j]
                return -1
                
################################################################## Max_Value Method ##################################################################
    
        def Max_Value(self,ut,state):
                counter = 1
                if self.Terminal_Test(state,counter):
                        return self.Evaluation(state)
                U = -9999
                child = []
                action = []
                action , child = self.Successors(state,self.__Human)
                for children in child:
                	U2 = self.Evaluation(children)
                	U = max(U,self.Min_Value(U2,children))
                	counter += 2
                return U

################################################################## Min_Value Method ##################################################################
            
        def Min_Value(self,ut,state):
            counter = 2
            if self.Terminal_Test(state,counter):
                return self.Evaluation(state)
            U = +9999
            child = []
            action = []
            action , child = self.Successors(state,self.__Human)
            for children in child:
                U2 = self.Evaluation(children)
                U = min(U,self.Max_Value(U2,children))
                counter += 2
            return U

################################################################## Evaluation Method #################################################################
            
        def Evaluation(self,state):
                Computer_Utility = self.Computer_Possible_Wins(state)
                Human_Utility = self.Human_Possible_Wins(state)
                Utility = Computer_Utility - Human_Utility
                return Utility

############################################################ Computer_Possible_Wins Method ###########################################################
            
        def Computer_Possible_Wins(self,state):
                count = 8
                if state[0][0] == self.__Human or state[0][1] == self.__Human or state[0][2] == self.__Human:
                        count -= 1
                if state[1][0] == self.__Human or state[1][1] == self.__Human or state[1][2] == self.__Human:
                        count -= 1
                if state[2][0] == self.__Human or state[2][1] == self.__Human or state[2][2] == self.__Human:
                        count -= 1
                if state[0][0] == self.__Human or state[1][0] == self.__Human or state[2][0] == self.__Human:
                        count -= 1
                if state[0][1] == self.__Human or state[1][1] == self.__Human or state[2][1] == self.__Human:
                        count -= 1
                if state[0][2] == self.__Human or state[1][2] == self.__Human or state[2][2] == self.__Human:
                        count -= 1
                if state[0][0] == self.__Human or state[1][1] == self.__Human or state[2][2] == self.__Human:
                        count -= 1
                if state[0][2] == self.__Human or state[1][1] == self.__Human or state[2][0] == self.__Human:
                        count -= 1
                return count

############################################################# Human_Possible_Wins Method #############################################################
            
        def Human_Possible_Wins(self,state):
                count = 8
                if state[0][0] == self.__Computer or state[0][1] == self.__Computer or state[0][2] == self.__Computer:
                        count -= 1
                if state[1][0] == self.__Computer or state[1][1] == self.__Computer or state[1][2] == self.__Computer:
                        count -= 1
                if state[2][0] == self.__Computer or state[2][1] == self.__Computer or state[2][2] == self.__Computer:
                        count -= 1
                if state[0][0] == self.__Computer or state[1][0] == self.__Computer or state[2][0] == self.__Computer:
                        count -= 1
                if state[0][1] == self.__Computer or state[1][1] == self.__Computer or state[2][1] == self.__Computer:
                        count -= 1
                if state[0][2] == self.__Computer or state[1][2] == self.__Computer or state[2][2] == self.__Computer:
                        count -= 1
                if state[0][0] == self.__Computer or state[1][1] == self.__Computer or state[2][2] == self.__Computer:
                        count -= 1
                if state[0][2] == self.__Computer or state[1][1] == self.__Computer or state[2][0] == self.__Computer:
                        count -= 1
                return count

############################################################# Check_Win_Terminal Method ##############################################################
                                
        def Check_Win_Terminal(self,state,l):
                return ((state[0][0] == l and state[0][1] == l and state[0][2] == l) or
                        (state[1][0] == l and state[1][1] == l and state[1][2] == l) or
                        (state[2][0] == l and state[2][1] == l and state[2][2] == l) or
                        (state[0][0] == l and state[1][0] == l and state[2][0] == l) or
                        (state[0][1] == l and state[1][1] == l and state[2][1] == l) or
                        (state[0][2] == l and state[1][2] == l and state[2][2] == l) or
                        (state[0][0] == l and state[1][1] == l and state[2][2] == l) or
                        (state[0][2] == l and state[1][1] == l and state[2][0] == l))

############################################################# Check_Tie_Terminal Method ##############################################################
            
        def Check_Tie_Terminal(self,state):
                for i in range(0,3):
                        for j in range(0,3):
                                if self.Is_Index_Free_Terminal(state,i,j):
                                        return False
                                return True

########################################################### Is_Index_Free_Terminal Method ############################################################
            
        def Is_Index_Free_Terminal(self , state , x , y):
                if x<=2 and x>=0 and y<=2 and y>=0:
                        if state[x][y] == '':
                                return True
                return False
        
################################################################## Successors Method #################################################################
            
        def Successors(self,state,l):
                child = []
                action = []
                for i in range(0,3):
                        for j in range(0,3):
                                if self.Is_Index_Free(i,j):
                                        New_State = state.copy()
                                        New_State[i][j] = l
                                        child.append(New_State)
                                        action.append(self.Select_Action(i,j))
                return action,child

################################################################ Select_Action Method ################################################################

        def Select_Action(self,i,j):
            if i == 0 and j ==0:
                    return 0
            if i == 0 and j == 1:
                    return 1
            if i == 0 and j == 2:
                    return 2
            if i == 1 and j == 0:
                    return 3
            if i == 1 and j == 1:
                    return 4
            if i == 1 and j == 2:
                    return 5
            if i == 2 and j == 0:
                    return 6
            if i == 2 and j == 1:
                    return 7
            if i == 2 and j == 2:
                    return 8

############################################################### Action_Decision Method ###############################################################

        def Action_Decision(self,x):
            x = 0
            y = 1
            z = 2
            if x == 0:
                return x,x
            if x == 1:
                return x,y
            if x == 2:
                return x,z
            if x == 3:
                return y,x
            if x == 4:
                return y,y
            if x == 5:
                return y,z
            if x == 6:
                return z,x
            if x == 7:
                return z,y
            if x == 8:
                return z,z
                
################################################################ Terminal_Test Method ################################################################
                    
        def Terminal_Test(self,state,depth):
            if depth == self.__Depth:
                U = self.Evaluation(state)
                return U
            for i in range(0,3):
                for j in range(0,3):
                    if self.Check_Win_Terminal(state,self.__Computer) or self.Check_Win_Terminal(state,self.__Human):
                        U = self.Evaluation(state)
                        return U
                    elif self.Check_Tie_Terminal(state):
                        U = self.Evaluation(state)
                        return U

#################################################################### Play Method #####################################################################
    
        def Play(self):
                turn_num =1
                loop = True
                while loop:
                        if turn_num % 2 !=0 :
                                x = self.MinMax_Decision(self.__board)
                                a , b =  self.Action_Decision(x)
                                self.Make_Move(int(a) , int(b) , self.__Computer)
                                self.Draw_Board()
                                turn_num +=1
			
                        else :
                                a , b = self.Get_Player_Move()
                                while not self.Is_Index_Free(int(a) , int(b) ):
                                        print('This move is not valid. Try again…')
                                        a , b = self.Get_Player_Move()
                                self.Make_Move(int(a) , int(b) , self.__Human)
                                self.Draw_Board()
                                turn_num +=1
                                
                        if turn_num > 9 or self.Check_Win(self.__Computer) or self.Check_Win(self.__Human) :
                                loop = False
                if self.Check_Win(self.__Computer):
                        print('Computer Won.')
                elif self.Check_Win(self.__Human):
                        print('Human Won.')
                else :
                        print('Tied')
                        
##################################################################### Main Method ####################################################################
                        
def main():
        print('Welcome To Tic Tac Toe !\n')
        print("Enter The Depth(ply) Of The Game : ")
        D = input()					
        Game1 = TicTacToe(D)
        while True:
                Game1.Play()
                ans = Game1.New_Game()
                if ans == 'y':
                        Game1.Clear_Board()
                        continue
                else:
                        print('Thank You !')
                        break

main()
	
