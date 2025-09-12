

def sensorStub():
    return {
        'temperatureInC': 50, 'precipitation': 70,
        'humidity': 26, 'windSpeedKMPH': 52
    }

def classify_weather(readings):
    weather = "Sunny Day"
    
    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
    
def report(sensorReader):
    return classify_weather(sensorReader())

if __name__ == '__main__':
    print(report(sensorStub))
    print("All is well (maybe!)");
