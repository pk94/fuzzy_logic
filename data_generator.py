from numpy.random import normal
import pandas as pd


class Attribute:
    def __init__(self, name, mean, std, min_val, max_val):
        self.name = name
        self.mean = mean
        self.std = std
        self.min_val = min_val
        self.max_val = max_val
        self.values = []

    def generate_values(self, num_samples):
        for _ in range(num_samples):
            val = normal(self.mean, self.std)
            while val < self.min_val or val > self.max_val:
                val = normal(self.mean, self.std)
            self.values.append(val)


class Dataset:
    def __init__(self, attributes):
        self.attributes = attributes

    def generate_dataset(self, num_samples, save_path):
        df = pd.DataFrame()
        for attribute in self.attributes:
            attribute.generate_values(num_samples)
            df[attribute.name] = attribute.values
        df.to_csv(save_path, index=False)


ATTRIBUTES = [Attribute(name="temperature", mean=36.5, std=3, min_val=33.5, max_val=42),
              Attribute(name="heart_rate", mean=70, std=30, min_val=40, max_val=140),
              Attribute(name="systolic pressure", mean=120, std=40, min_val=80, max_val=200),
              Attribute(name="diastolic pressure", mean=90, std=20, min_val=60, max_val=130),
              Attribute(name="glucose_level", mean=85, std=15, min_val=60, max_val=250),
              Attribute(name="tsh", mean=2, std=1, min_val=0.1, max_val=8),
              Attribute(name="cholesterol", mean=170, std=40, min_val=100, max_val=300),
              Attribute(name="headache", mean=3, std=4, min_val=0, max_val=10),
              Attribute(name="sore_throat", mean=3, std=4, min_val=0, max_val=10),
              Attribute(name="runny_nose", mean=3, std=4, min_val=0, max_val=10)]

dataset = Dataset(ATTRIBUTES)
dataset.generate_dataset(100000, "dataset.csv")




