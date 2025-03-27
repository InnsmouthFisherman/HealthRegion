import os
from script import validate_table
from database import load_table, connect_to_database
import chardet
    


def main():
    file_path = r"D:\coding\projects\HealthRegion\backend\src\tables\test_table.csv" 
    connect_to_database()
    #validate_table(file_path)
    #load_table(file_path)

if __name__ == "__main__":
    main()