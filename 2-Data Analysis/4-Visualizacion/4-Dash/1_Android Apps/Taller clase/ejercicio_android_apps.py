

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID, external_stylesheets])

df = pd.read_csv("data/googleplaystore.csv")

def quitar_m(x):
    return float(x.replace('M', '000'))

df['Reviews'] = list(map(quitar_m, df['Reviews']))

fig_scatter = px.scatter(df, x='Reviews', y='Rating', color='Category')

#fig_bar = px.bar(df, x= '', y='App', color='')

if __name__ == '__main__':
    app.run_server(debug=True)