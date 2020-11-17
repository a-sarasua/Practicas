print("Bienvenido al programa del equipo dinamita")

persona = {
  "Nombre":"",
  "Apellido":"",
  "Edad":0,
  "Peso":0,
  "Altura":0,
  "Direccion":"",
  "Telefono":""
}

for i in persona:
	persona[i] = input(f"Ingrese su {i} :" )

imc = round(float(persona["Peso"])/(float(persona["Altura"])**2),2)
persona["IMC"] = imc

def cat_imc(imc):
	if imc < 18.5:
		print("usted tiene Bajo Peso")
	elif imc < 24.9:
		print("usted tiene Peso Normal")
	elif imc < 29.9:
		print("usted tiene Sobre Peso")
	elif imc < 34.9:
		print("usted tiene Obesidad tipo I")
	elif imc < 39.9:
		print("usted tiene Obesidad tipo II")
	else:
		print("usted tiene Obesidad tipo III")

def imprimir():
	for i in persona:
		print (i, ":", persona[i])