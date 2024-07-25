from dataclasses import dataclass

from experiment import Experiment, Measurement, Variable


@dataclass
class MoistureExperiment(Experiment):
    def __init__(self, date: str):
        super().__init__(
            experiment="Moisture Analysis",
            date=date,
            variables=[
                Variable("cold-soak-time", "hour", (5, 45)),
                Variable("cold-soak-temp", "degF", (69, 72)),
                Variable("hot-soak-time", "minute", (5, 20)),
                Variable("hot-soak-temp", "degF", (180, 200)),
            ],
            measurements=[Measurement("moisture-content", "%", (0.06, 0.08))],
        )
