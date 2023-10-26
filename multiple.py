# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:07:41 2023

@author: Micaiah.O
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

#Loading the saved models

diabetes_model = pickle.load(open('Diabmodel.sav', 'rb'))

heart_model = pickle.load(open('Heart.sav', 'rb'))


parkinson_model = pickle.load(open('Parkinson.sav', 'rb'))

# Adding sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Micaiah4Data Multiple Prediction System',
                           
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson Disease Prediction'],
                           
                           icons = ['moisture','heart-pulse-fill','person'],
                           
                           default_index = 0)
    



#Diabetes Prediction Page
    
if (selected == 'Diabetes Prediction'):
    
    st.title ('Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number Of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('insulin Level')
        
    with col3:
        BMI = st.text_input('Body Mass Index Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input(' Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('How Old Are You')
        
    #code for prediction
    diab_diagnosis = ''
    
    #Prediction Button
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0]==1):
            diab_diagnosis = 'WE ARE SORRY TO INFORM YOU THAT YOU ARE DIABETIC'

        else:
            diab_diagnosis = 'CONGRATULATIONS YOU ARE NOT DIABETIC'        
        
    st.success(diab_diagnosis)



        
# For Heart Disease



if (selected == 'Heart Disease Prediction'):
    
    st.title ('Heart Disease Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('How Old Are You')
    
    with col2:
        sex = st.text_input('Your Gender(1=Male, 0= Female)')
        
    with col3:
        cp = st.text_input('Chest pain Type')
    
    with col1:
        trestbps = st.text_input('Resting Blood Presure Value')
    
    with col2:
        chol = st.text_input('Serum Cholestoral Value in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting blood Sugar(>120 mg/dl)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate Value')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
         oldpeak = st.text_input('ST Depression Induced By Exercise')
         
    with col2:
         slope = st.text_input('Slope Of The Peak Exercise ST Segment')
         
    with col3:
         ca = st.text_input('number of major vessels by flourosopy')

    with col1:
        thal = st.text_input('thal: 0= Error, 1= Fixed Defect, 2= Normal, 3= Reversable Effect')
        
    heart_diagnosis = ''
    
    #Prediction Button
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
        if (heart_prediction[0]==1):
            heart_diagnosis = 'WE ARE SORRY TO INFORM YOU THAT YOU HAVE HEART DISEASE'

        else:
            heart_diagnosis = 'CONGRATULATIONS YOU DO NOT HAVE HEART DISEASE'        
        
    st.success(heart_diagnosis)      


#For brest cancer

    

if (selected == 'Parkinson Disease Prediction'):
    
    st.title ('Parkinson Disease Prediction Using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    
    with col4:
        Jitter_percent  = st.text_input('MDVP:Jitter(%)')
    
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
        
    parkinson_diagnosis = ''
    
    #Prediction Button
    if st.button('Parkinson Test Result'):
        parkinson_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
    
        if (parkinson_prediction[0]==1):
            parkinson_diagnosis = 'WE ARE SORRY TO INFORM YOU THAT YOU HAVE HEART DISEASE'

        else:
            parkinson_diagnosis = 'CONGRATULATIONS YOU DO NOT HAVE HEART DISEASE'        
        
    st.success(parkinson_diagnosis)      

    