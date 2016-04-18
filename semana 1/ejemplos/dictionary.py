ab={'Swaroop':'swarooppc@hola.com','Larry':'larry@yahoo.org','Matsumoto':'matsumoto@hotmail.org'}
print('swaroop is: ',ab['Swaroop'])
ab['Guido'] = 'guido@python.org'
print('\n\n')
for name,address in ab.items():
    print('Contac: {} at {}'.format(name,address))
print('\nif Guido in ab: \n')
if 'Guido' in ab:
    print('Guido\'s address is: ',ab['Guido'])

print('\n\n')    
del ab['Swaroop']
for name,address in ab.items():
    print('Contac: {} at {}'.format(name,address))

