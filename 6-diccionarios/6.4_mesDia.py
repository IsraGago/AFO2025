meses = {
	"enero":1,
	"febrero":2,
	"marzo":3,
	"abril":4,
	"mayo":5,
	"junio":6,
	"julio":7,
	"agosto":8,
	"septiembre":9,
	"octubre":10,
	"noviembre":11,
	"diciembre":12
}

fecha = input("introduce una fecha (dd/mm/aaaa): ")
fecha = fecha.split("/")
dia = fecha[0]
mes = int(fecha[1])
ano = fecha[2]

nombreMes = ""

for nomMes,numMes in meses.items():
#	print("clave:",nomMes,"valor:",numMes)
	if numMes == mes:
		nombreMes = nomMes
		break
if nombreMes in meses:
	print(dia,"de",nombreMes,"de",ano)
else:
	print("el número de mes introducido es inválido")
