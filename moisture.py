from experiment import Experiment, Measurement, Variable


def make_cold_bath_experiment(
    date: str,
    initial_moisture: float,
    water_temperature: float,
    soak_time: int,
) -> Experiment:

    return Experiment(
        date=date,
        experiment="moisture-cold-bath",
        variables=[
            Variable(name="initial-moisture", unit="%", value=initial_moisture),
            Variable(
                name="water-temperature", unit="deg F", value=int(water_temperature)
            ),
            Variable(name="soak-time", unit="hours", value=soak_time),
        ],
        measurements=[
            Measurement(name="final-moisture", unit="%"),
            Measurement(name="final-temperature", unit="deg F"),
        ],
    )


def make_hot_bath_experiment(
    date: str,
    initial_moisture: float,
    water_temperature: float,
    soak_time: int,
) -> Experiment:

    return Experiment(
        date=date,
        experiment="moisture-cold-bath",
        variables=[
            Variable(name="initial-moisture", unit="%", value=initial_moisture),
            Variable(
                name="water-temperature", unit="deg F", value=int(water_temperature)
            ),
            Variable(name="soak-time", unit="minutes", value=soak_time),
        ],
        measurements=[
            Measurement(name="final-moisture", unit="%"),
        ],
    )
