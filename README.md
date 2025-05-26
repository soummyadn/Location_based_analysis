# 🗺️ Geographical Analysis of Restaurants

This project performs a comprehensive **geospatial and statistical analysis** of restaurant data using Python. It includes interactive maps, visualizations, and insights based on parameters like location, cuisine, ratings, and price range.

## 📂 Dataset

The dataset includes information on restaurants such as:

- Name
- Latitude & Longitude
- City and Locality
- Cuisine Type
- Average Rating
- Price Range

> 📁 The dataset is loaded from a CSV file: `266908d6-36ce-4104-b7f6-6513a67a2cbe.csv`

---

## 📊 Features & Analysis Steps

### 1. 📌 Load and Clean Dataset
- Handled missing values
- Renamed columns for consistency
- Prepared data for geospatial analysis

### 2. 🗺️ Restaurant Distribution Map
- Created interactive maps using **Folium**
- Clustered restaurants on map for better visualization
- Saved to `restaurant_map.html`

### 3. 📍 Concentration by City & Locality
- Bar charts of top 10 cities with the most restaurants
- Listing of top localities by restaurant count

### 4. 📈 Statistical Summaries
- Average ratings per city
- Most popular cuisines across all locations
- Average price range by city

### 5. 🔍 Pattern Analysis
- Scatter plots comparing price range vs ratings by city

### 6. 🧭 Interactive Plotly Map
- Fully interactive map built using **Plotly Express**
- Color-coded by restaurant rating
- Saved as `interactive_map_plotly.html`

---

## 📁 Output Files

| File                          | Description                                  |
|-------------------------------|----------------------------------------------|
| `restaurant_map.html`         | Folium-based interactive restaurant map      |
| `top_cities_restaurants.png`  | Bar chart of restaurant count by city        |
| `price_vs_rating.png`         | Scatter plot of price range vs ratings       |
| `interactive_map_plotly.html`| Plotly-based interactive map visualization   |

---

## 🧪 Technologies Used

- Python 🐍
- Pandas
- Seaborn & Matplotlib
- Folium
- Plotly Express

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/geographical-analysis-of-restaurants.git
cd geographical-analysis-of-restaurants
