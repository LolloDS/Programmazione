x=input('inserire testo operazione ')

def parse_and_calc(stringa) :
	i=0
	primo_numero=""
	secondo_numero=""
	operatore=""

	#tiro fuori il primo numero
	while i<len(stringa) and stringa[i] in '0123456789':
		primo_numero += stringa[i]
		i+=1
	print(primo_numero)#grafica

	#trovo un carattere che non é un numero
	if i>len(stringa) or stringa[i] not in '+*':return None #il carattere non é un operatore

	elif stringa[i] in '+*': #se il carattere é un operatore
		operatore+=stringa[i]
		i+=1
	print(operatore)#grafice

	while i<len(stringa) and stringa[i] in '0123456789':# tiro fuori il secondo numero
		secondo_numero += stringa[i]
		i+=1 
	print(secondo_numero, "=")#grafica
	if operatore=="+": return int(primo_numero)+int(secondo_numero)
	elif (operatore=="*"): return int(primo_numero)*int(secondo_numero)

risultato= parse_and_calc(x)

if type(risultato)==int:
	print(risultato)

else: print("errore nell'input")