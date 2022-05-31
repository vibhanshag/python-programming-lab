usr1='vibhansh'
usr1pass='vibhu123'

usr2='udit'
usr2pass='4582'

usr3='rohit'
usr3pass='r0hit'

usr4='sohil'
usr4pass='okok'


usrid=input('Enter ID ')
pasw=input('Enter Password ')


if ( usrid==usr1 and pasw==usr1pass ):
	print('welcome Vibhansh ')
elif ( usrid==usr2 and pasw==usr2pass ):
	print('welcome Udit ')
elif ( usrid==usr3 and pasw==usr3pass ):
	print('welcome Rohit ')
elif ( usrid==usr4 and pasw==usr4pass ):
	print('welcome Sohil ')
elif (usrid!=usr1 or usrid!=usr2 or usrid!=usr3 or usrid!=usr4 ):
	print('user does not exist')
else:
	print('invalid')
