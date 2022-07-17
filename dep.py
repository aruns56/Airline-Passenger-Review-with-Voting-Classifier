# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 18:29:39 2022

@author: as
"""
import pickle
import streamlit as st 
import os
os.chdir("C://Users//as//Downloads")


pickle_in = open("clf2.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_satisfaction(TypeofTravel,FlightDistance,InflightWifiService,OnlineBoarding,InflightEntertainment,OnBoardService,LegRoomService,CheckinService,DepartureDelayInMinutes):
    prediction=classifier.predict([[TypeofTravel,FlightDistance,InflightWifiService,OnlineBoarding,InflightEntertainment,OnBoardService,LegRoomService,CheckinService,DepartureDelayInMinutes]])
    if prediction == 0:
        pred = 'Neutral/dissatisfied'
    else:
        pred = 'Satisfied'
    return pred

def main():
    st.title("Ailrine Passenger Satisfaction")
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Ailrine Passenger Satisfaction Predictor App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    TypeofTravel = st.text_input('Type Of Travel')
    FlightDistance = st.text_input('Travel Distance')
    InflightWifiService = st.slider('Inflight Wifi Service', min_value=0, max_value=5)
    OnlineBoarding = st.slider('Online Boarding', min_value=0, max_value=5)
    InflightEntertainment = st.slider('Inflight entertainment', min_value=0, max_value=5)
    OnBoardService = st.slider('On-board service', min_value=0, max_value=5)
    LegRoomService = st.slider('Leg room service', min_value=0, max_value=5)
    CheckinService = st.slider('Checkin service', min_value=0, max_value=5)
    DepartureDelayInMinutes = st.text_input("Delay in Minutes")
    
    if st.button("Predict"):
        output = predict_satisfaction(TypeofTravel,FlightDistance,InflightWifiService,OnlineBoarding,InflightEntertainment,OnBoardService,LegRoomService,CheckinService,DepartureDelayInMinutes)
        st.success('The Passenger is {}'.format(output))
        
if __name__=='__main__':
    main()