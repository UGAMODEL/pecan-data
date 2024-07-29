from dataclasses import dataclass

from experiment import Experiment, Measurement, Variable


@dataclass
class ShellingExperiment(Experiment):
    def __init__(
        self,
        date: str,
        drum_rpm: int,
        paddle_shaft_rpm: int,
        ring_gap: float,
        tilt_angle: float,
        moisture_content: float,
        feed_rate: int = 500,
        pecan_variety: str = "desirable",
    ):

        super().__init__(experiment="Shelling Analysis", date=date)

        variables = [
            Variable("drum-rpm", "rpm", (30, 40), drum_rpm),
            Variable("paddle-shaft-rpm", "rpm", (400, 800), paddle_shaft_rpm),
            Variable("ring-gap", "in", value=ring_gap),
            Variable("tilt-angle", "deg", (2, 5), tilt_angle),
            Variable("feed-rate", "lb/hr", (300, 500), feed_rate),
            Variable("moisture-content", "%", (5, 9), moisture_content),
            Variable("pecan-variety", "", value=pecan_variety),
        ]
        self.add_variables(variables)

        measurements = [
            Measurement("bin1-weight", "lb"),
            Measurement("bin2-weight", "lb"),
            Measurement("bin3-weight", "lb"),
            Measurement("recirculated-weight", "lb"),
            Measurement("final-discharge-weight", "lb"),
            Measurement("bin1-half-yield", "%"),
            Measurement("bin2-half-yield", "%"),
            Measurement("bin3-half-yield", "%"),
        ]
        self.add_measurements(measurements)
