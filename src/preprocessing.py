def preprocess_data(df):
    # Drop rows with missing coordinates
    df = df.dropna(subset=["Latitude", "Longitude"])

    # Fill missing ratings and cost
    df["Aggregate rating"] = df["Aggregate rating"].fillna(0)
    df["Average Cost for two"] = df["Average Cost for two"].fillna(0)

    return df
