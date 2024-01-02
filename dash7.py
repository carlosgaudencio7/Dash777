#importa bibliotecas
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

#inicializando o dash em flask
app = Dash(__name__)


#lendo base de dados
df = pd.read_excel("vendas.xlsx")

#criando o gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

#definindo layout html
app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children="Gráfico com o faturamento de todos os produtos separados por Loja"),

    html.Div(children='''
        Obs: Esse gráfico mostra a quanridade de todos os produtos vendidos, não o faturamento,
    '''),
    html.Div(id="texto"),
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='listalojas'),
    
    dcc.Graph(
        id='grafqtdvendas', 
        figure=fig,
    )
    
  ])

@app.callback(
    Output("grafqtdvendas", 'figure'),
    Input('listalojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']== value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
