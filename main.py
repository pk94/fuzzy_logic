import pandas as pd
from tqdm import tqdm
import numpy as np
from os import makedirs
from os.path import exists
import matplotlib.pyplot as plt
import seaborn as sn
from reasoning import MamdaniReasoning
from rules import *

DATA_PATH = "dataset.csv"

DISEASES = {
    "Cold": MamdaniReasoning([Rule(COLD_RULE_IN_TRUE, COLD_RULE_OUT_TRUE),
                              Rule(COLD_RULE_IN_FALSE, COLD_RULE_OUT_FALSE)],
                             "Cold"),
    "Flu": MamdaniReasoning([Rule(FLU_RULE_IN_TRUE, FLU_RULE_OUT_TRUE),
                             Rule(FLU_RULE_IN_FALSE, FLU_RULE_OUT_FALSE)],
                            "Flu"),
    "Diabetes": MamdaniReasoning([Rule(DIABETES_RULE_IN_TRUE, DIABETES_RULE_OUT_TRUE),
                                  Rule(DIABETES_RULE_IN_FALSE, DIABETES_RULE_OUT_FALSE)],
                                 "Diabetes"),
    "Hashimoto": MamdaniReasoning([Rule(HASHIMOTO_RULE_IN_TRUE, HASHIMOTO_RULE_OUT_TRUE),
                                   Rule(HASHIMOTO_RULE_IN_FALSE, HASHIMOTO_RULE_OUT_FALSE)],
                                  "Hashimoto"),
    "Heart attack": MamdaniReasoning([Rule(HEART_ATTACK_RULE_IN_TRUE, HEART_ATTACK_RULE_OUT_TRUE),
                                      Rule(HEART_ATTACK_RULE_IN_FALSE, HEART_ATTACK_RULE_OUT_FALSE)],
                                     "Heart attack"),
    "Stroke": MamdaniReasoning([Rule(STROKE_RULE_IN_TRUE, STROKE_RULE_OUT_TRUE),
                                Rule(STROKE_RULE_IN_FALSE, STROKE_RULE_OUT_FALSE)],
                               "Stroke"),
    "Hypertension": MamdaniReasoning([Rule(HYPERTENSION_RULE_IN_TRUE, HYPERTENSION_RULE_OUT_TRUE),
                                      Rule(HYPERTENSION_RULE_IN_FALSE, HYPERTENSION_RULE_OUT_FALSE)],
                                     "Hypertension"),
    "Allergy": MamdaniReasoning([Rule(ALLERGY_RULE_IN_TRUE, ALLERGY_RULE_OUT_TRUE),
                                 Rule(ALLERGY_RULE_IN_FALSE, ALLERGY_RULE_OUT_FALSE)],
                                "Allergy")

}


def load_data(data_path):
    data = pd.read_csv(data_path)
    return data


class Results:
    def __init__(self, diseases, attributes):
        self.diseases = {disease: {"True": [], "False": []} for disease in diseases}
        self.attributes = attributes

    def statistical_analysis(self):
        for disease in self.diseases.keys():
            disease_results = []
            for attribute in self.attributes:
                true_values = [observation[attribute] for observation in self.diseases[disease]["True"]]
                false_values = [observation[attribute] for observation in self.diseases[disease]["False"]]
                disease_results.append({"Attribute": attribute,
                                        "Positive mean value": np.mean(true_values) if true_values else None,
                                        "Positive std": np.std(true_values) if true_values else None,
                                        "Negative mean value": np.mean(false_values) if false_values else None,
                                        "Negative std": np.std(false_values) if false_values else None,
                                        "Normalized difference": np.abs(np.mean(true_values) - np.mean(false_values))
                                                                 / np.mean(true_values + false_values)
                                        })
            if not exists("results"):
                makedirs("results")
            df = pd.DataFrame(disease_results)
            df.to_csv(f"results/{disease}.csv", index=False)

    def diseases_matrix(self, diagnoses):
        disease_matrix = np.zeros((len(self.diseases.keys()), len(self.diseases.keys())))
        for diagnose in diagnoses:
            if diagnose:
                for ii in diagnose:
                    for jj in diagnose:
                        disease_matrix[ii, jj] += 1
        df_cm = pd.DataFrame(disease_matrix, index=list(self.diseases.keys()), columns=list(self.diseases.keys()))
        plt.figure(figsize=(11, 8))
        sn.heatmap(df_cm, annot=True)
        plt.savefig("diseases_matrix.png")
        plt.clf()

    def diseases_number(self, diagnoses):
        num_diseases = {num: 0 for num in range(len(list(DISEASES.keys())) + 1)}
        for diagnose in diagnoses:
            num_diseases[len(diagnose)] += 1
        plt.bar(list(num_diseases.keys()), list(num_diseases.values()))
        plt.title("Number of patients with multiple diseases")
        plt.xlabel("Number of diseases")
        plt.ylabel("Number of patients with the specific number of diseases")
        plt.savefig("diseases_num.png")

    def analyse(self, diagnoses):
        self.statistical_analysis()
        self.diseases_matrix(diagnoses)
        self.diseases_number(diagnoses)


def main():
    data = load_data(DATA_PATH)
    results = Results(
        diseases=list(DISEASES.keys()),
        attributes=["temperature", "heart_rate", "systolic pressure", "diastolic pressure", "glucose_level", "tsh",
                    "cholesterol", "headache", "sore_throat", "runny_nose"])
    diagnoses = []
    for _, observation in tqdm(data.iterrows()):
        patient_diseases = []
        for idx, (disease, reasoning) in enumerate(DISEASES.items()):
            decision = reasoning(observation)
            results.diseases[disease]["True"].append(observation) if decision > 50 \
                else results.diseases[disease]["False"].append(observation)
            if decision > 50:
                patient_diseases.append(idx)
        diagnoses.append(patient_diseases)
    results.analyse(diagnoses)


if __name__ == "__main__":
    main()
