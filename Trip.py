class Trip:
    def __init__(self, trip_id, group_id, timestamps, headings, lats, longs, acc_xs, acc_ys, speeds):
        self.trip_id = trip_id
        self.group_id = group_id
        self.timestamps = timestamps
        self.headings = headings
        self.lats = lats
        self.longs = longs
        self.acc_xs = acc_xs
        self.acc_ys = acc_ys
        self.speeds = speeds
