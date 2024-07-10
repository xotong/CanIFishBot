import telebot
from datetime import datetime, timedelta
import requests
import os
from dotenv import load_dotenv

load_dotenv()

tele_key = os.getenv("TELE_CHANNEL_ID")
bot = telebot.TeleBot(tele_key)
visualcrossing_key = os.getenv("VISUALCROSSING_KEY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	text = """Welcome to CanIFish?\n
	Here you can check for weather and fishing conditions in SG.\n\n 
	To get started, here are list of commands you can use:\n
	/start - Start the bot\n 
	/help - Get help\n 
	/ystd_rainfall - Get yesterday's total rainfall data by area\n 
	/today_rainfall - Get today's total rainfall data by area\n
	/2hr_forecast - Get 2-hour weather forecast\n
	/24hr_forecast - Get 24-hour weather forecast\n
	/tides - Get tides data\n
	"""
	bot.reply_to(message, text)

@bot.message_handler(commands=['ystd_rainfall'])
def ystd_rainfall(message):

    applicable_device_ids_mapping = {
        "S109": "LowerSeletarReservior",
        "S40": "UpperSeletarReservior",
        "S08": "LowerPeirceReservior",
        "S69": "UpperPeirceReservior",
        "S66": "KranjiReservior",
        "S33": "PandanReservior1",
        "S71": "PandanReservior2",
        "S35": "PandanReservior3",
        "S07": "MacRitchieReservior",
        "S119": "MarinaReservior",
        "S81": "PunggolConeyReservior",
        "S900": "YishunDam",
        "S220": "PunggolParkPond",
        "S107": "BedokJetty",
        "S84": "BedokReservior",
        "S108": "MarinaBarrage",
        "S94": "DBestFishing",
    }

    total_rainfall_by_device_id = {
        "S109": 0,
        "S40": 0,
        "S08": 0,
        "S69": 0,
        "S66": 0,
        "S33": 0,
        "S71": 0,
        "S35": 0,
        "S07": 0,
        "S119": 0,
        "S81": 0,
        "S900": 0,
        "S220": 0,
        "S107": 0,
        "S84": 0,
        "S108": 0,
        "S94": 0,
    }

    # Initializing Data Required for GET Request
    yesterday = datetime.now() - timedelta(days=1)
    rainfall_request_url = "https://api.data.gov.sg/v1/environment/rainfall"
    params = {
        "date": yesterday.strftime("%Y-%m-%d")
    }

    # Making GET Request
    response = requests.get(rainfall_request_url, params=params)
    rainfall_data = response.json()["items"]

    # Calculating Total Rainfall by Device ID
    for perrecord in rainfall_data:
        for reading in perrecord["readings"]:
            if reading["station_id"] in applicable_device_ids_mapping:
                total_rainfall_by_device_id[reading["station_id"]] += reading["value"]

    text = "Yesterday's Total Rainfall by Area:\n\n"

    # Printing Total Rainfall by Device ID
    updatedtext = text
    for device_id, rainfall in total_rainfall_by_device_id.items():
        updatedtext += "{}: {:.2f}mm\n".format(applicable_device_ids_mapping[device_id], rainfall)
    updatedtext += "\n\nNote: With high amount of rainfall, some anglers may find it difficult to fish as the water may be murky and the fish may not be biting. Thus, do remember to bring along darker cloured lures to increase your chances of catching fish. However, do note that this assumption are based on terrain and depth of water."

    bot.reply_to(message, updatedtext)

@bot.message_handler(commands=['today_rainfall'])
def today_rainfall(message):

    applicable_device_ids_mapping = {
        "S109": "LowerSeletarReservior",
        "S40": "UpperSeletarReservior",
        "S08": "LowerPeirceReservior",
        "S69": "UpperPeirceReservior",
        "S66": "KranjiReservior",
        "S33": "PandanReservior1",
        "S71": "PandanReservior2",
        "S35": "PandanReservior3",
        "S07": "MacRitchieReservior",
        "S119": "MarinaReservior",
        "S81": "PunggolConeyReservior",
        "S900": "YishunDam",
        "S220": "PunggolParkPond",
        "S107": "BedokJetty",
        "S84": "BedokReservior",
        "S108": "MarinaBarrage",
        "S94": "DBestFishing",
    }

    total_rainfall_by_device_id = {
        "S109": 0,
        "S40": 0,
        "S08": 0,
        "S69": 0,
        "S66": 0,
        "S33": 0,
        "S71": 0,
        "S35": 0,
        "S07": 0,
        "S119": 0,
        "S81": 0,
        "S900": 0,
        "S220": 0,
        "S107": 0,
        "S84": 0,
        "S108": 0,
        "S94": 0,
    }

    # Initializing Data Required for GET Request
    today = datetime.now()
    rainfall_request_url = "https://api.data.gov.sg/v1/environment/rainfall"
    params = {
        "date": today.strftime("%Y-%m-%d")
    }

    # Making GET Request
    response = requests.get(rainfall_request_url, params=params)
    rainfall_data = response.json()["items"]

    # Calculating Total Rainfall by Device ID
    for perrecord in rainfall_data:
        for reading in perrecord["readings"]:
            if reading["station_id"] in applicable_device_ids_mapping:
                total_rainfall_by_device_id[reading["station_id"]] += reading["value"]

    text = "Today's Total Rainfall by Area:\n\n"

    # Printing Total Rainfall by Device ID
    for device_id, rainfall in total_rainfall_by_device_id.items():
        text += "{}: {:.2f}mm\n".format(applicable_device_ids_mapping[device_id], rainfall)
    text += "\n\nNote: With high amount of rainfall, some anglers may find it difficult to fish as the water may be murky and the fish may not be biting. Thus, do remember to bring along darker cloured lures to increase your chances of catching fish. However, do note that this assumption are based on terrain and depth of water."

    bot.reply_to(message, text)

@bot.message_handler(commands=['2hr_forecast'])
def twohr_rainforecast(message):

    # Initializing Data Required for GET Request
    request_url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    params = {
        "date_time": current_time
    }

    # Making GET Request
    response = requests.get(request_url, params=params)
    forecast_data = response.json()

    # Data Processing
    start_validity = forecast_data["items"][0]["valid_period"]["start"]
    stop_validity = forecast_data["items"][0]["valid_period"]["end"]
    updated_time = forecast_data["items"][0]["update_timestamp"]
    forecast_weather = forecast_data["items"][0]["forecasts"]

    text = """2-Hour Weather Forecast\n
    Updated At: {}\n\n""".format(updated_time)

    for forecast in forecast_weather:
        text += "{} | {}\n".format(forecast["area"], forecast["forecast"])

    bot.reply_to(message, text)

@bot.message_handler(commands=['24hr_forecast'])
def twentyfourhr_rainforecast(message):
     
    # Initializing Data Required for GET Request
    request_url = "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast"
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    params = {
        "date_time": current_time
    }

    # Making GET Request
    response = requests.get(request_url, params=params)
    forecast_data = response.json()

    # Data Processing
    start_validity = forecast_data["items"][0]["valid_period"]["start"]
    stop_validity = forecast_data["items"][0]["valid_period"]["end"]
    updated_time = datetime.strptime(forecast_data["items"][0]["update_timestamp"], "%Y-%m-%dT%H:%M:%S%z").strftime("%H:%M")
    forecast_weather = forecast_data["items"][0]["periods"]

    text = """24-Hour Weather Forecast\n
    Updated At: {}Hrs\n\n""".format(updated_time)

    for count, forecast in enumerate(forecast_weather):
        start_cleaned_date = datetime.strptime(forecast["time"]["start"], "%Y-%m-%dT%H:%M:%S%z").strftime("%H-%M")
        end_cleaned_date = datetime.strptime(forecast["time"]["end"], "%Y-%m-%dT%H:%M:%S%z").strftime("%H-%M")
        if count == len(forecast_weather) - 1:
            text += "Next Morning [ {} - {} ]\n".format(start_cleaned_date, end_cleaned_date)
        elif start_cleaned_date == "00-00" or end_cleaned_date == "12-00":
            text += "Morning [ {} - {} ]\n".format(start_cleaned_date, end_cleaned_date)
        elif start_cleaned_date == "12-00" or end_cleaned_date == "18-00":
            text += "Afternoon [ {} - {} ]\n".format(start_cleaned_date, end_cleaned_date)
        elif start_cleaned_date == "18-00" or end_cleaned_date == "06-00":
            text += "Night [ {} - {} ]\n".format(start_cleaned_date, end_cleaned_date)
        else: 
            print("Error in Time Formatting")


        for region, condition in forecast["regions"].items():
            if region == "east":
                text += "{}      | {}\n".format(region.capitalize(), condition)
            elif region == "west":
                text += "{}     | {}\n".format(region.capitalize(), condition)
            elif region == "south" or region == "north":
                text += "{}   | {}\n".format(region.capitalize(), condition)
            else:
                text += "{} | {}\n".format(region.capitalize(), condition)
        text += "\n"

    bot.reply_to(message, text)

@bot.message_handler(commands=['tides'])
def tides(message):
    
    # Initializing Data Required for GET Request
    request_url = "https://vincentneo.github.io/SGTideTimings/latest.json"

    # Making GET Request
    response = requests.get(request_url)
    tide_response = response.json()

    # Initialize an empty dictionary to store the formatted tide data
    tide_data = {}

    # Iterate through each item in the JSON response
    for item in tide_response:
        # Extract and format the date
        date_formated = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.000+08:00")
        date_key = date_formated.strftime("%d/%m")
        
        # Format the tide information
        tide_info = f"{item['classification']}: {date_formated.strftime('%H:%M')}Hrs {item['height']}m"
        
        # Check if the date key already exists in the dictionary
        if date_key in tide_data:
            # Append the tide information to the existing key
            tide_data[date_key] += "\n" + tide_info
        else:
            # Create a new key with the tide information
            tide_data[date_key] = tide_info

    if tide_data=={}:
        bot.reply_to(message, "Sorry, there is no tide data available.")
    else:
        msg = bot.reply_to(message, "Please enter a date (DD/MM) within this current month to get the tide data:")
        bot.register_next_step_handler(msg, process_date_step, tide_data)

# Function to process the date entered by the user
def process_date_step(message, tide_data):
    chat_id = message.chat.id
    date = message.text
    # Continuously prompt the user to enter a valid date if the input is invalid
    if len(date) != 5 or date[2] != "/" or not date[:2].isdigit() or not date[3:].isdigit() or int(date[:2]) > 31 or int(date[3:]) > 12:
        msg = bot.send_message(chat_id, "Please enter a valid date in the format DD/MM within this current month:")
        bot.register_next_step_handler(msg, process_date_step, tide_data)
        return

    if date in tide_data:
        cleandate1 = date.split("/")[0]
        cleandate2 = date.split("/")[1]
        cleanyear = datetime.now().year
        visualapi = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Singapore/{cleanyear}-{cleandate2}-{cleandate1}?key={visualcrossing_key}&include=days&elements=datetime,moonphase,sunrise,sunset"
        visual_response = requests.get(visualapi)
        visual_data = visual_response.json()
        bot.send_message(chat_id, f"Tide data for {date} are as follows.\nTraditional, western moon cycles are therefore represented by the following values:\n0 – new moon\n0-0.25 – waxing crescent\n0.25 – first quarter\n0.25-0.5 – waxing gibbous\n0.5 – full moon\n0.5-0.75 – waning gibbous\n0.75 – last quarter\n0.75 -1 – waning crescent\n\nTides\n{tide_data[date]}\n\nSunrise: {visual_data['days'][0]['sunrise']}\nSunset: {visual_data['days'][0]['sunset']}\nMoonPhase: {visual_data['days'][0]['moonphase']}")
    else:
        bot.send_message(chat_id, "Sorry, there is no tide data available for the selected date.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "I'm sorry, I don't understand that command. Please type /help for list of commands.")

bot.infinity_polling()




