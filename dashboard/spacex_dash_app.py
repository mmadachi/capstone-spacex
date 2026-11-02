"""Dashboard Plotly Dash — lançamentos do Falcon 9.
Execute:  python dashboard/spacex_dash_app.py   (dados em data/spacex_launch_dash.csv)
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv('data/spacex_launch_dash.csv')
min_p, max_p = df['Payload Mass (kg)'].min(), df['Payload Mass (kg)'].max()

app = Dash(__name__)
sites = [{'label': 'Todos os locais', 'value': 'ALL'}] + [{'label': s, 'value': s} for s in df['Launch Site'].unique()]

app.layout = html.Div([
    html.H1('Painel de lançamentos da SpaceX', style={'textAlign': 'center'}),
    dcc.Dropdown(id='site-dropdown', options=sites, value='ALL', placeholder='Escolha um local', searchable=True),
    dcc.Graph(id='success-pie-chart'),
    html.P('Carga útil (kg):'),
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000, value=[min_p, max_p],
                    marks={i: str(i) for i in range(0, 10001, 2500)}),
    dcc.Graph(id='success-payload-scatter-chart'),
])


@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def update_pie(site):
    if site == 'ALL':
        return px.pie(df, values='class', names='Launch Site', title='Sucessos por local')
    d = df[df['Launch Site'] == site]['class'].value_counts().reset_index()
    d.columns = ['class', 'count']
    return px.pie(d, values='count', names='class', title=f'Sucesso × falha em {site}')


@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'), Input('payload-slider', 'value')])
def update_scatter(site, payload):
    d = df[df['Payload Mass (kg)'].between(payload[0], payload[1])]
    if site != 'ALL':
        d = d[d['Launch Site'] == site]
    return px.scatter(d, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                      title='Carga útil × resultado do lançamento')


if __name__ == '__main__':
    app.run(debug=True)
