while True:
    s=input('enter something: ')
    if s=='quit':
        break
    if len(s)<3:
        print('too small')
        continue
    print('it is sufficient length')
print('Done')

