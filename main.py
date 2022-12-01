import streamlit as st
import plotly.express as px


def get_data(days_local):
    dates_local = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures_local = [10, 11, 15]
    temperatures_local = [days_local * i for i in temperatures_local]
    return dates_local, temperatures_local


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates, temperatures = get_data(days)

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
