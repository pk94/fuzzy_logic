import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import copy
from rules import *
import matplotlib.pyplot as plt


class MamdaniReasoning:
    def __init__(self, rules, disease_name):
        self.rules = rules
        self.disease_name = disease_name

    def __call__(self, observation):
        decisions = [rule(observation) for rule in self.rules]
        decision = self.centroid_method(decisions)
        # self.plot(observation, decisions, decision)
        return decision

    def centroid_method(self, decisions):
        xs = np.linspace(0, 100, 200)
        decision = [max([min(rule.output_mf(x), decision)
                         for rule, decision in zip(self.rules, decisions)])
                    for x in xs]
        decision = np.sum(xs * decision) / (np.sum(decision) + 10e-10)
        return decision

    def plot(self, observation, decisions, decision_val):
        subplots_titles = (list(ATTRIBUTES_NAMES.values()) + ["Rule decision", "Decision"]) + \
                          (len(self.rules) - 1) * (list(ATTRIBUTES_NAMES.values()) + ["Decision"])
        fig = make_subplots(rows=len(self.rules), cols=len(ATTRIBUTES_RANGES.keys()) + 2,
                            specs=[[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {"rowspan": 2}],
                                   [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, None]],
                            subplot_titles=subplots_titles)
        fig.update_yaxes(range=[0, 1])
        fig.update_layout(showlegend=False)
        fig.update_layout(width=3000, height=800, title_text=f"Reasoning for {self.disease_name}. "
                                     f"First row is a rule for True, second for False. Decision: {decision_val}",
                          font=dict(size=20))
        for ii, (rule, decision) in enumerate(zip(self.rules, decisions)):
            for jj, (attribute, mf) in enumerate(rule.input_mf.items()):
                xs = np.linspace(ATTRIBUTES_RANGES[attribute][0], ATTRIBUTES_RANGES[attribute][1], 200)
                if mf is None:
                    fig.add_trace(go.Scatter(x=xs, y=[0] * len(xs), mode="lines"), row=ii + 1, col=jj + 1)
                else:
                    ys = [mf(x) for x in xs]
                    fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", line=dict(width=3)), row=ii + 1, col=jj + 1)
                fig.add_shape(go.layout.Shape(type="line", yref="paper", xref="x", x0=observation[attribute], y0=0,
                                              x1=observation[attribute], y1=1, line=dict(color="red", width=1)),
                              row=ii + 1, col=jj + 1)
            xs = np.linspace(0, 100, 200)
            fig.add_trace(go.Scatter(x=xs, y=[rule.output_mf(x) for x in xs], mode="lines", line=dict(color="black")),
                          row=ii + 1, col=jj + 2)
            fig.add_trace(go.Scatter(x=xs, y=[min(rule.output_mf(x), decision) for x in xs], mode="lines",
                                     line=dict(color="green", width=5)), row=ii + 1, col=jj + 2)
            fig.add_trace(go.Scatter(x=xs, y=[min(rule.output_mf(x), decision) for x in xs], mode="lines",
                                     line=dict(color="green", width=5)), row=1, col=jj + 3)
        fig.add_trace(go.Scatter(x=xs,
                                 y=[max([min(rule.output_mf(x), decision)
                                         for rule, decision in zip(self.rules, decisions)]) for x in xs],
                                 mode="lines",
                                 line=dict(color="yellow", width=2)), row=1, col=jj + 3)
        fig.add_shape(go.layout.Shape(type="line", yref="paper", xref="x", x0=decision_val, y0=0,
                                      x1=decision_val, y1=1, line=dict(color="red", width=3)), row=1, col=12)
        fig.write_image("example_reasoning.png")
        # fig.show()