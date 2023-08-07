from QueueClass import Queue
qu = Queue()

def main(str):
    for char in str:
        qu.enqueue(char)
        
    rev=""
    
    while not qu.is_empty():
        rev+= qu.dequeue()
    r=""   
    if rev==str:
        r=f"the word {str} is palindrome"
    else:
        r=f"the word {str} is not"
    return r

    
print(main('min'))
print(main('civic'))
