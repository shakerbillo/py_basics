food = ['Jollof Rice','Soup', 'Rice and Stew', 'Fufu', 'Fried Rice', 'Steak']

for idx, item in enumerate(food):
    print(idx, item)
    
print('................................................................')
    
favorites = ['Manchester United', 'Bob Marley', 'Tupac Shakur', 'Lakers', 'Tema']

count = 0
while count < len(favorites):
    print('I like', favorites[count])
    count += 1

print('................................................................')
    
    
desserts = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for item in desserts:
    if item == 'Churros':
        continue 
    print('Other desserts I like are', item) 
    
