from membership_functions import *

ATTRIBUTES_RANGES = {
    "temperature": [32, 42],
    "heart_rate": [35, 150],
    "systolic pressure": [80, 200],
    "diastolic pressure": [70, 105],
    "glucose_level": [50, 200],
    "tsh": [0, 9],
    "cholesterol": [120, 280],
    "headache": [0, 10],
    "sore_throat": [0, 10],
    "runny_nose": [0, 10]
}

ATTRIBUTES_NAMES = {
    "temperature": "Temperature",
    "heart_rate": "Heart rate",
    "systolic pressure": "Systolic pressure",
    "diastolic pressure": "Diastolic pressure",
    "glucose_level": "Glucose level",
    "tsh": "TSH",
    "cholesterol": "Cholesterol",
    "headache": "Headache pain level",
    "sore_throat": "Sore throat pain level",
    "runny_nose": "Runny nose"
}


class Rule:
    def __init__(self, input_mf, output_mf):
        self.input_mf = input_mf
        self.output_mf = output_mf

    def __call__(self, observation):
        out_values = []
        for attribute, val in observation.items():
            if self.input_mf[attribute] is None:
                continue
            out_values.append(self.input_mf[attribute](val))
        decisions = [val for val in out_values]
        decision_val = min(decisions)
        return decision_val


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
COLD_RULE_IN_TRUE = {
    "temperature": RisingEdgeMF({"x1": 36, "x2": 38}),
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": RisingEdgeMF({"x1": 3, "x2": 7}),
    "sore_throat": RisingEdgeMF({"x1": 3, "x2": 7}),
    "runny_nose": RisingEdgeMF({"x1": 3, "x2": 7})}

COLD_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

COLD_RULE_IN_FALSE = {
    "temperature": TrailingEdgeMF({"x1": 35, "x2": 37.5}),
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": TrailingEdgeMF({"x1": 3, "x2": 7}),
    "sore_throat": TrailingEdgeMF({"x1": 3, "x2": 7}),
    "runny_nose": TrailingEdgeMF({"x1": 3, "x2": 7})}

COLD_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
FLU_RULE_IN_TRUE = {
    "temperature": RisingEdgeMF({"x1": 36, "x2": 39}),
    "heart_rate": RisingEdgeMF({"x1": 70, "x2": 120}),
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": RisingEdgeMF({"x1": 4, "x2": 7}),
    "sore_throat": RisingEdgeMF({"x1": 4, "x2": 7}),
    "runny_nose": RisingEdgeMF({"x1": 4, "x2": 7})}

FLU_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

FLU_RULE_IN_FALSE = {
    "temperature": TrailingEdgeMF({"x1": 35, "x2": 37.5}),
    "heart_rate": TrailingEdgeMF({"x1": 70, "x2": 120}),
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": TrailingEdgeMF({"x1": 5, "x2": 7}),
    "sore_throat": TrailingEdgeMF({"x1": 5, "x2": 7}),
    "runny_nose": TrailingEdgeMF({"x1": 5, "x2": 7})}

FLU_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
DIABETES_RULE_IN_TRUE = {
    "temperature": None,
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": RisingEdgeMF({"x1": 95, "x2": 115}),
    "tsh": None,
    "cholesterol": None,
    "headache": None,
    "sore_throat": None,
    "runny_nose": None}

DIABETES_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

DIABETES_RULE_IN_FALSE = {
    "temperature": None,
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": TrailingEdgeMF({"x1": 95, "x2": 120}),
    "tsh": None,
    "cholesterol": None,
    "headache": None,
    "sore_throat": None,
    "runny_nose": None}

DIABETES_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
HASHIMOTO_RULE_IN_TRUE = {
    "temperature": None,
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": RisingEdgeMF({"x1": 2, "x2": 5}),
    "cholesterol": None,
    "headache": None,
    "sore_throat": None,
    "runny_nose": None}

HASHIMOTO_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

HASHIMOTO_RULE_IN_FALSE = {
    "temperature": None,
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": TrailingEdgeMF({"x1": 2, "x2": 4.5}),
    "cholesterol": None,
    "headache": None,
    "sore_throat": None,
    "runny_nose": None}

HASHIMOTO_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
HEART_ATTACK_RULE_IN_TRUE = {
    "temperature": None,
    "heart_rate": RisingEdgeMF({"x1": 70, "x2": 130}),
    "diastolic pressure": TrailingEdgeMF({"x1": 70, "x2": 80}),
    "systolic pressure": TrailingEdgeMF({"x1": 90, "x2": 120}),
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": RisingEdgeMF({"x1": 6, "x2": 9}),
    "sore_throat": None,
    "runny_nose": None}

HEART_ATTACK_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

HEART_ATTACK_RULE_IN_FALSE = {
    "temperature": None,
    "heart_rate": TrailingEdgeMF({"x1": 70, "x2": 130}),
    "diastolic pressure": RisingEdgeMF({"x1": 70, "x2": 80}),
    "systolic pressure": RisingEdgeMF({"x1": 70, "x2": 130}),
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": TrailingEdgeMF({"x1": 3, "x2": 7}),
    "sore_throat": None,
    "runny_nose": None}

HEART_ATTACK_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
STROKE_RULE_IN_TRUE = {
    "temperature": RisingEdgeMF({"x1": 36, "x2": 39}),
    "heart_rate": RisingEdgeMF({"x1": 60, "x2": 130}),
    "systolic pressure": RisingEdgeMF({"x1": 90, "x2": 150}),
    "diastolic pressure": RisingEdgeMF({"x1": 80, "x2": 100}),
    "glucose_level": RisingEdgeMF({"x1": 110, "x2": 140}),
    "tsh": None,
    "cholesterol": RisingEdgeMF({"x1": 190, "x2": 260}),
    "headache": RisingEdgeMF({"x1": 6, "x2": 9}),
    "sore_throat": None,
    "runny_nose": None}

STROKE_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

STROKE_RULE_IN_FALSE = {
    "temperature": TrailingEdgeMF({"x1": 35, "x2": 37}),
    "heart_rate": TrailingEdgeMF({"x1": 70, "x2": 130}),
    "systolic pressure": TrailingEdgeMF({"x1": 70, "x2": 130}),
    "diastolic pressure": TrailingEdgeMF({"x1": 70, "x2": 90}),
    "glucose_level": TrailingEdgeMF({"x1": 70, "x2": 110}),
    "tsh": None,
    "cholesterol": TrailingEdgeMF({"x1": 140, "x2": 210}),
    "headache": TrailingEdgeMF({"x1": 3, "x2": 7}),
    "sore_throat": None,
    "runny_nose": None}

STROKE_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
HYPERTENSION_RULE_IN_TRUE = {
    "temperature": None,
    "heart_rate": RisingEdgeMF({"x1": 60, "x2": 130}),
    "systolic pressure": RisingEdgeMF({"x1": 110, "x2": 130}),
    "diastolic pressure": RisingEdgeMF({"x1": 75, "x2": 100}),
    "glucose_level": None,
    "tsh": None,
    "cholesterol": RisingEdgeMF({"x1": 190, "x2": 260}),
    "headache": RisingEdgeMF({"x1": 7, "x2": 9}),
    "sore_throat": None,
    "runny_nose": None}

HYPERTENSION_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

HYPERTENSION_RULE_IN_FALSE = {
    "temperature": None,
    "heart_rate": TrailingEdgeMF({"x1": 70, "x2": 120}),
    "systolic pressure": TrailingEdgeMF({"x1": 100, "x2": 130}),
    "diastolic pressure": TrailingEdgeMF({"x1": 80, "x2": 90}),
    "glucose_level": None,
    "tsh": None,
    "cholesterol": TrailingEdgeMF({"x1": 140, "x2": 240}),
    "headache": TrailingEdgeMF({"x1": 3, "x2": 9}),
    "sore_throat": None,
    "runny_nose": None}

HYPERTENSION_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
ALLERGY_RULE_IN_TRUE = {
    "temperature": None,
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": RisingEdgeMF({"x1": 4, "x2": 9}),
    "sore_throat": RisingEdgeMF({"x1": 7, "x2": 9}),
    "runny_nose": RisingEdgeMF({"x1": 2, "x2": 7}),}

ALLERGY_RULE_OUT_TRUE = RisingEdgeMF({"x1": 30, "x2": 70})

ALLERGY_RULE_IN_FALSE = {
    "temperature": None,
    "heart_rate": None,
    "systolic pressure": None,
    "diastolic pressure": None,
    "glucose_level": None,
    "tsh": None,
    "cholesterol": None,
    "headache": TrailingEdgeMF({"x1": 7, "x2": 9}),
    "sore_throat": TrailingEdgeMF({"x1": 8, "x2": 9}),
    "runny_nose": TrailingEdgeMF({"x1": 2, "x2": 8}),}

ALLERGY_RULE_OUT_FALSE = TrailingEdgeMF({"x1": 30, "x2": 70})


