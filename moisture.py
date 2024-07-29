from dataclasses import dataclass

from experiment import Experiment, Measurement, Variable


@dataclass
class MoistureExperiment(Experiment):
    def __init__(
        self,
        date: str,
        cold_soak_time: float | None,
        cold_soak_temp: float | None,
        hot_soak_time: float | None,
        hot_soak_temp: float | None,
    ):
        super().__init__(experiment="Moisture Analysis", date=date)
        variables = [
            Variable("cold-soak-time", "hour", (5, 45), cold_soak_time),
            Variable("cold-soak-temp", "degF", (69, 72), cold_soak_temp),
            Variable("hot-soak-time", "minute", (5, 20), hot_soak_time),
            Variable("hot-soak-temp", "degF", (180, 200), hot_soak_temp),
        ]
        self.add_variables(variables)

        measurement = Measurement("moisture-content", "%", (0.06, 0.08))
        self.add_measurement(measurement)
