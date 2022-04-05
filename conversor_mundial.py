
def conversor(tipo_pesos, valor_dolar):
    pesos = input ("¿Cuantos 💲  " +tipo_pesos+ "tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares= round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")



menu = """
Bienvenido al conversor de monedas💵 💶 💷
1-Dolares
2-Euros
3-Wones

Elige una opcion: """
opcion =int(input(menu))

if opcion ==1:
    conversor(" Dolares ", 3.875)
elif opcion ==2:
    conversor(" Euros ", 4.552)
elif opcion ==3:
    conversor(" Wones ", 3.40)
else:
    print("Ingresa una opcion correcta please 🥺 ")
