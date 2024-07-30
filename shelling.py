from experiment import Experiment, Measurement, Variable


def make_shelling_experiment(
    date: str,
    drum_rpm: int,
    paddle_shaft_rpm: int,
    ring_gap: float,
    tilt_angle: float,
    moisture_content: float,
    feed_rate: int = 500,
    pecan_variety_index: int = 0,
) -> Experiment:

    return Experiment(
        date=date,
        experiment="shelling",
        variables=[
            Variable(name="drum-rpm", unit="rpm", value=drum_rpm),
            Variable(name="paddle-shaft-rpm", unit="rpm", value=paddle_shaft_rpm),
            Variable(name="ring-gap", unit="in", value=ring_gap),
            Variable(name="tilt-angle", unit="deg", value=tilt_angle),
            Variable(name="feed-rate", unit="lb/hr", value=feed_rate),
            Variable(name="moisture-content", unit="%", value=moisture_content),
            Variable(name="pecan-variety", unit="", value=pecan_variety_index),
        ],
        measurements=[
            Measurement(name="bin1-weight", unit="lb"),
            Measurement(name="bin2-weight", unit="lb"),
            Measurement(name="bin3-weight", unit="lb"),
            Measurement(name="recirculated-weight", unit="lb"),
            Measurement(name="final-discharge-weight", unit="lb"),
            Measurement(name="bin1-half-yield", unit="%"),
            Measurement(name="bin2-half-yield", unit="%"),
            Measurement(name="bin3-half-yield", unit="%"),
        ],
    )
