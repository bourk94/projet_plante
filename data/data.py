#!/usr/bin/env python3
pins = {
    "motorPins" : (12, 16, 18, 22),
    "pumpPin" : 31,
    "dthPin" : 13,
    "lightPin" : 29,
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
            "percent" : 0,
            "moistureSensorDelay" : 3600,
}

roomData = { "humidity" : 0,
            "temperature" : 0,
}