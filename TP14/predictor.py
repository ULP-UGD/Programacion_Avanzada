import joblib
import pandas as pd
import numpy as np

class DiabetesPredictor:
    def __init__(self, package_path):
        try:
            package = joblib.load(package_path)
            self.model = package['model']
            self.scaler = package['scaler']
        except FileNotFoundError:
            raise FileNotFoundError(f"Asegúrate de que '{package_path}' esté en la misma carpeta.")
        except KeyError:
            raise KeyError(f"El archivo '{package_path}' no contiene 'model' y 'scaler'.\n"
                           "Por favor, vuelve a exportarlo desde tu notebook asegurándote de guardar un diccionario.")

    def make_prediction(self, input_data):
        feature_names = [
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
        ]
        
        input_df = pd.DataFrame([input_data], columns=feature_names)
        
        input_scaled = self.scaler.transform(input_df)
        
        prediction = self.model.predict(input_scaled)
        probability = self.model.predict_proba(input_scaled)
        
        result_text = "Sí" if prediction[0] == 1 else "No"
        diabetes_prob = probability[0][1] * 100
        
        return f"Predicción Diabetes: {result_text} ({diabetes_prob:.2f}%)"