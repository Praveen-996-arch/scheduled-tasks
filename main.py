API_KEY = os.environ.get("OMW_API_KEY")
MY_LAT = 33.387939
MY_LNG = -86.806122
import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

# client.api.account.messages.create(
#     to="+2055099890",
#     from_="+18447430228",
#     body="Hello there!")
params={
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    "appid" : API_KEY,
    "cnt" : 6
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= params)
response.raise_for_status()
data = response.json()

for list in data["list"]:
    weather_id = list["weather"][0]["id"]
    if weather_id < 700:
    # weather_description = list["weather"][0]["description"]

        client.api.account.messages.create(
            to="whatsapp:+12052532490",
            from_="whatsapp:+14155238886",
            body=f"Bring an umbrella. Its going to rain today at {list["dt_txt"]} ")


