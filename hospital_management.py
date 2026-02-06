def search_patients_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"] == disease]


# Example usage
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"
result = search_patients_by_disease(patients, search_disease)

print(f"Patients with {search_disease}:", result)
