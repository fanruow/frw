#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:44:03 2019

@author: wfr
"""

# 1
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 != 0:
        return 3 * number + 1
    
def collatz_sequence(number):
    seq = []
    while number != 1 :
        number = collatz(number)
        seq = seq + [number]
    return seq

# validation
assert( collatz(3)==10)
assert( collatz(2)==1)

# validation
assert(collatz_sequence(10)==[5, 16, 8, 4, 2, 1])

# 2
def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
        
# validation
assert(is_number(7)==True)
assert(is_number(7.0)==True)
assert(is_number('7')==True)
assert(is_number('puppy')==False)

# 3
def merge_strings(l):
    string = ''
    for i in range(len(l)-1):
        string = string + l[i] + ', '
    string = string + 'and ' + l[len(l)-1]
    return string    


# validation
assert(merge_strings(['apples', 'bananas', 'tofu', 'cats'])=='apples, bananas, tofu, and cats')       


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def print_grid(grid): 
    pg=''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pg += grid[i][j]
        pg += '\n'
    print(pg)

print_grid(grid)='......\n.OO...\nOOOO..\nOOOOO.\n.OOOOO\nOOOOO.\nOOOO..\n.OO...\n......\n'


def rotate_grid(grid):        
    rg=[[0] * len(grid) for row in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            rg[j][i]=grid[i][j]
    return rg

rg[i].append(grid[i][j])
print_grid(rotate_grid(grid))  
    
    
    






#5
def displayInventory(inventory):
    key = list(inventory.keys())
    key.sort()
    num = 0
    print('Inventory:')
    for i in range(len(key)):
        num += inventory[key[i]]
        print(inventory[key[i]],' ',key[i])
    print('Total number of items:',num)
    
displayInventory(inventory)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
    print(inventory['rope'],' ','rope')
    
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
        else:
            inventory[addedItems[i]] = 1
    return inventory
            
displayInventory()
            
#7
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

rjust() 

def printTable(tbl):
    colWidths = [0] * len(tbl)
    for i in range(len(tbl)):
        l=[]
        for j in range(len(tbl[i])):
            l.append(len(tbl[i][j]))
        colWidths[i] = max(l)  
    for j in range(len(tbl[i])):
        ptbl = ''
        for i in range(len(tbl)):
            ptbl = ptbl+tbl[i][j].rjust(colWidths[i])+' '
        print(ptbl)
    
    
printTable(tableData)
    print(tableData[0][1].rjust(colWidths[0]))
    
    
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        l=[]
        for j in range(len(tableData[i])):
            l.append(len(tableData[i][j]))
        colWidths[i] = max(l)
    for j in range(len(tableData[i])):
        for i in range(len(tableData)):
            print(tbl[i][j].rjust(colWidths[i]))
            
            
            
# 8
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

def encrypt(s,n):
    cipher = ''
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    for i in range(len(s)):
        if s[i] in alphabet1:
            cipher += alphabet1[(alphabet1.index(s[i])+n)%(len(alphabet1))]
        elif s[i] in alphabet2:
            cipher += alphabet2[(alphabet2.index(s[i])+n)%(len(alphabet2))]
        else:
            cipher += s[i]
    return cipher

s='zEbra !'
n=1
encrypt(s,n)  
      

def decrypt(s, n):
    cipher = ''
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    for i in range(len(s)):
        if s[i] in alphabet1:
            cipher += alphabet1[(alphabet1.index(s[i])-n)%(len(alphabet1))]
        elif s[i] in alphabet2:
            cipher += alphabet2[(alphabet2.index(s[i])-n)%(len(alphabet2))]
        else:
            cipher += s[i]
    return cipher

s='aFcsb !'
decrypt(s,1)

# 2）
def encode_text_file(input_file_plain, output_file_encoded, n, encoding='utf-8'):
    fr = open(input_file_plain,"r")   
    str = fr.read()  
    encrypt(str,n)
    with open(output_file_encoded,'w') as fw:    
        fw.write(str)

# 9
import re

def test_password(s):
    # beyond the number and digital
    NumDigRegex = re.compile(r'[^0-9a-zA-Z]')
    
    # length larger than 8
    LenRegex = re.compile(r'[0-9a-zA-Z]{8,}')
    
    # both Ucase and Lcase
    UcaseRegex = re.compile(r'[A-Z]')
    LcaseRegex = re.compile(r'[a-z]')
    
    # at least 1 digital
    DigRegex = re.compile(r'[0-9]')
    
    if NumDigRegex.search(s) != None:
        #print('only letter or digital allows')
        return False
    elif LenRegex.search(s) == None:
        #print('length of password lower than 8')
        return False
    elif UcaseRegex.search(s) == None:
        #print('At least one Ucase letter')
        return False
    elif LcaseRegex.search(s) == None:
        #print('At least one Lcase letter')
        return False
    elif DigRegex.search(s) == None:
        #print('At least one Digital')
        return False   
    return True
 
# Enter the password 
password = 'helloWorld9\n'
 
# Show the result
print('')
print(test_password(password))

            


    