class MontoElevado(Exception):
    pass
saldo = 450
try:
    monto = int(input("Ingrese un monto a retirar: "))
    if  monto > 1000:
        raise Exception("Monto excede el límite permitido por transacción")
    elif monto > saldo:
        raise MontoElevado("No hay fondos suficientes")
    else:
        print("Monto procesaso ✅")
except MontoElevado as e:
    print("❌ Error: ", e)
except Exception as e:
    print("☠️ Error: ", e)
