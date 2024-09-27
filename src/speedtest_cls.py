import speedtest
from loguru import logger

class SpeedTest:
    def __init__(self):
        self.st = speedtest.Speedtest(secure=1)
        
    def get_download_speed(self):
        logger.info("Testing download speed...")
        self.download_speed =  self.st.download()
        
    def get_upload_speed(self):
        logger.info("Testing upload speed...")
        self.upload_speed = self.st.upload()
    
    def get_results(self):
        logger.info("Getting results...")
        self.result = self.st.results.dict()
        
    def perform_test(self):
        self.get_download_speed()
        self.get_upload_speed()
        self.get_results()
    
    def result_dict(self):
        return {
            "timestamp": self.result["timestamp"],
            "download_speed": self.download_speed / 1024 / 1024,
            "upload_speed": self.upload_speed / 1024 / 1024,
            "ping": self.result["ping"],
            "server_url": self.result["server"]["url"],
            "server_name": self.result["server"]["name"],
            "server_country": self.result["server"]["country"],
            "client_ip": self.result["client"]["ip"],
            "client_isp": self.result["client"]["isp"],
        }
    