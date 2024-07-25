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
    measurements: List[Measurement] = field(default_factory=list)
    variables: List[Variable] = field(default_factory=list)

    def to_json(self):
        # Convert the data class to a dictionary, which can be easily converted to JSON.
        import json

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
