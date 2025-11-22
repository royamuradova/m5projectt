# main_triage.py
# If this project is separate, rename this file to main.py

from triage_system import HospitalTriageSystem


def main():
    triage = HospitalTriageSystem()

    print("----- Hospital Triage System Demo -----\n")

    # Example set of patients: (name, severity)
    sample_patients = [
        ("Alice", 2),
        ("Bob", 4),
        ("Carlos", 1),
        ("Diana", 3),
        ("Evan", 2),
        ("Fatima", 1),
    ]

    # Add patients
    for name, severity in sample_patients:
        print(f"Adding patient {name} with severity {severity}")
        triage.add_patient(name, severity)

    print("\n" + str(triage) + "\n")

    # Process patients in the correct order
    print("Processing patients in priority order:\n")
    while not triage.is_empty():
        patient = triage.process_next()
        print(
            f"Now treating: {patient.name} "
            f"(severity {patient.severity}, arrival #{patient.arrival_order})"
        )

    # Peek at empty queue to show it handles gracefully
    print("\nTrying to peek on empty queue:", triage.peek_next())
    print("\nAll patients have been treated.")


if __name__ == "__main__":
    main()
