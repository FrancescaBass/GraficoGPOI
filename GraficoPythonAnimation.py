import plotly.express as px
import pandas as pd

df = pd.read_csv('./datiSicurezzaLavoroAnni.csv')

fig = px.bar(df, x="geo", y="dati", color="dati",
  animation_frame="time", animation_group="geo",)

fig.update_layout(
    title="Persone che segnalano un problema di salute legato al lavoro per sesso, età e paese di nascita",
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