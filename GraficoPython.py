import pandas as pd
import plotly.graph_objects as go
#import plotly_express as px

dfF = pd.read_csv('./datiSicurezzaLavoroF.csv')
dfM = pd.read_csv('./datiSicurezzaLavoroM.csv')
dfT = pd.read_csv('./datiSicurezzaLavoroT.csv')

countryF = dfF["geo"]
dataF = dfF["dati"]

countryM = dfM["geo"]
dataM = dfM["dati"]

countryT = dfT["geo"]
dataT = dfT["dati"]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=countryF,
    y=dataF,
    name='Femmine',
    marker=dict(
        color='rgba(172, 96, 247, 0.95)',
        line_color='rgba(172, 96, 247, 1.0)'
    )
))

fig.add_trace(go.Scatter(
    x=countryM, y=dataM,
    name='Maschi',
    marker=dict(
        color='rgba(3, 186, 3, 0.95)',
        line_color='rgba(3, 186, 3, 1.0)'
    )
))

fig.add_trace(go.Scatter(
    x=countryT,
    y=dataT,
    name='Totale',
    marker=dict(
        color='rgba(78, 167, 255, 0.95)',
        line_color='rgba(78, 167, 255, 1.0)'
    )
))

fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=8))

fig.update_layout(
    title="Persone che segnalano un problema di salute legato al lavoro per sesso, età e paese di nascita",
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(0, 0, 0)',
        tickfont_color='rgb(0, 0, 0)',
        showticklabels=True,
        ticks='outside',
    ),
    yaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(0, 0, 0)',
        tickfont_color='rgb(0, 0, 0)',
        showticklabels=True,
        ticks='outside',
    ),
    margin=dict(l=40, r=40, b=40, t=80),
    legend=dict(
        font_size=12,
        yanchor='middle',
        xanchor='right',
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    hovermode='closest',
)
fig.show()
