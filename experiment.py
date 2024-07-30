from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from dataclasses import dataclass

Base = declarative_base()


@dataclass
class Measurement(Base):
    __tablename__ = "measurements"
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    experiment = relationship("Experiment", back_populates="measurements")
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    values = relationship("MeasurementValue", back_populates="measurement")
    id = Column(Integer, primary_key=True, autoincrement=True)

    def take_measurement(self, value: float):
        self.values.append(MeasurementValue(value=value))


@dataclass
class MeasurementValue(Base):
    __tablename__ = "measurement_values"
    value = Column(Float, nullable=False)
    measurement = relationship("Measurement", back_populates="values")
    measurement_id = Column(Integer, ForeignKey("measurements.id"))
    id = Column(Integer, primary_key=True, autoincrement=True)


@dataclass
class Variable(Base):
    __tablename__ = "variables"
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    value = Column(Integer, nullable=False)  # Storing Any type as string
    experiment = relationship("Experiment", back_populates="variables")
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    id = Column(Integer, primary_key=True, autoincrement=True)


@dataclass
class Experiment(Base):
    __tablename__ = "experiments"
    experiment = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    measurements = relationship("Measurement", back_populates="experiment")
    variables = relationship("Variable", back_populates="experiment")
    id = Column(Integer, primary_key=True, autoincrement=True)

    def get_measurement(self, source: str):
        # Get a measurement from the experiment.
        for m in self.measurements:
            if m.name == source:
                return m
        raise ValueError(f"Measurement {source} not found in the experiment.")

    def take_measurement(self, source: str | Measurement, value: float):
        measurement: Measurement = (
            source if isinstance(source, Measurement) else self.get_measurement(source)
        )
        measurement.take_measurement(value)
