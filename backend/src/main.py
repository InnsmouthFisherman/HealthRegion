import os
from script import validate_table
from database import load_table

def main():
    validate_table(r"D:\coding\projects\HealthRegion\backend\src\tables\test_table.csv")
    load_table(r"D:\coding\projects\HealthRegion\backend\src\tables\test_table.csv")

if __name__ == "__main__":
    main()