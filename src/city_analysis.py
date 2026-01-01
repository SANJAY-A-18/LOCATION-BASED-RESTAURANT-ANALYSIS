def city_wise_analysis(df):
    city_stats = (
        df.groupby("City")
        .agg(
            restaurant_count=("Restaurant ID", "count"),
            average_rating=("Aggregate rating", "mean"),
            average_cost_for_two=("Average Cost for two", "mean")
        )
        .sort_values(by="restaurant_count", ascending=False)
    )

    city_stats.to_csv("outputs/city_analysis.csv")
    return city_stats
