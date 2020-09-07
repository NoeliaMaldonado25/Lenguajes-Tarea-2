
cadena ="__Servidor1"
cadena2 ="3servidor"

letra ="(a|b|\c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|C|D|E|F|G|H|I|J|K|L|M|N|O||P|Q|R|S|T|U|V|W|X|Y|Z)"
numero ="[0-9]"
simbolo = "_"
entrada= letra| numero | simbolo

def AFD(entrada):
    estado = 0
      for i in range(len(entrada)):
            if estado == 0:
                if entrada[i] is simbolo:
                    estado = 1
                elif entrada [i] is letra:
                    estado = 2
                else:
                    print("cadena incorrecta")
                    return
            elif estado == 1:
                if entrada[i] is letra:
                    estado = 3
                elif entrada[i] is simbolo:
                    estado = 1
                else:
                    print("cadena incorrecta")
                    return
            elif estado == 2:
                if entrada[i] == numero:
                    estado = 4
                elif entrada[i] is letra:
                    estado = 2
                else:
                    print("cadena incorrecta")
                    return
            elif estado == 3:
                if entrada[i] == numero:
                    estado = 4
                else:
                    print("cadena incorrecta")
                    return
            elif estado == 4:
                    print("estado de aceptacion")
            return
      print()

    AFD(cadena)
    AFD(cadena2)





