# main entry point
from parameters.parameters import file_path
from data_ingestion.ingest import call_data
import time


#stage 0 Data Ingestion
print("Starting Data Ingestion")
start_time = time.time()
telco_customer_data = call_data(file_path)
end_time = time.time()
print(f"Execution time for data ingestin is {end_time - start_time} seconds")
print(telco_customer_data.shape)
print(telco_customer_data.head())

