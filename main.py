import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select box, and sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get list of dates and temperature or sky data
    try:
        filtered_data = get_data(place, days)
    except KeyError:
        st.error("Place input is not a known place")
        st.stop()

    dates = [data_dict["dt_txt"] for data_dict in filtered_data]

    if option == "Temperature":
        temperatures = [i["main"]["temp"] - 273.15 for i in filtered_data]

        # Plot temperature
        figure = px.line(x=dates, y=temperatures,
                         labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [data_dict["weather"][0]["main"] for data_dict in filtered_data]

        # Load sky images
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "image/snow.png"}
        image_paths = [images[condition] for condition in sky_conditions]
        captions = [dates[i]for i in range(len(dates))]
        st.image(image_paths, caption=captions, width=176)
