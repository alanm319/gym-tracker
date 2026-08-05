import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def plot_max_weight(by_exercise_df: pd.DataFrame, exercise_name: str):
    exercise_df = by_exercise_df[by_exercise_df["exercise_title"] == exercise_name]

    fig, ax = plt.subplots()
    ax.plot(exercise_df["date"], exercise_df["heaviest_weight_lbs"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight (lb)")
    ax.set_title(exercise_name)
    return fig


def plot_volume(by_exercise_df: pd.DataFrame, exercise_name: str):
    exercise_df = by_exercise_df[by_exercise_df["exercise_title"] == exercise_name]

    fig, ax = plt.subplots()
    ax.plot(exercise_df["date"], exercise_df["volume"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Volume (lb)")
    ax.set_title(exercise_name)
    return fig


def plot_best_set_volume(by_exercise_df: pd.DataFrame, exercise_name: str):
    exercise_df = by_exercise_df[by_exercise_df["exercise_title"] == exercise_name]

    fig, ax = plt.subplots()
    ax.plot(exercise_df["date"], exercise_df["volume"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Volume (lb)")
    ax.set_title(exercise_name)
    return fig


def plot_1rm(by_exercise_df: pd.DataFrame, exercise_name: str):
    exercise_df = by_exercise_df[by_exercise_df["exercise_title"] == exercise_name]

    fig, ax = plt.subplots()
    ax.plot(exercise_df["date"], exercise_df["est_1rm"])
    ax.set_xlabel("Date")
    ax.set_ylabel("1 Rep Max (lb)")
    ax.set_title(exercise_name)
    return fig