import requests
from twilio.rest import Client


api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "d07cad9c0014bbd26061b989bb5d774f"
account_sid = "AC63107ae8b6fce633501cbae60e450785"
auth_token = "001c0875f0116ccc348ade6196298a9e"

MY_LAT = 5.603717
MY_LOG = -0.186964

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LOG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


# getting first 12 hours
weather_slice = weather_data["hourly"][:12]

will_rain = False

# getting the condition code for all the 12 hours
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today remember to bring your umbrella",
        from_="+12765009503",
        to="+233240939415"
    )
    print(message.status)



