import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode

    def __init__(self):
        self.maxx = -1000
        self.minn = +1000
        self.summ = 0.0
        self.lenn = 0
        self.temperature_counts = [0] * 111
        self.highest_count = 0
        self.mode = None

    def insert(self, temperature):
        self.maxx = max(self.maxx, temperature)
        self.minn = min(self.minn, temperature)
        self.summ += temperature
        self.lenn += 1
        self.temperature_counts[temperature] += 1
        if self.temperature_counts[temperature] > self.highest_count:
            self.highest_count = self.temperature_counts[temperature]
            self.mode = temperature

    def get_max(self):
        return self.maxx

    def get_min(self):
        return self.minn

    def get_mean(self):
        return self.summ / self.lenn

    def get_mode(self):
        return self.mode


# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)
