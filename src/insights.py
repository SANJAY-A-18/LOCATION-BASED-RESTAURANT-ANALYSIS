def generate_insights(city_stats):
    top_city = city_stats.index[0]
    best_rated_city = city_stats["average_rating"].idxmax()

    print(f"• Highest number of restaurants: {top_city}")
    print(f"• Best average restaurant rating: {best_rated_city}")
    print("• Metro cities dominate restaurant density.")
    print("• Higher cost does not always imply higher ratings.")