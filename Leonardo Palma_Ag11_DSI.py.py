from colorama import Fore, Style, init

init(autoreset=True)

niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def exibir_status_reservatorio(dados_nivel):
  """Função responsável por exibir a situação atual do reservatório

  com a cor correspondente e restaurar o padrão ao final.
  """
  cor = dados_nivel["cor"]
  nivel = dados_nivel["nivel"]
  situacao = dados_nivel["situacao"]

  print(f"{cor}[Nível {nivel}] Status do Reservatório: {situacao}")


def main():
  print("=== SIMULADOR DE MONITORAMENTO DE NÍVEL DE ÁGUA ===")
  print("Simulando os diferentes estados do reservatório:\n")

  for item in niveis_agua:
    exibir_status_reservatorio(item)

  print("\n--- Simulação finalizada com sucesso. ---")


if __name__ == "__main__":
  main()