def helloWorld():
    '''
    One of the most complex applications involving many years of research
    '''
    print 'Hello World!'

def greetings():
    '''
    Welcomes you
    '''
    name = raw_input('What is your name? ')
    print 'Hello %s!' % (name)
    
def newGreetings():
    '''
    only greets you if your name is Alice
    '''
    name = raw_input('What is your name? ')
    if name == 'Alice' or name == 'Bobby':
        print 'Hello %s!' % (name)
        
def numberSum(n):
    '''
    sums all numbers up to n
    '''
    ans = 0
    while n > 0:
        ans += n
        n -= 1
    print ans

def newNumberSum(n):
    '''
    This one only adds numbers divisible by 3 and 5
    '''
    ans = 0
    while n > 0:
        if n%3 == 0 or n%5 == 0:
            ans += n
        n -= 1
    print ans
    
def prodOrSum():
    '''
    gets the product or some of an inputed number
    '''
    ans = 1
    num = int(raw_input('Enter a number:'))
    choice = raw_input('Multiply or add?')
    if choice == 'multiply':
        for i in range(1,num+1):
            print i
            ans *= i
    elif choice == 'add':
        for i in range(2,num+1):
            ans += i
    else:
        print 'Please enter valid input!'
    print ans

def multiTable():
    '''
    creates a 12x12 multiplication times table
    '''
    foo = '\t'
    for i in range(1,13):
        print
        for j in range(1,13):
            print foo + str(i*j),
            
def genPrime():
    '''
    spams primes out
    '''
    def primer():    
        primes  = [] 
        last = 1
        while True:
            last += 1
            for p in primes:
    	        if last % p == 0: #It's a prime!
                    break
            else:
                primes.append(last)
                yield last
    def getPrimer():
        foo = primer()
        while True:
            print foo.next()
    getPrimer()
    
def guess():
    '''
    Try and guess a number between 1 and 100
    '''
    from random import random
    num = int(random()*100) #Creates a random number up to 100
    guesses = []
    while True:
        guess = raw_input('Enter your guess!')
        if guess in guesses: #asks for a new number if already guessed
            continue
        for i in guess: #checks if it's a number
            if not i in '0123456789':
                print 'enter a number!'
                break
        guesses.append(guess)
        if int(guess) == num:
            print 'You guess correct! It took you %s guesses' % (len(guesses))
            return
        elif len(guesses) > 1: #Needs to be at least one guess
            if abs(int(guesses[-2]) - num) < abs(int(guess) - num):
                print 'colder'
            else:
                print 'warmer'
        else:
            print 'Wrong' #First time through response
    
def boxer(wordList, design):
    '''
    wordList = **list** of words to be boxed
    design = single character to make up the box
    '''
    longestWord = 0
    for i in wordList: #Size of box
        if len(i) > longestWord:
            longestWord = len(i)
            
    for i in wordList:
        if i is wordList[0]:
            print design*longestWord + 4*design
        print (design + ' ' + i + ((longestWord - len(i))* ' ') + ' ' + design)
        if i is wordList[-1]:
            print design*longestWord + 4*design
            
def pigLatin(wordList):
    '''
    takes a list of words and pig latinizes it
    '''
    for i in wordList:
        old = i[1:] + i[0] + 'ay'
        print old + ' ',
        

    