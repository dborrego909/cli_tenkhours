import csv
import sys


def main():
    topic = input("What did you study?: ")
    time = input("How long did you study for?: ")

    with open(f"{topic}.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["topic", "time"])
        writer.writerow({"topic": topic, "time": time})
