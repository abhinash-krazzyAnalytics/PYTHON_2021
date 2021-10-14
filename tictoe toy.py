# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:29:34 2021

@author: abhinash.mishra
"""

b = [" " for i in range(9)]
b

def print_board():
    row1 = "|{}|{}|{}|".format(b[0],b[1],b[2])
    row2 = "|{}|{}|{}|".format(b[3],b[4],b[5])
    row3 = "|{}|{}|{}|".format(b[6],b[7],b[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    
    

def change_icon(ic):
    if ic=="X":
        print("Your turn player 1")
    else:
        print("Your turn player 2")
    ch = int(input("Enter your move (1-9): ").strip())
    if b[ch-1]==" ":
        b[ch-1]=ic
    else:
        print()
        print("that place is already filled")

def is_draw():
    if " " not in b:
        return True
    else:
        return False

def is_victory(ic):
    if (b[0]==ic and b[1]==ic and b[2]==ic) or \
       (b[3]==ic and b[4]==ic and b[5]==ic) or \
       (b[6]==ic and b[7]==ic and b[8]==ic) or \
       (b[1]==ic and b[4]==ic and b[7]==ic) or \
       (b[0]==ic and b[3]==ic and b[6]==ic) or \
       (b[2]==ic and b[5]==ic and b[8]==ic) or \
       (b[0]==ic and b[4]==ic and b[8]==ic) or \
       (b[2]==ic and b[4]==ic and b[6]==ic):
           return True
    else:
        return False
        
        

while True:
    print_board()
    change_icon("X")
    print_board()
    if is_victory("X"):
        print("Player 1 wins: ")
        break
    elif is_draw():
        print("No one win")
        break
    change_icon("O")
    if is_victory("O"):
        print_board()
        print("Player 2 wins: ")
        break
    
        
    