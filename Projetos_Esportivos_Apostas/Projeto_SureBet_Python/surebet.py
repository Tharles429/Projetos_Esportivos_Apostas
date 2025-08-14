import pandas as pd

historico = []

def calcula_surebet(odds1, odds2, valor_total):
    soma_inversos = 1/odds1 + 1/odds2
    if soma_inversos >= 1:
        return None
    stake1 = valor_total * (1/odds1) / soma_inversos
    stake2 = valor_total * (1/odds2) / soma_inversos
    payout = stake1 * odds1
    lucro = payout - valor_total
    porcentagem_lucro = (lucro / valor_total) * 100
    return {
        "Odds 1": odds1,
        "Odds 2": odds2,
        "Valor Total": valor_total,
        "Stake 1": round(stake1, 2),
        "Stake 2": round(stake2, 2),
        "Payout": round(payout, 2),
        "Lucro": round(lucro, 2),
        "Porcentagem (%)": round(porcentagem_lucro, 2)
    }

def salvar_historico_excel(historico, nome_arquivo="historico_surebets.xlsx"):
    df = pd.DataFrame(historico)
    df.to_excel(nome_arquivo, index=False)
    print(f"Excel salvo como {nome_arquivo}")

# Exemplo de uso
while True:
    try:
        odds1 = float(input("Informe a odd 1: "))
        odds2 = float(input("Informe a odd 2: "))
        valor_total = float(input("Informe o valor total investido: "))
        resultado = calcula_surebet(odds1, odds2, valor_total)
        if resultado:
            print(f"Lucro líquido: R$ {resultado['Lucro']} ({resultado['Porcentagem (%)']}% do valor investido)")
            print(f"Aposta 1: R$ {resultado['Stake 1']} @ {odds1}")
            print(f"Aposta 2: R$ {resultado['Stake 2']} @ {odds2}")
            print(f"Payout garantido: R$ {resultado['Payout']}")
            historico.append(resultado)
        else:
            print("Sem surebet: soma dos inversos ≥ 1")
    except Exception as e:
        print("Entrada inválida. Tente novamente.")
    sair = input("Deseja adicionar outra entrada? (s/n): ").lower()
    if sair != 's':
        break

salvar_historico_excel(historico)