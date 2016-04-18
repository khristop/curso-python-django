running=True
number=23
while running:
    guess=int(input('Ingrese un valor entero'))
    if guess==number:
        print('Congratulation, you gessed it')
        running=False
    else:
        print('you do not guessed it. Try again')
else:# can have an else clause for the while loop
    print('Finished')
print('Done')
    
               

                   


              
