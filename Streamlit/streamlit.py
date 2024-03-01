# dependencies
import streamlit as st
import geopandas as gpd
import pandas as pd
import pydeck as pdk

# map variables
latitude = 33.85
longitude = -84.42
min_zoom = 8
max_zoom = 15
zoom = 8.8  # lower values zoom out, higher values zoom in
map_height = 590

# set color ramp (using Color Brewer)
custom_colors_hex = [
    '#eff3ff',  # lightest shade
    '#bdd7e7',
    '#6baed6',
    '#3182bd',
    '#08519c'  # darkest shade
]

# convert the above hex list to RGB values
custom_colors_rgb = [tuple(int(h.lstrip('#')[i:i+2], 16)
                           for i in (0, 2, 4)) for h in custom_colors_hex]

# set page configurations
st.set_page_config(
    page_title="Streamlit Demo",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def streamlit_mapper():

    gdf = gpd.read_file('../Data/Fulton_county.geojson')

    # Create a color mapping using quantiles
    color_mapper = pd.qcut(gdf['rPopDensity_e21'], q=len(
        custom_colors_rgb), labels=custom_colors_rgb)

    # Add the color column
    gdf["choro_color"] = color_mapper

    # Format density column
    gdf['density_formatted'] = gdf['rPopDensity_e21'].apply(
        lambda x: '{:,.0f}'.format(round(x)))

    # create map intitial state
    initial_view_state = pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=zoom,
        max_zoom=max_zoom,
        min_zoom=min_zoom,
        height=map_height
    )

    # create the geojson layer which will be rendered
    geojson = pdk.Layer(
        "GeoJsonLayer",
        gdf,
        pickable=True,
        autoHighlight=True,
        highlight_color=[255, 255, 255, 128],
        opacity=0.5,
        stroked=True,
        get_line_color=[128, 128, 128],
        line_width_min_pixels=0.5,
        filled=True,
        get_fill_color='choro_color'
    )

    # configure & customize the tooltip
    tooltip = {
        "html": "Population / square mile: <b>{density_formatted}</b><hr style='margin: 10px auto; opacity:1; border-top: 2px solid white; width:85%'>\
                    Census Tract {GEOID}",
        "style": {"background": "rgba(128,128,128,0.75)",
                  "border": "1px solid white",
                  "color": "white",
                  "font-family": "Helvetica",
                  "text-align": "center"
                  },
    }

    # instantiate the map object to be rendered to the Streamlit dashboard
    r = pdk.Deck(
        layers=geojson,
        initial_view_state=initial_view_state,
        map_provider='carto',  # can also try 'google_maps
        map_style='dark',  # or light or satellite
        tooltip=tooltip
    )

    return r


st.header('Fulton County Population Density')
st.pydeck_chart(streamlit_mapper(), use_container_width=True)
