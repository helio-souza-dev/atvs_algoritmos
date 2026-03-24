import time
import colorama
from colorama import init

init()

def escrever(texto, delay):
    
    cores=[colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN, colorama.Fore.WHITE]
    
    
    for i, letra in enumerate(texto):
        print(cores[i % len(cores)] + letra, end='', flush=True)
        time.sleep(delay)
    
rodando = True
while rodando:
    textos = []
    quantidade = int(input("Quantos textos deseja escrever? "))
    for q in range(quantidade):
            texto = input("Digite o texto que deseja escrever: ")
            delay = float(input("Digite o delay entre as letras (em segundos): "))
            
            textos.append([texto + " ", delay])
            
    for texto, delay in textos:
        escrever(texto, delay)
        
    resposta = ""
    
    
    while resposta != 'n' or resposta != 's':
        resposta = input("\nDeseja escrever mais um texto? (s/n): ")
        
        if resposta == 's':
            continue

        elif resposta == 'n':
            
            escrever("Saindo do programa...", 0.1)
            rodando = False
            break
        
        else:
            print("resposta invalida")
            continue