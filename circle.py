def circ_area_circf(ra):
	return[3.14*ra*ra,2*3.14*ra]

r=int(input("enter the radius of circle"))

out1,out2=circ_area_circf(r)
print("\nthe area of circle is=",out1,"\nthe circumference of circle is=",out2)
