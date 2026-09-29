temperaturas = [18, 25, 31, 12, 28, 35, 20]


for i in range(len(temperaturas)): # 18, 25, 31, 12, 28, 35,30
    if temperaturas[i] < 15:
        print(f"La temperatura registrada {temperaturas[i]} es fría: ")
    elif temperaturas[i] >= 15 and temperaturas[i] <= 25:
        print(f"La temperatura registrada {temperaturas[i]} es templada: ")
    elif temperaturas[i] > 25:
        print(f"La temperatura registrada {temperaturas[i]} es calurosa: ")

def temperaturas_frias():
    print("Días de temperaturas frias: ", sum(1 for temp in temperaturas if temp < 15))
    return sum(1 for temp in temperaturas if temp < 15)

def temperaturas_templadas():
    print("Dias de temperaturas templadas: ", sum(1 for temp in temperaturas if temp >= 15 and temp <= 25))
    return sum(1 for temp in temperaturas if temp >= 15 and temp <= 25)

def temperaturas_calidas():
    print("Dias de temperaturas calidas: ", sum(1 for temp in temperaturas if temp > 25))
    return sum(1 for temp in temperaturas if temp > 25)

dias_fríos = temperaturas_frias()
dias_templados = temperaturas_templadas()
dias_calidos = temperaturas_calidas()

print("Dias totales con temperaturas frias = ", dias_fríos)
print("Dias totales con temperaturas templadas = ", dias_templados)
print("Dias totales con temperaturas calidas = ", dias_calidos)
