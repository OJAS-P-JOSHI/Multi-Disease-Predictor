import pickle
import streamlit as st

# loading the saved models

diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))


# Sidebar navigation
selected = st.sidebar.selectbox('Navigation',
                                ['Home',
                                 'Diabetes Prediction',
                                 'Heart Disease Prediction',
                                 'Parkinsons Prediction'])

# Home Page
if selected == 'Home':
    # Title and description of the application
    st.image('Logo.png', use_column_width=True)

    st.write('Welcome to the Multiple Disease Prediction System! This application allows you to predict different diseases using machine learning models.')

    st.write('Please select a disease prediction from the sidebar to get started.')

    # User Guide
    st.header("User Guide")
    st.write("""
    ### 1) Diabetes Prediction
    
    **Pregnancies**: This typically ranges from 0 to 7.
    
    **Glucose**: Plasma glucose concentration in a 2-hour oral glucose tolerance test is typically between 0 and 199 mg/dL.
    
    **BloodPressure**: Diastolic blood pressure readings in this dataset range from 0 to 120 mmHg, but are likely lower in most cases.
    
    **SkinThickness**: Triceps skin fold thickness, measured in millimeters, typically falls between 0 and 99 mm.
    
    **Insulin**: 2-Hour serum insulin levels are measured in microU/mL (uU/mL) and can range from 0 to 200 in this dataset, but this may vary.
    
    **BMI**: Body mass index (BMI) is a calculated value based on weight and height. In this dataset, it ranges from 0 to 70, which is unrealistic for high values.
    
    **DiabetesPedigreeFunction**: This is a complex number that considers family history of diabetes. It typically ranges between 0.0 and 2.0.
    
    **Age**: Age ranges from 20 to 120 years, though values above 100 are unlikely in the dataset.
             
    ### 2) Heart Disease Prediction
    
    **Age**: Age ranges from 20 to 120 years in the dataset, though extreme highs are biologically unlikely.
    
    **Sex**: 0 for female, 1 for male.
    
    **Chest Pain Type (cp)**: 
        - 0: Typical angina
        - 1: Atypical angina
        - 2: Non-anginal pain
        - 3: Asymptomatic
    
    **Resting Blood Pressure (trestbps)**: Typically ranges from around 90 to 200 mmHg, though the dataset allows 0 to 120 mmHg.
    
    **Cholesterol (chol)**: Cholesterol in mg/dL. No strict range, but generally lower is better.
    
    **Fasting Blood Sugar (fbs)**: 
        - 0: Fasting blood sugar <= 120 mg/dL
        - 1: Fasting blood sugar > 120 mg/dL
    
    **Resting Electrocardiographic Results (restecg)**: 
        - 0: Normal
        - 1: Having ST-T wave abnormality
        - 2: Possible or definite left ventricular hypertrophy
    
    **Maximum Heart Rate Achieved During Exercise (thalach)**: No strict range, but a healthy heart rate during exercise can vary depending on age and fitness level.
    
    **Exercise Induced Angina (exang)**: 
        - 0: No exercise induced angina
        - 1: Yes
    
    **ST Depression Induced by Exercise Relative to Rest (oldpeak)**: Ranges from 0.0 upwards, higher values are not ideal.
    
    **Slope of the Peak Exercise ST Segment (slope)**: 
        - 0: Upsloping
        - 1: Flat
        - 2: Downsloping
    
    **Number of Major Vessels Colored by Fluoroscopy (ca)**: Ranges from 0 (no major vessels colored) to 3 (3 major vessels colored).
    
    **Thallium Stress Test Result (thal)**: 
        - 3: Normal
        - 6: Fixed defect
        - 7: Reversible defect
    ### 3) Parkinson's Disease Prediction
    
    **MDVP Fundamental Frequency (MDVP_Hz)**: 
        - Same as pitch (fo, fhi, flo).
        - Adults: Males (100-150 Hz), Females (160-250 Hz) (very rough guide).
    
    **Shimmer**: 
        - Shimmer_percent: Less than 10%.
        - Shimmer_dB: Less than 0.3 dB.
    
    **HNR (Harmonics-to-Noise Ratio)**: 
        - Lower is generally better, but specific range depends on the analysis method.
    
    **D2, RPDE, PPE, DFA, Spread1, Spread2**: 
        - These measures don't have well-defined general ranges due to the complexity of the measures and variations in calculation methods.
    
    """)
# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]

            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        except ValueError:
            st.error("Please enter valid numerical values for all input fields.")
            diab_diagnosis = ''
    st.success(diab_diagnosis)
# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            st.error("Please enter valid numerical values for all input fields.")
            heart_diagnosis = ''
    st.success(heart_diagnosis)
# Parkinson's Prediction Page
elif selected == "Parkinsons Prediction":
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    # code for Prediction
    parkinsons_diagnosis = ''
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            st.error("Please Enter Valid Numerical Values for All Input Fields.")
            parkinsons_diagnosis = ''
    st.success(parkinsons_diagnosis)

else:
    st.write("Invalid user input")
