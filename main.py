import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ", value="Tokyo")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates, required_data = get_data(place, days, option)

if option == "Temperature":
    figure = px.line(x=dates, y=required_data,
                     labels={"x": "Date", "y": "Temperature (C)"})
    st.plotly_chart(figure)
if option == "Sky":
    images = [f"images/{required_data[i].lower()}.png" for i in range(len(dates))]
    captions = [dates[i]for i in range(len(dates))]
    st.image(images, caption=captions, width=176)
