number=23
guess=int(input('enter an integer: '))

if guess==number:
    print('congratulation, you guessed it')
    print('But you do not win any prizes')
elif guess<number:
    print('No, it is a litle higher than that')
else:
    print('No, it is a litle lower than that')
print('program finished succeful')

    
