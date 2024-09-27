from loguru import logger
from src.speedtest_cls import SpeedTest
from time import sleep
import pandas as pd


class TestSeries:
    def __init__(
        self, delay: int = 2, iterations: int = 10, create_excel: bool = False
    ):
        self.delay = delay
        self.iterations = iterations
        self.create_excel = create_excel

    def perform_test_series(self):
        self.out_array = []
        for i in range(self.iterations):
            logger.info(f"Measurement index: {i+1}")
            measurement = SpeedTest()
            measurement.perform_test()
            self.out_array.append(measurement.result_dict())
            logger.info(f"Applying delay of {self.delay} seconds...")
            sleep(self.delay)
        # print(out_array)
        self.measurements = pd.DataFrame(self.out_array)
        if self.create_excel:
            self.create_excel_file()

    def create_excel_file(self, filename: str = "measurements.xlsx"):
        self.measurements.to_excel(filename, index=False)
