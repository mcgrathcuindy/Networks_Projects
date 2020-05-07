"""
NAME: Christopher McGrath
DATE: 1/16/20
DESC: Statistics on a data set in python, Function will end when CTRL + C is entered
"""
from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print("{} values entered".format(len(lst)))
    print("{} was the minimum value".format(min(lst)))
    print("{} was the maximum value".format(max(lst)))
    print("{} was the sum".format(sum(lst)))
    least_frequent(lst)
    most_frequent(lst)
    exit(0)

def most_frequent(lst): 
    Dict = {} 
    for i in lst: 
        if (i in Dict): 
            Dict[i] += 1
        else: 
            Dict[i] = 1
            
    MaxValue = max(Dict.items(), key=lambda x: x[1]) 
    KeyList = list()
    # Iterate over all the items in dictionary to find keys with max value
    for key, value in Dict.items():
        if value == MaxValue[1]:
            KeyList.append(key)
    print("Most mentioned numbers (repeated {} times)".format(MaxValue[1]), end =" ")
    print(KeyList)
    
def least_frequent(lst):
    Dict = {} 
    for i in lst: 
        if (i in Dict): 
            Dict[i] += 1
        else: 
            Dict[i] = 1
            
    MinValue = min(Dict.items(), key=lambda x: x[1]) 
    KeyList = list()
    # Iterate over all the items in dictionary to find keys with max value
    for key, value in Dict.items():
        if value == MinValue[1]:
            KeyList.append(key)
    print("Least mentioned numbers (repeated {} times)".format(MinValue[1]), end =" ")
    print(KeyList) 

value = 0

lst = [] 

if __name__ == '__main__':
    signal(SIGINT, handler)

    while True:
        value = int(input())
        lst.append(value)
            
        pass
    