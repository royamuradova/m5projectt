# triage_system.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Tuple
import heapq


@dataclass
class Patient:
    """
    Represents a patient in the triage system.

    Attributes:
        name: Patient's name.
        severity: Integer 1–5 (1 is MOST severe).
        arrival_order: Auto-incremented number to break ties.
    """
    name: str
    severity: int
    arrival_order: int


class HospitalTriageSystem:
    """
    Priority-queue-based hospital triage system.

    Uses a min-heap with tuples:
        (severity, arrival_order, patient_object)

    This ensures:
        - Lower severity number has higher priority.
        - For the same severity, earlier arrival is seen first.
    """

    _arrival_counter: int = 0  # static/class-level counter

    def __init__(self) -> None:
        self._queue: List[Tuple[int, int, Patient]] = []

    # ---- internal helper for arrival order -----------------------------

    @classmethod
    def _next_arrival(cls) -> int:
        """Return the next arrival number and increment the counter."""
        cls._arrival_counter += 1
        return cls._arrival_counter

    # ---- ADT operations -----------------------------------------------

    def is_empty(self) -> bool:
        """Return True if there are no patients waiting."""
        return len(self._queue) == 0

    def size(self) -> int:
        """Return the number of patients in the queue."""
        return len(self._queue)

    def add_patient(self, name: str, severity: int) -> None:
        """
        Add a new patient to the triage queue.

        Args:
            name: patient name (non-empty string)
            severity: integer from 1 (most severe) to 5 (least severe)

        Raises:
            ValueError if name empty or severity out of range.
        """
        if not name or not name.strip():
            raise ValueError("Patient name must not be empty.")

        if not isinstance(severity, int) or not (1 <= severity <= 5):
            raise ValueError("Severity must be an integer between 1 and 5.")

        arrival = self._next_arrival()
        patient = Patient(name=name.strip(), severity=severity, arrival_order=arrival)

        # Min-heap based on (severity, arrival_order)
        heapq.heappush(self._queue, (severity, arrival, patient))

    def peek_next(self) -> Optional[Patient]:
        """
        Return the next patient to be treated without removing them.
        Returns None if the queue is empty.
        """
        if self.is_empty():
            return None
        _, _, patient = self._queue[0]
        return patient

    def process_next(self) -> Optional[Patient]:
        """
        Remove and return the next patient to be treated.
        Returns None if the queue is empty.
        """
        if self.is_empty():
            return None
        _, _, patient = heapq.heappop(self._queue)
        return patient

    def __str__(self) -> str:
        """
        Return a readable string showing the current queue
        from next-to-be-seen to last.
        """
        if self.is_empty():
            return "Queue is currently empty."

        # Don't mutate the real queue; make a sorted copy
        temp = list(self._queue)
        temp.sort(key=lambda tup: (tup[0], tup[1]))  # (severity, arrival)

        lines = ["Current queue (next to be seen first):"]
        for severity, arrival, patient in temp:
            lines.append(
                f"  {patient.name} (severity {severity}, arrival #{arrival})"
            )
        return "\n".join(lines)
