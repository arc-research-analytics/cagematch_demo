# dependencies for building the map
import plotly.express as px
import pandas as pd
import geopandas as gpd
# dependencies for building the app
from dash import Dash, dcc, html

# ------ STEP 1: BUILD THE MAP----------

# # color ramp to be used by choropleth
# custom_colors_hex = [
#     '#eff3ff',  # lightest shade
#     '#bdd7e7',
#     '#6baed6',
#     '#3182bd',
#     '#08519c'  # darkest shade
# ]

# # create dictionary from above list
# color_discrete_map = {color_hex: color_hex for color_hex in custom_colors_hex}

# # read local geoJSON file
# gdf = gpd.read_file('../Data/Fulton_county.geojson')

# # Calculate quantiles for population density
# gdf["density_hex"] = pd.qcut(
#     gdf["rPopDensity_e21"],
#     q=len(custom_colors_hex),
#     labels=custom_colors_hex
# )

# # instantiate Plotly choropleth map 'figure'
# fig = px.choropleth_mapbox(
#     gdf,
#     geojson=gdf.geometry,
#     locations=gdf.index,
#     color='density_hex',
#     color_discrete_map=color_discrete_map,
#     hover_name="GEOID",
#     hover_data={"GEOID": True, "rPopDensity_e21": True},
#     opacity=0.8,
#     zoom=8.8,  # higher number = more zoomed in
#     center={
#         "lat": 33.85,  # same lat/long value the Streamlit app is using
#         "lon": -84.42
#     },

#     mapbox_style="carto-darkmatter",
#     # mapbox_style="open-street-map",
#     # mapbox_style="carto-positron",
# )


# # update map layout options
# fig.update_layout(
#     margin={
#         "r": 0,
#         "t": 30,
#         "l": 0,
#         "b": 0
#     },
#     height=620,
# )

# # using the 'fig' object created above, we'll modify a few of the components here
# fig.update_traces(
#     showlegend=False,
#     marker_line_width=0.5,
#     marker_line_color='rgb(128,128,128)',
#     hovertemplate="Population / square mile: <b>%{customdata[1]:,.0f}</b><br><br>"
#     "Census Tract %{customdata[0]}<extra></extra>",
#     hoverlabel=dict(
#         bgcolor="rgba(128,128,128,0.75)",  # Background color of the tooltip
#         bordercolor="white",
#         font=dict(family="Arial", size=15, color="white"),
#         align='auto'
#     )

# )

# # Modebar options
# config = {
#     # 'displayModeBar': False,
#     'displaylogo': False,
#     # 'modeBarButtonsToRemove': [
#     #     'lasso2d',
#     #     'toImage',
#     #     'resetViewMapbox'
#     # ]
# }


# ------ STEP 2: BUILD THE APP----------

# instantiate the Dash app
app = Dash()

# page title (aka browser tab title)
app.title = "Dash Demo"

# define the app's layout usings quasi-HTML elements
app.layout = html.Div([
    # html.H1(
    #     "Fulton County Population Density",
    #     style={
    #         'textAlign': 'left',
    #         'font-size': '2em',
    #         'font-family': 'sans-serif',
    #         'marginTop': '60px'
    #     }),
    # dcc.Graph(  # stands for "dash core components"
    #     figure=fig,
    #     config=config,
    #     style={
    #         'marginTop': '-5px',
    #     })
], style={
    'margin': '50px',
    'padding': '10px'
})

app.run_server(
    debug=True,
    dev_tools_ui=False
)
