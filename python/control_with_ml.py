import joblib, serial, time

model = joblib.load('../models/ml_model.pkl')
arduino = serial.Serial('COM3', 9600)

def read_temp():
    arduino.write(b'R')
    return float(arduino.readline().decode().strip())

def send_command(cmd):
    arduino.write(str(cmd).encode())

while True:
    temp = read_temp()
    action = model.predict([[temp]])[0]
    send_command(action)
    time.sleep(5)
