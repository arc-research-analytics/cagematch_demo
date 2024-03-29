# dependencies
import streamlit as st
import geopandas as gpd
import pandas as pd
import pydeck as pdk

# # set page configurations
# st.set_page_config(
#     page_title="Streamlit Demo",
#     page_icon=":sunglasses:",
#     layout="wide",
#     initial_sidebar_state="collapsed",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app that Will made for the cage match!"
#     }
# )

# # Add a map heading - the easy way
# st.header('Fulton County Population Density')

# # Add a map heading - the hard way
# color = '#000000'
# font_size = 40
# font_weight = '100'
# line_height = '1'
# margin_top = 5
# margin_bottom = 25
# st.markdown(
#     f"<h2 style='color:{color};font-size:{font_size}px; font-weight: {font_weight}; line-height: {line_height}; margin-top: {margin_top}px; margin-bottom: {margin_bottom}px'>Fulton County Population Density</h2>",
#     unsafe_allow_html=True)

# # map variables
# latitude = 33.85
# longitude = -84.42
# zoom = 8.8  # lower values zoom out, higher values zoom in
# map_height = 590

# # set color ramp (using Color Brewer)
# custom_colors_hex = [
#     '#eff3ff',  # lightest shade
#     '#bdd7e7',
#     '#6baed6',
#     '#3182bd',
#     '#08519c'  # darkest shade
# ]

# # equivalent RGB array from Color Brewer
# CB_rgb_list = ['rgb(239,243,255)', 'rgb(189,215,231)',
#                'rgb(107,174,214)', 'rgb(49,130,189)', 'rgb(8,81,156)']
# st.write(CB_rgb_list)

# # Pydeck is picky about how RGB values are stored, so we'll
# # use a custom conversion to create a list of tuples containing the RGB values
# custom_colors_rgb = [tuple(int(h.lstrip('#')[i:i+2], 16)
#                            for i in (0, 2, 4)) for h in custom_colors_hex]
# st.write(custom_colors_rgb)

# # read in the data using GeoPandas
# gdf = gpd.read_file('../Data/Fulton_county.geojson')

# # inspect the initial data inside the browser
# st.write(gdf.columns)
# gdf_initial = gdf.drop(columns=['geometry'])
# st.dataframe(gdf_initial)

# # Create a color map using quantiles
# color_mapper = pd.qcut(gdf['rPopDensity_e21'], q=len(
#     custom_colors_rgb), labels=custom_colors_rgb)

# # Add the color column
# gdf["choro_color"] = color_mapper

# # Format density column
# gdf['density_formatted'] = gdf['rPopDensity_e21'].apply(
#     lambda x: '{:,.0f}'.format(round(x)))

# # after adding the above columns, let's once again take a look at the data
# gdf_final = gdf.drop(columns=['geometry'])
# st.dataframe(gdf_final)

# # Now let's make a map! The below will configure how the map looks on load
# initial_view_state = pdk.ViewState(
#     latitude=latitude,
#     longitude=longitude,
#     zoom=zoom,
#     height=map_height
# )

# # create the geojson layer for the map
# geojson = pdk.Layer(
#     "GeoJsonLayer",
#     gdf,
#     pickable=True,
#     autoHighlight=True,
#     highlight_color=[255, 255, 255, 128],
#     opacity=0.5,
#     stroked=True,
#     get_line_color=[128, 128, 128],
#     line_width_min_pixels=0.5,
#     filled=True,
#     get_fill_color='choro_color'
# )

# # configure & customize the tooltip
# tooltip = {
#     "html": "Population / square mile: <b>{density_formatted}</b><hr style='margin: 10px auto; opacity:1; border-top: 2px solid white; width:85%'>\
#                 Census Tract {GEOID}",
#     "style": {"background": "rgba(128,128,128,0.75)",
#               "border": "1px solid white",
#               "color": "white",
#               "font-family": "Helvetica",
#               "text-align": "center"
#               },
# }

# # instantiate the map object to be rendered to the browser
# choropleth_map = pdk.Deck(
#     layers=geojson,
#     initial_view_state=initial_view_state,
#     map_provider='carto',  # can also try 'google_maps
#     map_style='dark',  # or light or satellite
#     tooltip=tooltip
# )

# # render the map
# col1, col2, col3 = st.columns([1, 1, 3])
# st.pydeck_chart(choropleth_map, use_container_width=True)
