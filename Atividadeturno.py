# Programa para perguntar qual turno você estuda

turno = input( "Digite seu turno: M para matutino ,V para vespertino ,N para noturno: ")
match turno :
    case "M":
        print("digite bom dia")
    case "V":
        print("digite boa tarde")
    case "N":
        print("digite boa noite")
    case _:
        print("invalido")








