"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""

import csv
from typing import List

from src.some_storage_library import SomeStorageLibrary
def extra_source_columns(path: str) -> List:
    try:
        with open(path, "r") as f:
            source_columns = f.readlines()
            source_columns = [ line.strip() for line in source_columns]
            source_columns = [line.split("|") for line in source_columns]
    except Exception as e:
        raise(e)
    # counvert the first column value to int  of this dimension list    
    for element in source_columns:
        element[0]= int(element[0]) 

    # sort this souce columns by the order 
    source_columns.sort(key=lambda x: x[0], reverse = False)
    return source_columns


def data_transform_load(source_columns: List, input_path: str, output_path: str) -> None:
    
    # Define the header of csv file
    headers = [i[1] for i in source_columns]

    # Read row from SOURCEDATA.txt and save into output.csv file
    with open(input_path, "r") as input_file:
        #  read per line just incase memory leak
        with open(output_path, "w") as output_file:
            writer = csv.writer(output_file, delimiter = ",")
            writer.writerow(headers)
            for line in input_file:
                row = line.strip().split("|")
                writer.writerow(row)
    
def main():
    source_columns_path = "data/source/SOURCECOLUMNS.txt"
    source_data_path = "data/source/SOURCEDATA.txt"
    output_path = "output.csv"
    source_columns = extra_source_columns(source_columns_path)
    data_transform_load(source_columns, source_data_path, output_path)
    s = SomeStorageLibrary()
    s.load_csv(output_path)



if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    main()


