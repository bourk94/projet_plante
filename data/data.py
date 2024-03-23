#!/usr/bin/env python3
pins = {
    "motorPins" : (12, 16, 18, 22),
    "pumpPin" : 38,
    "dthPin" : 37,
    "lightPin" : 40,
    "ledPins" : { "red" : 33, "green" : 31, "blue" : 29 },
}

mqttConfig = {
    "broker" : "172.16.72.221",
    "localhost" : "127.0.0.1",
    "port" : 1883,
}

motorPostions = {
    1 : (1, 2, 128),
    2 : (2, 2, 384),
    3 : (1, 2, 128),
    4 : (1, 2, 128),
}


wateringData = { "is_moist" : True,
            "percent" : 100,
            "moistureSensorDelay" : 3600,
}

roomData = { "humidity" : 0,
            "temperature" : 0,
}

ledColor = {
    "red" : { "r" : 75, "g" : 0, "b" : 0 },
    "green" : { "r" : 0, "g" : 75, "b" : 0 },
    "yellow" : { "r" : 171, "g" : 150, "b" : 0 },
}