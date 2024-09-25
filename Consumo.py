# função para calcular o consumo de energia
def calcular_consumo(quantidade, potencia, horas):
  return quantidade * potencia * horas

def main():
    # lista de eletrodomesticos = []
    eletrodomesticos = [] # initialize eletrodomesticos list
    print("cálculo de consumo médio de energia\n")
    print("digite as informações dos eletrodomésticos")

    while True:
      nome = input("\nNome do eletrodoméstico (quando terminar digite 'sair' para finalizar):").strip()
      if nome.lower() == 'sair':
        break  # This should be indented to be part of the if block
      try:
          quantidade = int(input(f"Quantidade de {nome}(s):"))
          potencia = float(input(f"Potência de {nome} em watts:"))
          horas = float(input(f"Tempo de uso diário de {nome} em horas:"))
      except ValueError:
          print("entrada invalida por favor, insira números validos") # This should be indented to be part of the try block
          continue

          # adiciona os dados do eletrodomestico a lista
      consumo_diario = calcular_consumo(quantidade, potencia, horas)
      eletrodomesticos.append((nome, consumo_diario))

    # Calculate totals outside the loop
    consumo_total_diario = sum([consumo for _, consumo in eletrodomesticos])
    consumo_total_mensal = consumo_total_diario * 30 / 1000
    # convertendo para kwh

    # exibir resultados
    print("\nConsumo diário por eletrodoméstico (em wh):")
    for nome, consumo in eletrodomesticos:
        print(f"{nome}: {consumo:.2f} wh")

    print(f"Consumo total diário: {consumo_total_diario:.2f} wh")
    print(f"Consumo total mensal estimado: {consumo_total_mensal:.2f} kwh")

    #print para mostrar o consumo total de todos os eletrodomesticos
    print("\nResumo do consumo total:") #This line was not indented correctly
    print(f"Consumo total diário de todos os eletrodomésticos: {consumo_total_diario:.2f} wh")
    print(f"Consumo total mensal estimado de todos os eletrodomésticos: {consumo_total_mensal:.2f} kwh")

if __name__ == "__main__":
    main()
