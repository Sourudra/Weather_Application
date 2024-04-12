import streamlit as st
import requests

#Made by Sourudra
# Mapping of weather condition codes to weather emoji
weather_icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Fog": "🌫️",
    "Tornado": "🌪️"
}

st.header('City Climates: Weather Insights for Every City')

if(st.button("More Info")):
    st.text("Crafted with Python and Streamlit: An Easy Platform for Weather Insight")

api_key = 'c3e713475ec50ad478b160af1dab4d3e'

user_input = st.text_input("Enter Your City:")

if user_input:
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        st.write("No City Found!")
    else:
        weather_main = weather_data.json()['weather'][0]['main']
        weather_description = weather_data.json()['weather'][0]['description']
        temp_fahrenheit = round(weather_data.json()['main']['temp'])
        temp_celsius = round((temp_fahrenheit - 32) / 1.8)
        humidity = weather_data.json()['main']['humidity']
        wind_speed = weather_data.json()['wind']['speed']
        visibility = weather_data.json().get('visibility', 'N/A')

        
        weather_icon = weather_icons.get(weather_main, "❓")

        st.info(f"The weather in {user_input} is: {weather_main} {weather_icon}")
        st.success(f"Description: {weather_description}")
        st.info(f"Temperature: {temp_celsius}ºC / {temp_fahrenheit}ºF")
        st.success(f"Humidity: {humidity}%")
        st.info(f"Wind Speed: {wind_speed} mph")
        st.success(f"Visibility: {visibility} meters")
