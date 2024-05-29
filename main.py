from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.utils import *
# def test_exception():
#     try:
#         logging.info("error division")
#         a = 1 / 0
#     except Exception as e:
#         raise SensorException(e,sys)    
    
    
if __name__ == "__main__":
    file_path="/Users/bhawnagupta/Desktop/sensorlive/aps_failure_training_set1.csv"
    database_name="ineuron"
    collection_name = "sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)
    
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
        