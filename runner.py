from src.testseries_cls import TestSeries
from loguru import logger
import pandas as pd
import matplotlib.pyplot as plt
import typer


def main(iterations: int = 10, delay: int = 2, create_excel: bool = False):
    test_series = TestSeries(
        delay=delay, iterations=iterations, create_excel=create_excel
    )
    test_series.perform_test_series()

    mdf = test_series.measurements
    mdf["date_time"] = pd.to_datetime(mdf["timestamp"])
    plt.plot(mdf["date_time"], mdf["download_speed"], label="Download Speed")
    plt.plot(mdf["date_time"], mdf["upload_speed"], label="Upload Speed")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.savefig("speed.png", bbox_inches='tight')


if __name__ == "__main__":
    typer.run(main)
