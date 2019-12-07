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

    # gets trip_nr (0..n) sets reader
    def _map_index(self, trip_nr):
        id_changes = -1

        # go through rows until trip_id changes trip_nr times
        prev_id = ""
        for row in self.reader:
            if row[0] != prev_id:
                id_changes += 1
                prev_id = row[0]

            if id_changes == trip_nr:
                break


    def __del__(self):
        self.file.close()
