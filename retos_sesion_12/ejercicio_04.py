edad = int(input("Edad del cliente: "))
compra = float(input("Monto de compra: "))

if edad > 60 and compra > 1000:
    pagar= compra*0.80
   
elif edad>18 and edad<60 and compra>500:
    pagar = compra*0.90
   
else:
    pagar = compra*0.98

print(f"Usted debe pagar: {pagar}")
    

