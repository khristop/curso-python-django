shoplist=['apple','mango','carrot','banana']
print('I have ',len(shoplist),'intems to purchese ')
print('this items are:' )
for item in shoplist:
    print(item,)
print('I also have to buy rice')
shoplist.append('rice')

print('My shoplist is now: ',shoplist)

print('I have to sort my shoplist: ')
shoplist.sort()
print('the shoplist ordered is :',shoplist)
print('the last thing that I have to buy is: ',shoplist[4])

print('removing the first element')
del shoplist[0]
print('The list is now: ',shoplist)



      
