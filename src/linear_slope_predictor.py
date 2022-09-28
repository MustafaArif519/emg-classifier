import numpy as np
from window_predictor import WindowPredictor
from window_producer import *


class LinearSlopePredictor(WindowPredictor):

    def LinearSlopePredictor(self):
        super.__init__()
        self.rising_slope_min = None
        self.falling_slope_max = None

    def train(self, windows, labels):
        window_count = len(windows)
        rising_slopes = np.zeros((window_count))
        falling_slopes = np.zeros((window_count))
        window_idx = 0
        for window_arr in windows:
            max_idx = np.argmax(window_arr)
            max_val = window_arr[max_idx]
            min_rising_idx = np.argmin(window_arr[0:max_idx])
            min_rising_val = window_arr[min_falling_idx]
            min_falling_idx = np.argmin(window_arr[max_idx:len(window_arr)])
            min_falling_val = window_arr[min_rising_idx]

            rising_slopes[window_idx] = (max_val - min_rising_val) / (max_idx - min_rising_idx)
            falling_slopes[window_idx] = (min_falling_val - max_val) / (min_falling_idx - max_idx)

            window_idx += 1
        
        self.rising_slope_min = np.median(rising_slopes) - (0.5 * np.std(rising_slopes))
        self.falling_slope_max = np.median(falling_slopes) - (0.5 * np.std(falling_slopes))

        self.trained = True

