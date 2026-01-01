from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.geo_visualization import plot_restaurant_map
from src.city_analysis import city_wise_analysis
from src.insights import generate_insights

def main():
    print("Loading and preprocessing data...")
    df = load_data("data/Dataset.csv")
    df = preprocess_data(df)

    print("\nPlotting restaurant locations...")
    plot_restaurant_map(df)

    print("\nCity-wise Restaurant Analysis:\n")
    city_stats = city_wise_analysis(df)
    print(city_stats.head(10))

    print("\nKey Insights:\n")
    generate_insights(city_stats)

if __name__ == "__main__":
    main()
