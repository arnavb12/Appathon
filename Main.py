import tkinter as tk
from tkinter import ttk, messagebox, Listbox, Scrollbar
from ttkthemes import ThemedStyle

disease_symptoms = {'(vertigo) Paroymsal  Positional Vertigo': ['nausea',
  'loss_of_balance',
  'unsteadiness',
  'spinning_movements',
  'vomiting',
  'headache'],
 'AIDS': [' high_fever',
  'patches_in_throat',
  'extra_marital_contacts',
  'muscle_wasting'],
 'Acne': ['skin_rash', 'scurring', 'pus_filled_pimples', 'blackheads'],
 'Alcoholic hepatitis': ['distention_of_abdomen',
  'history_of_alcohol_consumption',
  'fluid_overload',
  'yellowish_skin',
  'swelling_of_stomach',
  'vomiting',
  'abdominal_pain'],
 'Allergy': ['shivering',
  'watering_from_eyes',
  'continuous_sneezing',
  'chills'],
 'Arthritis': ['movement_stiffness',
  'painful_walking',
  'swelling_joints',
  'muscle_weakness',
  'stiff_neck'],
 'Bronchial Asthma': ['high_fever',
  'family_history',
  'fatigue',
  'cough',
  'mucoid_sputum',
  'breathlessness'],
 'Cervical spondylosis': ['back_pain',
  'neck_pain',
  'loss_of_balance',
  'dizziness',
  'weakness_in_limbs'],
 'Chicken pox': ['loss_of_appetite',
  'itching',
  'high_fever',
  'skin_rash',
  'lethargy',
  'swelled_lymph_nodes',
  'fatigue',
  'malaise',
  'headache',
  'red_spots_over_body',
  'mild_fever'],
 'Chronic cholestasis': ['loss_of_appetite',
  'itching',
  'nausea',
  'yellowish_skin',
  'vomiting',
  'yellowing_of_eyes',
  'abdominal_pain'],
 'Common Cold': ['muscle_pain',
  'high_fever',
  'congestion',
  'redness_of_eyes',
  'loss_of_smell',
  'continuous_sneezing',
  'swelled_lymph_nodes',
  'fatigue',
  'cough',
  'malaise',
  'throat_irritation',
  'sinus_pressure',
  'chest_pain',
  'headache',
  'phlegm',
  'runny_nose',
  'chills'],
 'Dengue': ['loss_of_appetite',
  'joint_pain',
  'skin_rash',
  'high_fever',
  'nausea',
  'back_pain',
  'muscle_pain',
  'pain_behind_the_eyes',
  'fatigue',
  'malaise',
  'vomiting',
  'headache',
  'red_spots_over_body',
  'chills'],
 'Diabetes ': ['polyuria',
  'excessive_hunger',
  'lethargy',
  'irregular_sugar_level',
  'increased_appetite',
  'fatigue',
  'weight_loss',
  'blurred_and_distorted_vision',
  'obesity',
  'restlessness'],
 'Dimorphic hemmorhoids(piles)': ['pain_during_bowel_movements',
  'bloody_stool',
  'pain_in_anal_region',
  'irritation_in_anus',
  'constipation'],
 'Drug Reaction': ['itching',
  'skin_rash',
  'spotting_ urination',
  'stomach_pain',
  'burning_micturition'],
 'Fungal infection': ['itching',
  'skin_rash',
  'nodal_skin_eruptions',
  'dischromic _patches'],
 'GERD': ['cough',
  'chest_pain',
  'stomach_pain',
  'vomiting',
  'ulcers_on_tongue',
  'acidity'],
 'Gastroenteritis': ['sunken_eyes',
  'vomiting',
  'dehydration',
  'diarrhoea'],
 'Heart attack': ['chest_pain', 'vomiting', 'sweating', 'breathlessness'],
 'Hepatitis B': ['loss_of_appetite',
  'tching',
  'lethargy',
  'fatigue',
  'receiving_unsterile_injections',
  'yellowish_skin',
  'malaise',
  'yellowing_of_eyes',
  'dark_urine',
  'yellow_urine',
  'abdominal_pain',
  'receiving_blood_transfusion'],
 'Hepatitis C': ['loss_of_appetite',
  'nausea',
  'family_history',
  'fatigue',
  'yellowish_skin',
  'yellowing_of_eyes'],
 'Hepatitis D': ['loss_of_appetite',
  'joint_pain',
  'nausea',
  'fatigue',
  'yellowish_skin',
  'vomiting',
  'yellowing_of_eyes',
  'dark_urine',
  'abdominal_pain'],
 'Hepatitis E': ['loss_of_appetite',
  'joint_pain',
  'high_fever',
  'nausea',
  'fatigue',
  'yellowish_skin',
  'vomiting',
  'yellowing_of_eyes',
  'dark_urine',
  'coma',
  'abdominal_pain',
  'stomach_bleeding',
  'acute_liver_failure'],
 'Hypertension ': ['lack_of_concentration',
  'loss_of_balance',
  'chest_pain',
  'dizziness',
  'headache'],
 'Hyperthyroidism': ['excessive_hunger',
  'irritability',
  'fatigue',
  'weight_loss',
  'sweating',
  'fast_heart_rate',
  'abnormal_menstruation',
  'muscle_weakness',
  'restlessness',
  'diarrhoea',
  'mood_swings'],
 'Hypoglycemia': ['excessive_hunger',
  'nausea',
  'drying_and_tingling_lips',
  'fatigue',
  'palpitations',
  'slurred_speech',
  'vomiting',
  'anxiety',
  'blurred_and_distorted_vision',
  'headache',
  'sweating',
  'irritability'],
 'Hypothyroidism': ['weight_gain',
  'lethargy',
  'cold_hands_and_feets',
  'brittle_nails',
  'fatigue',
  'enlarged_thyroid',
  'depression',
  'puffy_face_and_eyes',
  'swollen_extremeties',
  'dizziness',
  'abnormal_menstruation',
  'irritability',
  'mood_swings'],
 'Impetigo': ['skin_rash',
  'high_fever',
  'blister',
  'red_sore_around_nose',
  'yellow_crust_ooze'],
 'Jaundice': ['itching',
  'high_fever',
  'fatigue',
  'weight_loss',
  'yellowish_skin',
  'vomiting',
  'dark_urine',
  'abdominal_pain'],
 'Malaria': ['muscle_pain',
  'high_fever',
  'nausea',
  'vomiting',
  'headache',
  'sweating',
  'diarrhoea',
  'chills'],
 'Migraine': ['excessive_hunger',
  'visual_disturbances',
  'depression',
  'blurred_and_distorted_vision',
  'headache',
  'acidity',
  'irritability',
  'stiff_neck',
  'indigestion'],
 'Osteoarthristis': ['joint_pain',
  'neck_pain',
  'hip_joint_pain',
  'knee_pain',
  'painful_walking',
  'swelling_joints'],
 'Paralysis (brain hemorrhage)': ['altered_sensorium',
  'weakness_of_one_body_side',
  'vomiting',
  'headache'],
 'Peptic ulcer diseae': ['loss_of_appetite',
  'vomiting',
  'passage_of_gases',
  'abdominal_pain',
  'internal_itching',
  'indigestion'],
 'Pneumonia': ['high_fever',
  'fatigue',
  'cough',
  'malaise',
  'chest_pain',
  'phlegm',
  'rusty_sputum',
  'sweating',
  'fast_heart_rate',
  'breathlessness',
  'chills'],
 'Psoriasis': ['joint_pain',
  'skin_rash',
  'silver_like_dusting',
  'skin_peeling',
  'small_dents_in_nails',
  'inflammatory_nails'],
 'Tuberculosis': ['loss_of_appetite',
  'high_fever',
  'swelled_lymph_nodes',
  'fatigue',
  'weight_loss',
  'cough',
  'malaise',
  'chest_pain',
  'vomiting',
  'yellowing_of_eyes',
  'phlegm',
  'sweating',
  'blood_in_sputum',
  'breathlessness',
  'mild_fever',
  'chills'],
 'Typhoid': ['high_fever',
  'nausea',
  'fatigue',
  'diarrhoea',
  'belly_pain',
  'vomiting',
  'toxic_look_(typhos)',
  'headache',
  'abdominal_pain',
  'constipation',
  'chills'],
 'Urinary tract infection': ['continuous_feel_of_urine',
  'bladder_discomfort',
  'foul_smell_of urine',
  'burning_micturition'],
 'Varicose veins': ['prominent_veins_on_calf',
  'swollen_legs',
  'swollen_blood_vessels',
  'fatigue',
  'cramps',
  'bruising',
  'obesity'],
 'hepatitis A': ['loss_of_appetite',
  'joint_pain',
  'muscle_pain',
  'nausea',
  'yellowish_skin',
  'mild_fever',
  'vomiting',
  'yellowing_of_eyes',
  'dark_urine',
  'abdominal_pain',
  'diarrhoea']
}

disease_medicines = {
    "Fungal infection": ["econazole", "clotrimazole (Canesten)"],
    "Acne": ["tretinoin", "tazarotene"],
    "Psoriasis": ["Methotrexate", "cyclosporine"],
    "Impetigo": ["dicloxaci llin", "cephalexin"],
    "hepatitis A": [ 'acetaminophen','paracetamo'],
    "Hepatitis B": ['entecavir (Baraclude)', 'tenofovir (Viread)'],
    "Hepatitis C": ['Elbasvir-Grazoprevir (Zepatier) ','Glecaprevir-Pibrentasvir (Mavyret)'],
    "Hepatitis D": ["Pegylated interferon alpha"],
    "Hepatitis E": ["interferon", "ribavirin"],
    "Alcoholic hepatitis": ["Corticosteroids", "Pentoxifylline"],
    "GERD": ['esomeprazole (Nexium)', 'lansoprazole (Prevacid)'],
    "Chronic cholestasis": ["ursodiol"],
    "Peptic ulcer diseae": ["omeprazole (Prilosec)","lansoprazole (Prevacid)"],
    "Gastroenteritis": ['operamide link (Imodium)','bismuth subsalicylate link'],
    "Jaundice": ['Iron supplements','Antihistamines'],
    "Tuberculosis": ['Rifampin', 'isoniazid'],
    "Bronchial Asthma": ['malizumab (Xolair)','mepolizumab (Nucala)'],
    "Common Cold": ['oxymetazoline nasal', 'phenylephrine nasal'],
    "AIDS": ["Abacavir", "Emtricitabine"],
    "Hypertension": ["Doxazosin", "Propranolol"],
    "Malaria": ["Doxycycline", "Mefloquine"],
    "Chicken pox": ["Acyclovir", "Valacyclovir"],
    "Dengue": ["Pain Relievers", "Acetaminophen "],
    "Typhoid": ["Ciprofloxacin", "Azithromycin"],
    "Pneumonia": ["Penicillins", "Tetracyclines"],
    "Dimorphic hemmorhoids(piles)": ["Pain Relievers", "Fiber Supplements"],
    "Heart attack": ["Aspirin", "Nitroglycerin"],
    "Hypothyroidism": ["Liothyronine (T3)", "Desiccated Thyroid Extract"],
    "Hyperthyroidism": ["Methimazole (Tapazole)", "Radioactive Iodine (I-131)"],
    "Hypoglycemia": ["Glucagon", "Dextrose (IV)"],
    "Diabetes": ["Insulin for type 1", "Metformin (Glucophage) for type 2"],
    "Osteoarthritis": ["Corticosteroids", "Hyaluronic Acid Injections"],
    "Arthritis": ["Celecoxib (Celebrex)", "Diclofenac (Voltaren)"],
    "(vertigo) Paroymsal Positional Vertigo": ["Metoclopramide (Reglan)", "Diazepam (Valium)"],
    "Urinary Tract Infection": ["Levofloxacin (Levaquin)", "Fosfomycin (Monurol)"],
    "Allergy": ["Anticholinergic Nasal Spray", "Antibiotics "],
    "Drug Reaction": ["Epinephrine", "Bronchodilators "],
    "Migraine": ["Antidepressants", "Metoclopramide (Reglan) "],
    "Paralysis (brain hemorrhage)": ["Antiplatelet Agents ", "Blood Pressure Medications"],
    "Cervical spondylosis": ["Heat and Cold Therapy", "Pain Relief Medications"]
}

medicines_list = list(set(medicine for medicines in disease_medicines.values() for medicine in medicines))

all_symptoms = sorted(list(set(symptom for symptoms in disease_symptoms.values() for symptom in symptoms)))

def suggest_medicines(*args):
    entered_text = entry_var.get().lower()
    entered_symptoms = entered_text.split(", ")
    suggested_diseases = set()

    for disease, symptoms in disease_symptoms.items():
        if any(symptom.lower() in entered_symptoms for symptom in symptoms):
            suggested_diseases.add(disease)

    update_suggested_diseases_listbox(suggested_diseases)

def update_suggested_diseases_listbox(suggested_diseases):
    suggested_diseases_listbox.delete(0, tk.END)
    for disease in suggested_diseases:
        symptoms = ", ".join(symptom for symptom in disease_symptoms[disease])
        suggested_diseases_listbox.insert(tk.END, f"{disease} - You might also be suffering from [{symptoms}]")

def suggest_medicines_for_disease():
    selected_disease_index = suggested_diseases_listbox.curselection()
    if selected_disease_index:
        selected_disease = suggested_diseases_listbox.get(selected_disease_index[0]).split(" - ")[0]
        suggested_medicines = set(disease_medicines.get(selected_disease, []))
        update_suggested_medicines_listbox(suggested_medicines)
    else:
        messagebox.showwarning("No Disease Selected", "Please select a disease.")

def update_suggested_medicines_listbox(suggested_medicines):
    suggested_medicines_listbox.delete(0, tk.END)
    for medicine in suggested_medicines:
        suggested_medicines_listbox.insert(tk.END, medicine)

def show_medicine_details():
    selected_medicine_index = suggested_medicines_listbox.curselection()
    if selected_medicine_index:
        selected_medicine = suggested_medicines_listbox.get(selected_medicine_index[0])
        medicine_details = get_medicine_details(selected_medicine)
        messagebox.showinfo("Medicine Details", medicine_details)
    else:
        messagebox.showwarning("No Medicine Selected", "Please select a medicine.")

def get_medicine_details(medicine):
    return f"Details for {medicine}:\nDescription, Dosage, Precautions, etc."

def add_symptom():
    selected_symptom_index = symptom_listbox.curselection()
    if selected_symptom_index:
        selected_symptom = symptom_listbox.get(selected_symptom_index[0])
        current_text = entry_var.get()
        if current_text:
            new_text = f"{current_text}, {selected_symptom}"
        else:
            new_text = selected_symptom
        entry_var.set(new_text)

def main():
    def on_select(event):
        selected_symptom = symptom_listbox.get(symptom_listbox.curselection())
        current_text = entry_var.get()
        if current_text:
            new_text = f"{current_text}, {selected_symptom}"
        else:
            new_text = selected_symptom
        entry_var.set(new_text)

    root = tk.Tk()
    root.title("SPACE-DOCTOR 🚀")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")
    style = ThemedStyle(root)
    style.set_theme("plastik")

    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    left_frame = ttk.Frame(main_frame)
    left_frame.grid(row=0, column=0, padx=(0, 20), pady=20, sticky="nsew")

    right_frame = ttk.Frame(main_frame)
    right_frame.grid(row=0, column=1, pady=20, sticky="nsew")

    ttk.Label(left_frame, text="Enter Your Symptoms", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=(0, 10), sticky="w")
    ttk.Label(left_frame, text="Suggested Diseases", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=(0, 10), pady=(10, 0), sticky="w")

    global entry_var
    entry_var = tk.StringVar()
    entry_var.trace_add('write', suggest_medicines)
    entry = ttk.Entry(left_frame, textvariable=entry_var, font=("Helvetica", 10, "normal"))
    entry.grid(row=1, column=0, padx=0, pady=(0, 10), sticky="ew")

    suggest_medicines_button = ttk.Button(left_frame, text="Suggest Medicines for Disease", command=suggest_medicines_for_disease)
    suggest_medicines_button.grid(row=3, column=0, padx=0, pady=10, sticky="ew")

    global suggested_diseases_listbox
    suggested_diseases_listbox = Listbox(left_frame, height=5)
    suggested_diseases_listbox.grid(row=4, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")

    diseases_scrollbar = Scrollbar(left_frame, orient="vertical", command=suggested_diseases_listbox.yview)
    suggested_diseases_listbox.config(yscrollcommand=diseases_scrollbar.set)
    diseases_scrollbar.grid(row=4, column=1, sticky="ns")

    global symptom_listbox
    symptom_listbox = Listbox(left_frame, height=10)
    symptom_listbox.grid(row=5, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")

    symptom_h_scrollbar = Scrollbar(left_frame, orient="horizontal", command=symptom_listbox.xview)
    symptom_listbox.config(xscrollcommand=symptom_h_scrollbar.set)
    symptom_h_scrollbar.grid(row=6, column=0, padx=(0, 10), sticky="ew")

    add_symptom_button = ttk.Button(left_frame, text="Add Symptom", command=add_symptom)
    add_symptom_button.grid(row=7, column=0, padx=0, pady=(10, 0), sticky="ew")

    ttk.Label(right_frame, text="Suggested Medicines", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=(0, 10), sticky="w")

    global suggested_medicines_listbox
    suggested_medicines_listbox = Listbox(right_frame, height=15)
    suggested_medicines_listbox.grid(row=1, column=0, padx=(0, 10), sticky="nsew")

    medicines_scrollbar = Scrollbar(right_frame, orient="vertical", command=suggested_medicines_listbox.yview)
    suggested_medicines_listbox.config(yscrollcommand=medicines_scrollbar.set)
    medicines_scrollbar.grid(row=1, column=1, sticky="ns")

    show_details_button = ttk.Button(right_frame, text="Show Medicine Details", command=show_medicine_details)
    show_details_button.grid(row=2, column=0, padx=0, pady=(10, 0), sticky="ew")

    suggested_medicines_listbox.bind('<Double-1>', lambda event: show_medicine_details())

    symptom_listbox.bind('<Double-1>', on_select)

    for symptom in all_symptoms:
        symptom_listbox.insert(tk.END, symptom)

    root.mainloop()

if __name__ == "__main__":
    main()
