import requests
import streamlit as st

APIkey = st.secrets["API_KEY"]


def get_data(place, days, option):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    days_data = data["list"][:days*8]
    dates = [i["dt_txt"] for i in days_data]
    if option == "Temperature":
        required_data = [i["main"]["temp"]-273 for i in days_data]
    if option == "Sky":
        required_data = [i["weather"][0]["main"] for i in days_data]
    return dates, required_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3, option="Sky"))
