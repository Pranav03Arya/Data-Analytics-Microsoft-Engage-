from matplotlib import image
import streamlit as st 
import pandas as pd
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import requests
import webbrowser


#title
st.title("Automobile Production Statistics")
st.write("The desired analytics for the automobile cars and the manufacturers")

#csv file and its respective table 
df = pd.read_csv("cars_engage_2022data.csv", index_col=[0])
st.write (df.head(5))

#display full
if st.checkbox('show full data'):
    df


#buttons
col1, col2, col3, col4 = st.columns([0.6,1,1,1])
with col1:
    url = 'http://localhost:8501/#bar-graphs'
    if st.button('BAR GRAPH'):
        webbrowser.open_new(url)
with col2:
    url ='http://localhost:8501/#box-plots-graphs'
    if st.button('BOX PLOT GRAPH'):
        webbrowser.open_new(url)
with col3:
    url = 'http://localhost:8501/#stacked-bar-graph'
    if st.button('STACKED BAR GRAPH'):
         webbrowser.open_new(url)
with col4:
    url = 'http://localhost:8501/#line-graphs'
    if st.button('LINE GRAPH'):
        webbrowser.open_new(url)



#sidebar
st.sidebar.title('Satisfactory Ratings')

rating = st.sidebar.radio('Are you satisfies with this app',('Yes','No','Not Sure'))
if rating == 'Yes':
    st.sidebar.success('Thank you for selecting Yes')

elif rating == 'No':
    st.sidebar.success('Thank you for selecting No')

elif rating == 'Not Sure':
    st.sidebar.success('Thank you for selecting Not Sure')

rating = st.sidebar.selectbox("How much would you rate this App?",['5 Stars', '4 Stars', '3 Stars','2 Stars','1 Star'])  


st.subheader('BAR GRAPHS')
#2percent missing values 
st.image('Percentage of missing values.png',clamp='False',caption='Percentage of missing values for the car companies', output_format='auto')
st.markdown(' **There are some values in data set which have an EMPTY space or NULL values. Collecting all the null values from various columns and present the amount od null values each column contains which means, It shows the car has a particular feature or not.**.')

#3boot space vs count 
st.image('Bootspace.png',clamp='False',caption='Bootspace in Liters vs Number if vehicles in that range ', output_format='auto')
st.markdown('**This provides the Bootspace and number of cars having that particular amount of bootspace in Liters.**.')

#4Wheelbase vs count
st.image('wheelbase.png',clamp='False',caption='Wheelbase vs Number if vehicles in that range ', output_format='auto')
st.markdown('**This shows the number of cars having a particular Wheelbase measurements and the number of cars falling in a particular wheelbase measurements.**.')

#9body type vs price bar
st.image('Price_bodytype.png',clamp='False',caption='Body type of a particular model vs Price df vehicles in that Range ', output_format='auto')
st.markdown('**This shows how much a particular model of car would cost  with sports model being the most expensive.**.')

#10make vs price type 
st.image('make_price.png',clamp='False',caption='Manufacturer vs Price of vehicles in that range ', output_format='auto')
st.markdown('**This shows the car companies and the cost of the models which it ranges from like the luxury cars are expensive and companies like TATA and Maruti produce cost effective models.**.')

st.subheader('BOX PLOTS GRAPHS')
#5fuel type vs price
st.image('fuel_type.png',clamp='False',caption='Fuel Type vs Price of the vehicle', output_format='auto')
st.markdown('**This is a different graph showing the range of price for different fuel types petrol and diesel showing a wide range of cost.**.')

#6bluetooth vs price
st.image('bluetooth.png',clamp='False',caption='Bluetooth availability vs the price of the vehicle  ', output_format='auto')
st.markdown('**This graph shows the at what prices can we get the facility of Bluetooth**.')

#7type vs price 
st.image('type.png',clamp='False',caption='Car Gearbox Type vs Price of the car ', output_format='auto')
st.markdown('**This graph shows different models having different types of gearbox and number of models having a particular gearbox**.')

#7.2type vs price 
st.image('body_type.png',clamp='False',caption='Car Body Type vs Price of the car ', output_format='auto')
st.markdown('**This graph contains different body type models and the price regarding that particular model**.')

st.subheader('STACKED BAR GRAPH')
#8make vs Body_type
st.image('make_body_type.png',clamp='False',caption='Different types of car Companies vs Price Range', output_format='auto')
st.markdown('**This graph shows the different types of car body types in different companies. There are wide range of companies having different body types.**.')

#11make and fuel type bar graph 
st.image('make_fueltype.png',clamp='False',caption='Companies and the various fuel types they use ', output_format='auto')
st.markdown('**This graph shows companies using different types of fuels in their car models.**.')

st.subheader('LINE GRAPHS')
#12features given and its price
st.image('feature_count.png',clamp='False',caption='Feature given and its price ', output_format='auto')
st.markdown('**This graph shows that with more amount spent on the car, more the features will be provided and vice versa.**.')

#1image and content
st.image('airbags.png',clamp='False',caption='Number of Airbags vs Price', output_format='auto')
st.markdown('**The Price Range varies from the number of Airbags a car consists. More the number of Airbags more the price and vice versa. The graph shows a sudden increase between 4 to 6 Airbags consisting more cars and price ranges.**.')
