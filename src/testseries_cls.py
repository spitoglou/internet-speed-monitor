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
        self.error_array = []
        for i in range(self.iterations):
            try:
                logger.info(f"Measurement index: {i+1}")
                measurement = SpeedTest()
                measurement.perform_test()
                self.out_array.append(measurement.result_dict())
                logger.info(f"Applying delay of {self.delay} seconds...")
                sleep(self.delay)
            except KeyboardInterrupt:
                logger.info("KeyboardInterrupt detected. Exiting Loop...")
                break
            except Exception as e:
                logger.error(e)
                self.error_array.append(
                    {"timestamp": pd.Timestamp.now(), "error": str(e)}
                )
        # print(out_array)
        self.measurements = pd.DataFrame(self.out_array)
        self.errors = pd.DataFrame(self.error_array)
        if self.create_excel:
            self.create_excel_file()

    def create_excel_file(self, filename: str = "measurements.xlsx"):
        self.measurements.to_excel(filename, index=False)
        self.errors.to_excel(f'errors-{filename}', index=False)
