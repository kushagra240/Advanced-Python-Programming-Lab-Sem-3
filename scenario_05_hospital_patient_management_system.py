class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def get_category(self):
        if self.treatment_cost >= 5000:
            return "Special"
        return "General"

    def __str__(self):
        return (
            f"Patient ID: {self.patient_id}, "
            f"Name: {self.name}, "
            f"Treatment Cost: ₹{self.treatment_cost}, "
            f"Category: {self.get_category()}"
        )


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        print(f"\nPatients in {self.name}:\n")
        if not self.patients:
            print("No patients registered.")
            return
        for patient in self.patients:
            print(patient)


def main():
    hospital = Hospital("Sunrise Hospital")

    hospital.add_patient(Patient("P101", "Ritu", 3200))
    hospital.add_patient(Patient("P102", "Vikram", 7800))
    hospital.add_patient(Patient("P103", "Sonia", 4600))
    hospital.add_patient(Patient("P104", "Amit", 9200))

    hospital.display_patients()


if __name__ == "__main__":
    main()
