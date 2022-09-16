#funion que covierta grados
def convertir_grados(valor, origen, destino):
if origen == "cecius":
    if destino == "celcius":
        valor_destino = valor
    elif destino == "farenheit":
        valor_destino = (valor * 9 / 5) + 32
    elif destino == "kelvin":
        valor_destino = valor + 275.15
    else:
        print("Parametro incorrecto")