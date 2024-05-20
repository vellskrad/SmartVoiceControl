import sounddevice as sd

# Вывести все доступные устройства
print(sd.query_devices())

# Вывести параметры устройства по умолчанию
device = sd.default.device
print(sd.query_devices(device[1], 'input'))
