#pizza app
am1='vibhu61'
am1pas='12345'


u1='vibhansh'
u1pas='321'

count=10

print("\n--------------------Welcome to JOE's PIZZA------------------")
print("		Enter 'A' or 1 if you're an Admin\n")
print("		Enter 'U' or 2 if you're a User\n")
print("		Enter 'E' or 3 if you want to exit")

au=input('\nEnetr : ')

if (au=='A' or au=='a' or au=='1'):
	
	print('!!! WELCOME TO ADMIN PANEL !!!')
	print('		Enter login details: ')
	a1=input('enter id: ')
	a1pas=input('enter password: ')
	while 1:	
		if( a1==am1 and a1pas==am1pas ):
			
			print(" \n-----------------------Welcome admin-------------------------\n")
		
			print('\n	1. View Stocks	')
		
			print('\n	2. Manage Stock	')
			
			print('\n	3. logout and exit')
			ch=int(input('\nenter any option above: '))
			if ch==1:
				print('number of pizza available- ',count)
				print()
			elif ch==2:
				a=int(input('enter new amount of pizza available: '))
				count=a
			elif ch==3:
				print('\n	----------- THANK YOU FOR USING THE APP	-------------------\n')
				break
		else:
			print('user id or password incorrect')
			break
			
elif (au== 'U' or au=='u' or au=='2'):
	print('!!! WELCOME USER !!!')
	
elif (au== 'E' or au=='e' or au=='3'):
	print('\n	----------- THANK YOU FOR USING THE APP	-------------------\n')
	
else:
	print('Enter valid option')
		
	
	
	
	
	
	
	
	
	
