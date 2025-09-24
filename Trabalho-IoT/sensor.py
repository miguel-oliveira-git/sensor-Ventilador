import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"
port = 1883
topic_temperatura = "estufa/temperatura"

def conectar(client, userdata, flags, rc):
    if rc == 0:
        print("Sensor conectado ao broker MQTT com sucesso.")
    else:
        print("Falha na conexão do sensor: ", rc)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "SensorTemperatura")
client.on_connect = conectar
client.connect(broker_address, port)

try:
    while True:
        temperatura = round(random.uniform(15.0, 30.0), 2)
        print(f"Publicando temperatura: {temperatura}°C")
        client.publish(topic_temperatura, str(temperatura))
        time.sleep(5)
except KeyboardInterrupt:
    print("Simulação do sensor encerrada.")
    client.disconnect()