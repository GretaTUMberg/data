import csv
from Trip import *

# Constants
TRIP_ID = 0
GROUP_ID = 1
TIMESTAMP = 2
HEADING = 4
LAT = 5
LON = 7
ACC_X = 13
ACC_Y = 14
SPEED = 15


class DataParser:
    def __init__(self, filename):
        try:
            self.file = open(filename, newline='')
            self.reader = csv.reader(self.file, delimiter=',', quotechar='"')
            # Skip header row
            next(self.reader)
        except FileNotFoundError:
            print('File not found')
        self.trip_id = 0
        self.group_id = 0
        self.timestamps = []
        self.headings = []
        self.lats = []
        self.longs = []
        self.acc_xs = []
        self.acc_ys = []
        self.speeds = []

    def _add_row(self, row, last_acc_x, last_acc_y, last_speed):
        self.timestamps.append(int(row[TIMESTAMP]))
        self.headings.append(float(row[HEADING]))
        self.lats.append(float(row[LAT]))
        self.longs.append(float(row[LON]))
        try:
            last_acc_x = float(row[ACC_X])
            last_acc_y = float(row[ACC_Y])
            last_speed = float(row[SPEED])
        except ValueError:
            pass
        finally:
            self.acc_xs.append(last_acc_x)
            self.acc_ys.append(last_acc_y)
            self.speeds.append(last_speed)

    def _create_rows(self):
        last_acc_x = 0
        last_acc_y = 0
        last_speed = 0

        first = True
        first_time = -1
        for row in self.reader:
            if row[0] != self.trip_id:
                break
            else:
                if first:
                    first_time = self.timestamps[0]
                    self.timestamps[0] = 0
                    first = False
                self._add_row(row, last_acc_x, last_acc_y, last_speed)
                self.timestamps[-1] -= first_time
                last_acc_x = self.acc_xs[-1]
                last_acc_y = self.acc_ys[-1]
                last_speed = self.speeds[-1]


        self.file.seek(1)

    def get_trip(self, trip_nr):
        self._map_index(trip_nr)
        self._create_rows()
        return Trip(self.trip_id, self.group_id,
                    self.timestamps, self.headings,
                    self.lats, self.longs,
                    self.acc_xs, self.acc_ys, self.speeds)

    # gets trip_nr (0..n) sets reader
    def _map_index(self, trip_nr):
        id_changes = -1

        # go through rows until trip_id changes trip_nr times
        prev_id = ""
        prev_groupid = -1

        tell_position_pointer = 1
        for row in self.reader:
            if row[0] != prev_id:
                id_changes += 1
                prev_id = row[0]
                prev_groupid = row[1]

            if id_changes == trip_nr:
                self._add_row(row, 0, 0, 0)
                break

            tell_position_pointer += 1

        self.trip_id = prev_id
        self.group_id = prev_groupid

    def __del__(self):
        self.file.close()


d = DataParser("dataframe.csv")
t = d.get_trip(1)
