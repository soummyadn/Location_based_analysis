# geographical_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
import plotly.express as px

# Step 1: Load the dataset
df = pd.read_csv('Dataset .csv')

# Step 2: Explore dataset columns
print("\nColumns:", df.columns)
print("\nData Info:")
print(df.info())

# Step 3: Rename columns for consistency
columns_map = {
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    'City': 'city',
    'Locality': 'locality',
    'Average Rating': 'average_rating',
    'Cuisines': 'cuisine',
    'Price Range': 'price_range',
    'Name': 'name'
}
df.rename(columns={k: v for k, v in columns_map.items() if k in df.columns}, inplace=True)

# Drop rows with missing latitude or longitude
df.dropna(subset=['latitude', 'longitude'], inplace=True)

# Step 4: Visualize restaurant distribution on map
center_lat = df['latitude'].mean()
center_lon = df['longitude'].mean()
restaurant_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)
marker_cluster = MarkerCluster().add_to(restaurant_map)

for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row.get('cuisine', 'N/A')} | Rating: {row.get('average_rating', 'N/A')}",
        tooltip=row.get('name', 'Restaurant')
    ).add_to(marker_cluster)

restaurant_map.save("restaurant_map.html")

# Step 5: Analyze restaurant concentration by city
plt.figure(figsize=(12, 6))
city_counts = df['city'].value_counts().head(10)
sns.barplot(x=city_counts.index, y=city_counts.values)
plt.title("Top 10 Cities with Most Restaurants")
plt.xticks(rotation=45)
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("top_cities_restaurants.png")
plt.show()

# Top localities
top_localities = df.groupby(['city', 'locality']).size().sort_values(ascending=False).head(10)
print("\nTop 10 Localities with Most Restaurants:\n", top_localities)

# Step 6: Statistics by city
# Average rating
avg_ratings_city = df.groupby('city')['average_rating'].mean().sort_values(ascending=False)
print("\nAverage Ratings by City:\n", avg_ratings_city.head(10))

# Popular cuisines
df['cuisine'] = df['cuisine'].astype(str)
df_cuisine = df.copy()
df_cuisine['cuisine'] = df_cuisine['cuisine'].str.split(', ')
df_cuisine = df_cuisine.explode('cuisine')

popular_cuisines = df_cuisine['cuisine'].value_counts().head(10)
print("\nTop 10 Cuisines:\n", popular_cuisines)

# Average price range
avg_price_city = df.groupby('city')['price_range'].mean().sort_values(ascending=False)
print("\nAverage Price Range by City:\n", avg_price_city.head(10))

# Step 7: Pattern Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='price_range', y='average_rating', hue='city', legend=False)
plt.title("Price Range vs Rating by City")
plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.show()

# Optional: Interactive Map using Plotly
fig = px.scatter_mapbox(
    df, lat="latitude", lon="longitude", color="average_rating",
    hover_name="cuisine", zoom=10, height=600,
    mapbox_style="carto-positron"
)
fig.write_html("interactive_map_plotly.html")
fig.show()

print("\nAnalysis complete. Maps and charts saved to files.")
