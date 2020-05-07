"""
NAME: Christopher McGrath
DATE: 1/16/20
DESC: Box Maker in Python
"""

width = int(input("Enter the width:"))
height = int(input("Enter the height:"))
char = input("Enter the character:")

for i in range(height):
    for j in range(width):
        print(char, end = "")
    print()
