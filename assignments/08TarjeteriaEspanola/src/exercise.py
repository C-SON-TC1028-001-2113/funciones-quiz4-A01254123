def tarjetas(p,pl):
    pliego=p*12
    plumon=pl*35
    if pliego<plumon:
        return pliego
    elif pliego>plumon:
        return plumon
def main():
    #escribe tu código abajo de esta línea
    pliegos=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    maximo=tarjetas(pliegos, plumones)
    print("El número máximo de tarjetas que se pueden hacer es: "+str(maximo))
if __name__=='__main__':
    main()
