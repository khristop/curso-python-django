bri=set(['Brazil','Rusia','India'])
print('India' in bri)
print('Usa' in bri)
bric=bri.copy()
bric.add('China')
print('\nSet: ',bric)
bric.add('Brazil')
print('\n the new set is: ',bric)#No incluye objetos repetidos
print(bric & bri)


         
