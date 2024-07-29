from dataclasses import dataclass, field
from typing import List, Any

Interval = tuple[float, float] | None


@dataclass
class Measurement:
    """These are the fields that represent the outputs of the experiment."""

    name: str
    unit: str
    interval: Interval = None
    values: List[float] = field(default_factory=list)


@dataclass
class Variable:
    """These are the fields that represent the inputs of the experiment."""

    name: str
    unit: str
    interval: Interval = None
    value: Any = None


@dataclass
class Experiment:
    """This is the data class that represents the experiment."""

    experiment: str
    date: str
    measurements: dict[str, Measurement] = field(default_factory=dict)
    variables: dict[str, Variable] = field(default_factory=dict)

    def to_json(self):
        # Convert the data class to a dictionary, which can be easily converted to JSON.
        import json

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(self, json_str):
        # Convert a JSON string to a data class.
        import json

        data = json.loads(json_str)
        self.__dict__.update(data)

    def add_measurement(self, measurement: Measurement):
        # Add a measurement to the experiment.
        if measurement.name in self.measurements:
            raise ValueError(
                f"Measurement {measurement.name} already exists in the experiment."
            )
        self.measurements[measurement.name] = measurement

    def add_measurements(self, measurements: List[Measurement]):
        # Add a list of measurements to the experiment.
        for measurement in measurements:
            self.add_measurement(measurement)

    def take_measurement(self, source: str, value: float):
        # Add a measurement to the experiment.
        if source not in self.measurements:
            raise ValueError(f"Measurement {source} not found in the experiment.")
        self.measurements[source].values.append(value)

    def add_variable(self, variable: Variable):
        # Add a variable to the experiment.
        if variable.name in self.variables:
            raise ValueError(
                f"Variable {variable.name} already exists in the experiment."
            )
        self.variables[variable.name] = variable

    def add_variables(self, variables: List[Variable]):
        # Add a list of variables to the experiment.
        for variable in variables:
            self.add_variable(variable)

    def set_variable(self, source: str, value: Any):
        # Set a variable in the experiment.
        if source not in self.variables:
            raise ValueError(f"Variable {source} not found in the experiment.")
        self.variables[source].value = value
