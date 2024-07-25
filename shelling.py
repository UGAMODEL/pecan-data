from dataclasses import dataclass

from experiment import Experiment, Measurement, Variable


@dataclass
class ShellingExperiment(Experiment):
    def __init__(self, date: str):
        super().__init__(
            experiment="Shelling Analysis",
            date=date,
            variables=[
                Variable("drum-rpm", "rpm", (30, 40)),
                Variable("paddle-shaft-rpm", "rpm", (400, 800)),
                Variable("ring-gap", "in"),
                Variable("tilt-angle", "deg", (2, 5)),
                Variable("feed-rate", "lb/hr", (300, 500), 500),
                Variable("moisture-content", "%", (5, 9)),
                Variable("pecan-variety", "", None, "desirable"),
            ],
            measurements=[
                Measurement("bin1-weight", "lb"),
                Measurement("bin2-weight", "lb"),
                Measurement("bin3-weight", "lb"),
                Measurement("recirculated-weight", "lb"),
                Measurement("final-discharge-weight", "lb"),
                Measurement("bin1-half-yield", "%"),
                Measurement("bin2-half-yield", "%"),
                Measurement("bin3-half-yield", "%"),
            ],
        )
