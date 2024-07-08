from fastapi import FastAPI
from datetime import datetime, timedelta
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ystd_rainfall/")
def ystd_rainfall():

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

    total_rainfall_by_location = {
        "LowerSeletarReservior": 0,
        "UpperSeletarReservior": 0,
        "LowerPeirceReservior": 0,
        "UpperPeirceReservior": 0,
        "KranjiReservior": 0,
        "PandanReservior1": 0,
        "PandanReservior2": 0,
        "PandanReservior3": 0,
        "MacRitchieReservior": 0,
        "MarinaReservior": 0,
        "PunggolConeyReservior": 0,
        "YishunDam": 0,
        "PunggolParkPond": 0,
        "BedokJetty": 0,
        "BedokReservior": 0,
        "MarinaBarrage": 0,
        "DBestFishing": 0,
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

    # Calculating Total Rainfall by Location
    for device_id, rainfall in total_rainfall_by_device_id.items():
        total_rainfall_by_location[applicable_device_ids_mapping[device_id]] += rainfall

    # Printing Total Rainfall by Device ID
    # for device_id, rainfall in total_rainfall_by_device_id.items():
    #     print(f"{applicable_device_ids_mapping[device_id]}: {rainfall}mm")
    return total_rainfall_by_location

@app.get("/tdy_rainfall/")
def tdy_rainfall():

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

    total_rainfall_by_location = {
        "LowerSeletarReservior": 0,
        "UpperSeletarReservior": 0,
        "LowerPeirceReservior": 0,
        "UpperPeirceReservior": 0,
        "KranjiReservior": 0,
        "PandanReservior1": 0,
        "PandanReservior2": 0,
        "PandanReservior3": 0,
        "MacRitchieReservior": 0,
        "MarinaReservior": 0,
        "PunggolConeyReservior": 0,
        "YishunDam": 0,
        "PunggolParkPond": 0,
        "BedokJetty": 0,
        "BedokReservior": 0,
        "MarinaBarrage": 0,
        "DBestFishing": 0,
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

    # Calculating Total Rainfall by Location
    for device_id, rainfall in total_rainfall_by_device_id.items():
        total_rainfall_by_location[applicable_device_ids_mapping[device_id]] += rainfall

    # Printing Total Rainfall by Device ID
    # for device_id, rainfall in total_rainfall_by_device_id.items():
    #     print(f"{applicable_device_ids_mapping[device_id]}: {rainfall}mm")
    return total_rainfall_by_location

@app.get("/twohr_rainforecast/")
def twohr_rainforecast():

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

    return {
        "start_validity": start_validity,
        "stop_validity": stop_validity,
        "forecast_weather": forecast_weather,
        "updated_time": updated_time
    }

@app.get("/twentyfourhr_rainforecast/")
def twentyfourhr_rainforecast():

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
    updated_time = forecast_data["items"][0]["update_timestamp"]
    forecast_weather = forecast_data["items"][0]["periods"]

    return {
        "start_validity": start_validity,
        "stop_validity": stop_validity,
        "forecast_weather": forecast_weather,
        "updated_time": updated_time
    }

