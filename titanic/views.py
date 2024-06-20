import os
import pickle
from django.shortcuts import render
import pandas as pd
from .models import Prediction

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'logistic_regression_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def predict_survival(request):
    if request.method == 'POST':
        data = request.POST
        features = {
            'Pclass': int(data['Pclass']),
            'Age': float(data['Age']),
            'SibSp': int(data['SibSp']),
            'Parch': int(data['Parch']),
            'Fare': float(data['Fare']),
            'Sex_male': int(data['Sex']),  # Sex: 1 for male, 0 for female
            'Embarked_Q': 1 if int(data['Embarked']) == 1 else 0,  # Embarked_Q: 1 for Queenstown
            'Embarked_S': 1 if int(data['Embarked']) == 2 else 0   # Embarked_S: 1 for Southampton
        }

        df = pd.DataFrame([features])
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1] * 100

        prediction_result = 'Survived' if prediction == 1 else 'Did Not Survive'

        # Save to database
        prediction_record = Prediction(
            Pclass=features['Pclass'],
            Age=features['Age'],
            SibSp=features['SibSp'],
            Parch=features['Parch'],
            Fare=features['Fare'],
            Sex_male=features['Sex_male'],
            Embarked_Q=features['Embarked_Q'],
            Embarked_S=features['Embarked_S'],
            prediction=prediction_result,
            probability=probability
        )
        prediction_record.save()

        context = {
            'prediction': prediction_result,
            'probability': f'{probability:.2f}'
        }

        return render(request, 'titanic/result.html', context)
    return render(request, 'titanic/predict.html')
