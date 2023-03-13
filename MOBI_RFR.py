import pandas as pd
from joblib import load
import streamlit as st 
import re
import seaborn as sns
import matplotlib.pyplot as plt

##---Import data of evacuate by city and by day
def read_csv():
    df = pd.read_csv(r"C:\Users\USER\Documents\python\Mobi\Mobi\mobi-ML\CSV_file_new\data_with_encoder.csv")
    print(df)
    return df


##---Creating a dictionary of city names and their code
def dict_cities(df):
    dict_of_city = pd.Series(df.origin.values,index=df.origin_encoder).to_dict()
    # print(dict_of_city)
    return dict_of_city


##---Creating a list of city names and their code
def list_cities(dict_of_city):
    my_list = [f"{key}: {value}" for key, value in dict_of_city.items()]
    # print(my_list)
    return my_list


##---Loaded model
loaded_model = load(r'C:\Users\USER\Documents\python\Mobi\Mobi\mobi-ML\CSV_file_new\model.joblib')


##---Display Diagram of evacuate by choose city all days
def diagram_of_city(df,title):
    sub_title="מספר המתפנים בכל ימי המבצע ב" + title
    days_x="ימי הלחימה"
    evacuees_y="כמות מתפנים"

    x = list(df[df['origin']==title]['day'])
    y = list(10**df[df['origin']==title]['trips'])
    y = list(map(int, y))

    ax = sns.barplot(x=x, y=y, data=df)
    ax.bar_label(ax.containers[0])
    
    ax.set_title(sub_title[::-1], fontsize=13)
    plt.xlabel(days_x[::-1])
    plt.ylabel(evacuees_y[::-1])
    return ax.figure


##---Streamlit
def display_streamlit():

    df = read_csv()
    dict_of_city = dict_cities(df)
    list_of_city = list_cities(dict_of_city)

    st.title("Predicting the amount of evacuees from a certain city on a certain day of fighting")
    st.subheader("By RandomForestRegressor")

    ##---Selectbox of cities
    list_city = list(map(lambda x: re.sub(r'[^א-ת ]', '', x), list_of_city))
    option_city = st.selectbox('Select the city to predict',list_city)
    st.write('You selected:', option_city)

    ##---Selectbox of days
    list_day = [*range(1, 14, 1)]
    option_day = st.selectbox('Select the day to predict',list_day)
    st.write('You selected:', option_day)

    new_dict_of_city = {str(key): value for key, value in dict_of_city.items()}

    for key, value in new_dict_of_city.items():  
        if value == option_city.lstrip():  
            print(f"The key of {option_city} in the dictionary is: ", key)  
            city_code=key

    ##---Prediction
    new_prediction = loaded_model.predict([[int(option_day), int(city_code)]])
    new_prediction = re.sub(r'[^\d.]','',str(new_prediction))

    print(re.sub(r'[^\d.]','',str(new_prediction)))

    st.write(f'The amount of people expected to evacuate from {option_city} on the {option_day} day of fighting is:')
    st.write(f'**{int(10**float(new_prediction))}**')

    st.pyplot(diagram_of_city(df,option_city.lstrip()))

    
#####----MAIN

display_streamlit()
