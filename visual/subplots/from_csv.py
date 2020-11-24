import matplotlib.pyplot as plt
import csv

def read_data():
  with open("visual/subplots/temps.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
      print(row[0])