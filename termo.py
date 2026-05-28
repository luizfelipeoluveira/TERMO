palavra_sys = ["T", "E", "R", "M", "O"]    
numero_tentivas = 6

def arrumar(palavra_system):
        juntar = "".join(palavra_system)
        corrigir_cor = f"\033[0m{juntar}"
        return corrigir_cor

while numero_tentivas > 0:
    
    entrada = list(input("Digite uma palavra com 5 letras:\n").upper())
    
    if len(entrada) != 5:
        print("Por favor coloque uma palavra com 5 letras")
        continue
    
    elif len(entrada) == 5:
        
        entrada_2 = entrada.copy()
        for k in range(5):
            if entrada[k] == palavra_sys[k]:
                entrada[k] = f"\033[92m{entrada[k]}\033[0m" 
        
            elif entrada[k] in palavra_sys and entrada[k] != palavra_sys:
                entrada[k] = f"\033[93m{entrada[k]}\033[0m"
    
            elif entrada[k] not in palavra_sys:
                entrada[k] = f"\033[91m{entrada[k]}\033[0m"   
                
        resposta_usuario = "".join(entrada)
        print(resposta_usuario)
        
        
    if entrada_2 == palavra_sys:
        final = "".join(entrada)
        print(f"Você acertou, a palavra era: {arrumar(palavra_sys)}")
        
    
    else:
        numero_tentivas -= 1
        atualizar_chance = print(f"Você tem {numero_tentivas} tentativas restantes.")