import json
import random

class IoTDevice:
    def __init__(self, device_id, device_type, sensor_types):
        self.device_id = device_id
        self.device_type = device_type
        self.sensor_types = sensor_types
        self.sensors = {}
        for sensor in sensor_types:
            self.sensors[sensor] = None

    def simulate_sensors(self):
        for sensor in self.sensors:
            if sensor == 'temperature':
                self.sensors[sensor] = round(random.uniform(20.0, 30.0), 2)
            elif sensor == 'humidity':
                self.sensors[sensor] = round(random.uniform(50.0, 80.0), 2)
            elif sensor == 'pressure':
                self.sensors[sensor] = round(random.uniform(900.0, 1100.0), 2)
            else:
                self.sensors[sensor] = 'Unknown sensor type'

    def get_device_data(self):
        return {
            'device_id': self.device_id,
            'device_type': self.device_type,
            'sensors': self.sensors
        }


class IoTDeviceSimulator:
    def __init__(self, num_devices):
        self.devices = []
        for i in range(num_devices):
            device_id = f'Device-{i+1}'
            device_type = random.choice(['Sensor', 'Actuator'])
            sensor_types = random.sample(['temperature', 'humidity', 'pressure'], random.randint(1, 3))
            self.devices.append(IoTDevice(device_id, device_type, sensor_types))

    def simulate_all_devices(self):
        for device in self.devices:
            device.simulate_sensors()

    def get_all_device_data(self):
        return [device.get_device_data() for device in self.devices]


# Example usage:
simulator = IoTDeviceSimulator(5)
simulator.simulate_all_devices()
all_device_data = simulator.get_all_device_data()
print(json.dumps(all_device_data, indent=4))