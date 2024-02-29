from urllib.request import urlopen
import json
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html

# mapping component
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})


fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))

fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center={"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# create dash application, pass in above 'fig'
app = Dash()
app.title = "Dash Demo 😎"
app.layout = html.Div([
    html.H1("Fulton County Population Density", style={
            'textAlign': 'center',
            'font-size': '2em',
            'font-family': 'sans-serif',
            }),
    dcc.Graph(figure=fig)
], style={
    'margin': '50px',
    'padding': '20px'
})

app.run_server(
    debug=True,
    use_reloader=True,
    dev_tools_ui=False)
