print("----------------------------------------------------------------------------------------------------")
print("| Codigo | Descricao               |  Tamanho (P) 500ml  | Tamanho (M) 1000ml | Tamanho (G) 2000ml |")
print("| TR     | Sabor Tradicional       |  RS 6.00            |           R$ 10.00 |            R$ 18.00|")
print("| ES     | Sabores Especiais       |  RS 7.00            |           R$ 12.00 |            R$ 21.00|")
print("| PR     | Sabores Premium         |  RS 8.00            |           R$ 14.00 |            R$ 24.00|")
print("----------------------------------------------------------------------------------------------------")

contador = 0
bandeira = 1
while bandeira:
    tamanho_pote = input("Selecione o tamanho do pote do sorvete desejado: (p/m/g) >> ")
    codigo_do_sorvete = input("Selecione o sabor do pote de sorvete desejado  >> (TR/ES/PR)")
    # Primeira condicao para os sorvertes tradicionais.
    if codigo_do_sorvete == "TR".lower():
        if tamanho_pote == "p".lower():
            contador += 6
            print(contador)
        elif tamanho_pote == "m".lower():
            contador += 10
            print(contador)
        else:
            contador += 18
            print(contador)
    # Primeira condicao para os sorvertes especiais.
    elif codigo_do_sorvete == "ES".lower():
        if tamanho_pote == "p".lower():
            contador += 10
            print(contador)
        elif tamanho_pote == "m".lower():
            contador += 12
            print(contador)
        else:
            contador += 14
            print(contador)
    # Primeira condicao para os sorvertes premium.
    else:
        if tamanho_pote == "p".lower():
            contador += 18
            print(contador)
        elif tamanho_pote == "m".lower():
            contador += 21
            print(contador)
        else:
            contador += 24
            print(contador)
    
    mais_items = input("Voce deseja selecionar mais items? S ou N >> ")
    if mais_items.lower() == "s":
        continue
    else:
        break
        
        
        
