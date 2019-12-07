import csv
class DataParser:
    # Constants
    TRIP_ID = 0
    GROUP_ID = 1
    TIMESTAMP = 2
    HEADING = 4
    LAT = 5
    LON = 7
    ACC_X = 18
    ACC_Y = 19
    SPEED = 20

    def __init__(self, filename):
        try:
            self.file = open(filename, newline='')
            self.reader = csv.reader(self.file, delimiter=',', quotechar='"')
            # Skip header row
            next(self.reader)
        except FileNotFoundError:
            print('File not found')

    def __del__(self):
        self.file.close()
