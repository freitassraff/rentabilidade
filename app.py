from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

investimentos = {
    "Banco A": 0.07,  # 7% a.a.
    "Banco B": 0.065, # 6.5% a.a.
    "Tesouro Direto": 0.06, # 6% a.a.
    "CDB X": 0.08,    # 8% a.a.
    "CDB Y": 0.075    # 7.5% a.a.
}

def calcular_aliquota_ir(periodo_dias):
    if periodo_dias <= 180:
        return 0.225
    elif periodo_dias <= 360:
        return 0.20
    elif periodo_dias <= 720:
        return 0.175
    else:
        return 0.15

def calcular_rentabilidade_com_ir(valor_investido, taxa_anual, periodo_dias):
    rentabilidade_anual = valor_investido * taxa_anual
    aliquota_ir = calcular_aliquota_ir(periodo_dias)
    rentabilidade_liquida_anual = rentabilidade_anual * (1 - aliquota_ir)
    
    taxa_mensal = (1 + taxa_anual) ** (1/12) - 1
    rentabilidade_mensal = valor_investido * taxa_mensal
    rentabilidade_liquida_mensal = rentabilidade_mensal * (1 - aliquota_ir)
    
    taxa_semanal = (1 + taxa_anual) ** (1/52) - 1
    rentabilidade_semanal = valor_investido * taxa_semanal
    rentabilidade_liquida_semanal = rentabilidade_semanal * (1 - aliquota_ir)
    
    return rentabilidade_liquida_anual, rentabilidade_liquida_mensal, rentabilidade_liquida_semanal

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        valor_investido = float(request.form['valor'])
        periodo_dias = int(request.form['periodo'])
        resultados = []
        for investimento, taxa in investimentos.items():
            rent_anual, rent_mensal, rent_semanal = calcular_rentabilidade_com_ir(valor_investido, taxa, periodo_dias)
            resultados.append({
                "Investimento": investimento,
                "Rentabilidade Anual Líquida (R$)": f"R$ {rent_anual:.2f}",
                "Rentabilidade Mensal Líquida (R$)": f"R$ {rent_mensal:.2f}",
                "Rentabilidade Semanal Líquida (R$)": f"R$ {rent_semanal:.2f}",
                "Taxa Anual (%)": f"{taxa * 100:.2f}%"
            })

        return render_template('index.html', resultados=resultados)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#create by Rafael Freitas