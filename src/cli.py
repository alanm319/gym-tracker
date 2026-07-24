from load import load_workouts
from metrics import aggregate_by_session
from charts import plot_max_weight, plot_1rm, plot_volume, plot_best_set_volume
import matplotlib.pyplot as plt

import argparse

COMMANDS = {
    "heaviest": plot_max_weight,
    "1rm": plot_1rm,
    "volume": plot_volume,
    "best_volume": plot_best_set_volume
}

parser = argparse.ArgumentParser()
parser.add_argument("exercise")
parser.add_argument("metric")

args = parser.parse_args()


all_exercises = load_workouts()
by_exercise = aggregate_by_session(all_exercises)

fig = COMMANDS[args.metric](by_exercise, args.exercise)
plt.show()