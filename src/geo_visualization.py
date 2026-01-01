import folium
import os

def plot_restaurant_map(df):
    os.makedirs("outputs", exist_ok=True)

    center_lat = df["Latitude"].mean()
    center_lon = df["Longitude"].mean()

    restaurant_map = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=4
    )

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=3,
            popup=f"{row['Restaurant Name']} | Rating: {row['Aggregate rating']}",
            color="blue",
            fill=True,
            fill_opacity=0.6
        ).add_to(restaurant_map)

    restaurant_map.save("outputs/restaurant_map.html")
