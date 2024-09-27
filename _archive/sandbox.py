import speedtest
from loguru import logger
from time import sleep
import pandas as pd


def test_speed():
    st = speedtest.Speedtest(secure=1)
    logger.info("Testing download speed...")
    download_speed = st.download()
    logger.info("Testing upload speed...")
    upload_speed = st.upload()
    logger.info("Getting results...")
    result = st.results.dict()
    return download_speed, upload_speed, result


def create_dataframe(delay: int = 2, measurements: int = 10, create_excel: bool = False):
    out_array = []
    for i in range(measurements):
        logger.info(f"Measurement index: {i+1}")
        download_speed, upload_speed, result = test_speed()
        out_array.append(
            {
                "timestamp": result["timestamp"],
                "download_speed": download_speed / 1024 / 1024,
                "upload_speed": upload_speed / 1024 / 1024,
                "ping": result["ping"],
                "server_url": result["server"]["url"],
                "server_name": result["server"]["name"],
                "server_country": result["server"]["country"],
                "client_ip": result["client"]["ip"],
                "client_isp": result["client"]["isp"],
            }
        )
        logger.info(f"Applying delay of {delay} seconds...")
        sleep(delay)
    # print(out_array)
    measurements = pd.DataFrame(out_array)
    if create_excel:
        excel_file = measurements.to_excel("measurements.xlsx", index=False)
    # print(measurements)
    return measurements


if __name__ == "__main__":
    delay = 2
    out_array = []
    for i in range(2):
        logger.info(f"Measurement index: {i}")
        download_speed, upload_speed, result = test_speed()
        out_array.append(
            {
                "timestamp": result["timestamp"],
                "download_speed": download_speed / 1024 / 1024,
                "upload_speed": upload_speed / 1024 / 1024,
                "ping": result["ping"],
                "server_url": result["server"]["url"],
                "server_name": result["server"]["name"],
                "server_country": result["server"]["country"],
                "client_ip": result["client"]["ip"],
                "client_isp": result["client"]["isp"],
            }
        )
        logger.info(f"Applying delay of {delay} seconds...")
        sleep(delay)
    print(out_array)
    measurements = pd.DataFrame(out_array)
    excel_file = measurements.to_excel("measurements.xlsx", index=False)
    print(measurements)
