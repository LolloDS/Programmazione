x= input('inserire prima stringa ')
y= input('inserire seconda stringa ')

def filtro(stringa, stringa_filtro):
	caratteri_comuni=""
	for c in stringa:
		if c in stringa_filtro:
			caratteri_comuni+=c
	return caratteri_comuni

print(filtro(x,y))