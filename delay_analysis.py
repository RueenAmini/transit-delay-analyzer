import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("delays.csv")

    print("\n--- Transit Delay Analysis ---\n")

    print("Total delay incidents:", len(df))

    avg_delay = df["delay_minutes"].mean()
    print("Average delay:", round(avg_delay, 2))

    print("\nMost delayed routes:")
    print(df["route"].value_counts())

    print("\nDelay by hour:")
    print(df["hour"].value_counts().sort_index())

    print("\nAverage delay per route:")
    print(df.groupby("route")["delay_minutes"].mean())

    # Visualization
    df.groupby("route")["delay_minutes"].mean().plot(kind="bar")
    plt.title("Average Delay by Route")
    plt.ylabel("Minutes")
    plt.xlabel("Route")
    plt.show()

if __name__ == "__main__":
    main()
