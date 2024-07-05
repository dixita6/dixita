#########  medical disease   ###############

import streamlit as st
import pandas as pd

# Load the medical data CSV file
df = pd.read_csv('medical data (1).csv')

# Fill NaN values in the 'Symptoms' column with an empty string
df['Symptoms'] = df['Symptoms'].fillna('')

# Define the function to predict the disease and recommend the medicine
def predict_disease_and_medicine():
    # Get user input
    symptoms = st.text_input("Enter your symptoms (comma-separated):")
    if symptoms:
        symptoms_list = [symptom.strip() for symptom in symptoms.split(',')]

        # Search the dataset for matching symptoms
        matching_records = df[df['Symptoms'].str.contains('|'.join(symptoms_list), case=False)]

        if not matching_records.empty:
            # Get the predicted disease and recommended medicine
            predicted_disease = matching_records['Symptoms'].iloc[0]
            recommended_medicine = matching_records['Medicine'].iloc[0]

            # Display the results
            st.write(f"Predicted disease: {predicted_disease}")
            st.write(f"Recommended medicine: {recommended_medicine}")
        else:
            st.write("Sorry, we couldn't find a match in the dataset. Please try again with different symptoms.")

# Create the Streamlit app
st.title("Disease Prediction and Medicine Recommendation")
st.write("Enter your symptoms and we'll try to predict the disease and recommend the appropriate medicine.")

predict_disease_and_medicine()


# #########   heart disease   ###############



# import pandas as pd

# # Load the dataset
# df = pd.read_csv('heart.csv')

# # Function to find symptoms for a given disease
# def find_symptoms(disease_name):
#     symptoms = df[df['Disease'] == disease_name]['Symptoms']
#     if not symptoms.empty:
#         return symptoms.values[0]
#     else:
#         return "Disease not found in the dataset."

# # Example usage
# disease = "COVID-19    
# symptoms = find_symptoms(disease)
# print(f"Symptoms of {disease}: {symptoms}")


# import pandas as pd

# # Load the dataset (replace 'your_dataset.csv' with your actual dataset path)
# df = pd.read_csv('your_dataset.csv')

# # Print column names to verify
# print("Columns in the DataFrame:", df.columns)

# # Define a function to find symptoms based on the dataset
# def find_symptoms(label):
#     symptoms = []
    
#     # Check each row for matching label
#     for index, row in df.iterrows():
#         if row['class'] == label:  # Use the correct column name 'class'
#             # Example: If 'height' feature is indicative of a symptom
#             if row['height'] == 1:
#                 symptoms.append('Height-related symptom')
#             # Add more conditions for other features as needed
            
#     return symptoms

# # Define a function to provide advice based on the label
# def provide_advice(label):
#     if label == 1:
#         return "Advice for class 1"
#     elif label == 2:
#         return "Advice for class 2"
#     elif label == 3:
#         return "Advice for class 3"
#     elif label == 4:
#         return "Advice for class 4"
#     elif label == 5:
#         return "Advice for class 5"
#     elif label == 6:
#         return "Advice for class 6"
#     else:
#         return "Class not found"

# # Example usage:
# label_to_check = 1  # Replace with any label you want to check
# symptoms = find_symptoms(label_to_check)
# advice = provide_advice(label_to_check)

# print(f"Symptoms for label {label_to_check}: {symptoms}")
# print(f"Advice: {advice}")

