from abc import abstractmethod


class MF:
    def __init__(self, parameters_dict):
        self.parameters_dict = parameters_dict

    @abstractmethod
    def field(self):
        return NotImplemented


class TrapezoidMF(MF):
    def __init__(self, parameters_dict, max_val=1):
        super().__init__(parameters_dict)
        self.max_val = max_val

    def __call__(self, val):
        if val < self.parameters_dict["x1"] or val > self.parameters_dict["x4"]:
            return 0
        elif self.parameters_dict["x1"] <= val < self.parameters_dict["x2"]:
            return self.max_val * (val - self.parameters_dict["x1"]) / (self.parameters_dict["x2"] - self.parameters_dict["x1"])
        elif self.parameters_dict["x2"] <= val <= self.parameters_dict["x3"]:
            return self.max_val
        elif self.parameters_dict["x3"] < val <= self.parameters_dict["x4"]:
            return self.max_val * (self.parameters_dict["x4"] - val) / (self.parameters_dict["x4"] - self.parameters_dict["x3"])

    def field(self):
        return ((self.parameters_dict["x4"] - self.parameters_dict["x1"]) +
                (self.parameters_dict["x3"] - self.parameters_dict["x2"])) * self.max_val / 2


class RisingEdgeMF(MF):
    def __init__(self, parameters_dict, max_val=1):
        super().__init__(parameters_dict)
        self.max_val = max_val

    def __call__(self, val):
        if val < self.parameters_dict["x1"]:
            return 0
        elif self.parameters_dict["x1"] <= val <= self.parameters_dict["x2"]:
            return self.max_val * (val - self.parameters_dict["x1"]) / (self.parameters_dict["x2"] - self.parameters_dict["x1"])
        elif val > self.parameters_dict["x2"]:
            return self.max_val

    def field(self, max_range):
        return (self.parameters_dict["x2"] - self.parameters_dict["x1"]) * self.max_val / 2 + \
               (max_range - self.parameters_dict["x2"]) * self.max_val


class TrailingEdgeMF(MF):
    def __init__(self, parameters_dict, max_val=1):
        super().__init__(parameters_dict)
        self.max_val = max_val

    def __call__(self, val):
        if val < self.parameters_dict["x1"]:
            return self.max_val
        elif self.parameters_dict["x1"] <= val <= self.parameters_dict["x2"]:
            return self.max_val * (self.parameters_dict["x2"] - val) / (self.parameters_dict["x2"] - self.parameters_dict["x1"])
        elif val > self.parameters_dict["x2"]:
            return 0

    def field(self, min_range):
        return (self.parameters_dict["x1"] - min_range) * self.max_val +  \
               (self.parameters_dict["x2"] - self.parameters_dict["x1"]) * self.max_val / 2



