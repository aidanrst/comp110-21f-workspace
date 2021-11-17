"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730433261"


class Simpy:
    """A simple emulation of NumPy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill our values array by mutating object called on."""
        # Start with an empty values list
        self. values = []
        # Loop for 'times' number of times
        i: int = 0
        while i < times:
            #   append value parameter to the values list
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        # Start an empty values list
        self.values = []
        # Be sure step is not 0.0 by asserting
        assert step != 0.0
        # When step is positive:
        if step > 0.0:
            # Initialize next value to start
            next_value: float = start
            # While next value is less than stop value
            while next_value < stop:
                # Add next value to values list
                self.values.append(next_value)
                # Update next value by adding the step to it
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Delegate this algo to the built-in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1

        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1

        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for equality test."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1

        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater-than test."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1

        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overload for subscription notation."""
        if isinstance(rhs, int):
            result_float: float = self.values[rhs]
            return result_float
        else:
            result_Simpy: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i]:
                    result_Simpy.values.append(self.values[i])
            return result_Simpy