def contarLetras(*parametros):
	diccionario = {}
	for palabra in parametros:
		for letra in palabra:
			if(letra in diccionario):
				diccionario[letra] += 1
			else:
				diccionario[letra] = 1
	return diccionario
