
from colorama import Fore, Style, init

# Inicializa o Colorama
init()

# Lista com os níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para definir a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe a situação do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for i in range(len(niveis)):
    cor = definir_cor(i + 1)
    mensagem = f"Nível {i + 1} - {niveis[i]}"

    print(cor + mensagem + Style.RESET_ALL)

from colorama import Fore, Style, init

# Inicializa o Colorama
init()

# Lista com os níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para definir a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe a situação do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for i in range(len(niveis)):
    cor = definir_cor(i + 1)
    mensagem = f"Nível {i + 1} - {niveis[i]}"

    print(cor + mensagem + Style.RESET_ALL)
